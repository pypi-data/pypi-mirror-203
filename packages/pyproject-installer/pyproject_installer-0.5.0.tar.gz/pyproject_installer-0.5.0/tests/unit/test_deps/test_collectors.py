from copy import deepcopy
import json
import textwrap

import pytest

from pyproject_installer.deps_cmd import deps_command
from pyproject_installer.deps_cmd.collectors import (
    get_collector,
    MetadataCollector,
    SUPPORTED_COLLECTORS,
)
from pyproject_installer.deps_cmd.collectors.collector import Collector


def test_get_collector_missing():
    collector = get_collector("foo")
    assert collector is None


def test_get_collector():
    collector = get_collector("metadata")
    assert collector is MetadataCollector


def test_supported_collectors():
    assert isinstance(SUPPORTED_COLLECTORS, dict)
    for k, v in SUPPORTED_COLLECTORS.items():
        assert isinstance(k, str)
        assert issubclass(v, Collector)


@pytest.fixture
def pyproject_with_backend(pyproject, monkeypatch):
    """Generates pyproject with self-hosted build backend"""

    def _build_backend_src(be_content):
        be_module = "be"
        pyproject_toml_content = textwrap.dedent(
            f"""\
            [build-system]
            requires=[]
            build-backend="{be_module}"
            backend-path=["."]
            """
        )
        pyproject_path = pyproject(pyproject_toml_content)

        backend_path = pyproject_path / be_module
        backend_path.mkdir()
        (backend_path / "__init__.py").write_text(be_content)

        monkeypatch.chdir(pyproject_path)
        return pyproject_path

    return _build_backend_src


@pytest.fixture
def pyproject_metadata(pyproject_with_backend):
    """Build backend with prepare_metadata_for_build_wheel"""

    def _core_metadata(reqs):
        content_fields = [
            "Metadata-Version: 2.1",
            "Name: foo",
            "Version: 1.0",
        ]
        for req in reqs:
            content_fields.append(f"Requires-Dist: {req}")

        be_content = textwrap.dedent(
            """\
            def prepare_metadata_for_build_wheel(
                metadata_directory, config_settings=None
            ):
                from pathlib import Path

                distinfo = "foo-1.0.dist-info"
                distinfo_path = Path(metadata_directory) / distinfo
                distinfo_path.mkdir()
                metadata_path = distinfo_path / "METADATA"
                content = "{content}"

                metadata_path.write_text(content, encoding="utf-8")

                return distinfo
            """
        ).format(content="\\n".join(content_fields) + "\\n")
        return pyproject_with_backend(be_content)

    return _core_metadata


@pytest.fixture
def pyproject_pep517_wheel(pyproject_with_backend):
    """Build backend with get_requires_for_build_wheel"""

    def _pep517_wheel(reqs):
        be_content = textwrap.dedent(
            f"""\
            def get_requires_for_build_wheel(config_settings=None):
                return {reqs}
            """
        )
        return pyproject_with_backend(be_content)

    return _pep517_wheel


@pytest.fixture
def pyproject_pep518(pyproject, monkeypatch):
    """pyproject.toml with PEP518 deps"""

    def _pyproject_pep518(reqs):
        toml_content = textwrap.dedent(
            f"""\
            [build-system]
            build-backend = "be"
            requires = {reqs}
            """
        )
        pyproject_path = pyproject(toml_content)
        monkeypatch.chdir(pyproject_path)
        return pyproject_path

    return _pyproject_pep518


@pytest.fixture
def pip_reqfile(tmpdir, monkeypatch):
    """pip's requirements.txt file"""

    def _pip_reqfile(content):
        reqfile_path = tmpdir / "requirements.txt"
        reqfile_path.write_text(content, encoding="utf-8")
        monkeypatch.chdir(tmpdir)
        return reqfile_path

    return _pip_reqfile


@pytest.fixture
def poetry_deps(tmpdir, monkeypatch):
    """poetry deps"""

    def _poetry_deps(content):
        pyproject_toml_path = tmpdir / "pyproject.toml"
        pyproject_toml_path.write_text(content, encoding="utf-8")
        monkeypatch.chdir(tmpdir)
        return pyproject_toml_path

    return _poetry_deps


@pytest.fixture
def tox_deps(tmpdir, monkeypatch):
    """tox deps in specified format"""

    def _tox_deps(config_type, testenv, deps):
        if config_type == "toml":
            config_path = tmpdir / "pyproject.toml"
            contents = ["[tool.tox]", "legacy_tox_ini = '''", f"[{testenv}]"]
            if deps is not None:
                contents.append("deps =")
                contents.extend((f"    {x}" for x in deps))
            contents.append("'''")

        elif config_type == "ini":
            config_path = tmpdir / "tox.ini"
            contents = [f"[{testenv}]"]
            if deps is not None:
                contents.append("deps =")
                contents.extend((f"    {x}" for x in deps))
        else:
            raise ValueError(f"Unsupported tox config type: {config_type}")

        config_path.write_text("\n".join(contents) + "\n", encoding="utf-8")
        monkeypatch.chdir(tmpdir)
        return config_path

    return _tox_deps


PEP508_DEPS_DATA = (
    ([], []),
    (["foo"], ["foo"]),
    (["foo == 1.0"], ["foo == 1.0"]),
    (
        ["foo @ https://example.com/foo.zip"],
        ["foo @ https://example.com/foo.zip"],
    ),
    (["foo [test]"], ["foo [test]"]),
    (["foo [test] > 1.0"], ["foo [test] > 1.0"]),
    (["foo [test] > 1.0", "bar"], ["bar", "foo [test] > 1.0"]),
    (["Fo_.--o"], ["Fo_.--o"]),
    (["bar", "foo"], ["bar", "foo"]),
    (["foo", "bar"], ["bar", "foo"]),
    (["foo", "bar > 1.0"], ["bar > 1.0", "foo"]),
    (
        ["foo", "bar > 1.0; python_version == '1.0'"],
        ["bar > 1.0; python_version == '1.0'", "foo"],
    ),
    (["_foo"], []),
    (["foo", "bar !> 1.0"], ["foo"]),
    (["foo", "bar > 1.0; invalid_marker == '1.0'"], ["foo"]),
)


@pytest.mark.parametrize("deps_data", PEP508_DEPS_DATA)
def test_metadata_collector(deps_data, pyproject_metadata, depsconfig):
    """Collection of core metadata"""
    # prepare source config
    srcname = "foo"
    collector = "metadata"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    in_reqs, out_reqs = deps_data

    # configure pyproject with build backend
    pyproject_metadata(in_reqs)

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


def test_metadata_collector_unsupported(pyproject_with_backend, depsconfig):
    """Build backend doesn't support prepare_metadata_for_build_wheel"""
    # prepare source config
    srcname = "foo"
    collector = "metadata"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    # configure pyproject with build backend
    pyproject_with_backend("")

    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = (
        "Backend doesn't support prepare_metadata_for_build_wheel hook"
    )
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


def test_pep518_collector_missing_pyproject_toml(
    tmpdir, depsconfig, monkeypatch
):
    """Collection of pep518 reqs with missing pyproject.toml"""
    # prepare source config
    srcname = "foo"
    collector = "pep518"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    monkeypatch.chdir(tmpdir)
    assert not (tmpdir / "pyproject.toml").exists()

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    expected_conf["sources"][srcname]["deps"] = ["setuptools", "wheel"]
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


def test_pep518_collector_missing_build_system(
    pyproject, depsconfig, monkeypatch
):
    """Collection of pep518 reqs with missing build-system"""
    # prepare source config
    srcname = "foo"
    collector = "pep518"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    pyproject_path = pyproject("")
    monkeypatch.chdir(pyproject_path)

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    expected_conf["sources"][srcname]["deps"] = ["setuptools", "wheel"]
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize("deps_data", PEP508_DEPS_DATA)
def test_pep518_collector(deps_data, pyproject_pep518, depsconfig):
    """Collection of pep518 reqs"""
    # prepare source config
    srcname = "foo"
    collector = "pep518"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    in_reqs, out_reqs = deps_data

    pyproject_pep518(in_reqs)
    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize("deps_data", PEP508_DEPS_DATA)
def test_pep517_collector(deps_data, pyproject_pep517_wheel, depsconfig):
    """Collection of pep517 wheel reqs"""
    # prepare source config
    srcname = "foo"
    collector = "pep517"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    in_reqs, out_reqs = deps_data

    # configure pyproject with build backend
    pyproject_pep517_wheel(in_reqs)

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


def test_pep517_collector_missing_hook(pyproject_with_backend, depsconfig):
    """Build backend doesn't have get_requires_for_build_wheel"""
    # prepare source config
    srcname = "foo"
    collector = "pep517"
    input_conf = {"sources": {srcname: {"srctype": collector}}}
    depsconfig_path = depsconfig(json.dumps(input_conf))

    # configure pyproject with build backend
    pyproject_with_backend("")

    deps_command("sync", depsconfig_path, srcnames=[])

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


@pytest.mark.parametrize("deps_data", PEP508_DEPS_DATA)
def test_pipreqfile_collector(deps_data, pip_reqfile, depsconfig):
    """Collection of pip's reqs"""
    # prepare source config
    srcname = "foo"
    collector = "pip_reqfile"

    in_reqs, out_reqs = deps_data

    pip_reqfile_path = pip_reqfile("\n".join(in_reqs) + "\n")

    input_conf = {
        "sources": {
            srcname: {"srctype": collector, "srcargs": [str(pip_reqfile_path)]},
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize(
    "deps_data",
    (
        (["-r other-requirements.txt"], []),
        (["-r other-requirements.txt", "foo"], ["foo"]),
        (["-c constraints.txt"], []),
        (["-c constraints.txt", "foo"], ["foo"]),
        (["# comment"], []),
        (["# comment", "foo"], ["foo"]),
        (["foo # comment"], ["foo"]),
        (["./foo.whl"], []),
        (["./foo.whl", "bar"], ["bar"]),
        (["https://example.com/foo.whl"], []),
        (["https://example.com/foo.whl", "bar"], ["bar"]),
        (["\\"], []),
        (["foo", "\\", " > 1.0"], ["foo"]),
    ),
)
def test_pipreqfile_collector_unsupported_deps(
    deps_data, pip_reqfile, depsconfig
):
    """Collection of pip's unsupported reqs"""
    # prepare source config
    srcname = "foo"
    collector = "pip_reqfile"

    in_reqs, out_reqs = deps_data

    pip_reqfile_path = pip_reqfile("\n".join(in_reqs) + "\n")

    input_conf = {
        "sources": {
            srcname: {"srctype": collector, "srcargs": [str(pip_reqfile_path)]},
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize(
    "deps_data",
    (
        ([], []),
        (['_foo = "*"'], []),
        (['foo = { git = "https://example.com/bar.git" }'], ["foo"]),
        (['foo = { url = "https://example.com/foo-1.0.tar.gz" }'], ["foo"]),
        (['foo = { version = "^2.0.1", python = "<3.11" }'], ["foo"]),
        (
            ['foo = {version = "^2.2", markers = "python_version <= \'3.4\'"}'],
            ["foo;python_version <= '3.4'"],
        ),
        (
            ['foo = {version = "^2.2", markers = "invalid_marker == \'3.4\'"}'],
            ["foo"],
        ),
        (
            [
                "foo = [",
                '    {version = "<=1.9", python = ">=3.6,<3.8"},',
                '    {version = "^2.0", python = ">=3.8"},',
                "]",
            ],
            ["foo"],
        ),
        (['foo = { path = "foo-1.0.tar.gz" }'], ["foo"]),
        (['foo = "*"', 'bar = "*"'], ["bar", "foo"]),
        (['bar = "*"', 'foo = "*"'], ["bar", "foo"]),
        (['Foo = "*"'], ["Foo"]),
        (['foo = "~1.2.3"', 'bar = "^1.2.3"'], ["bar", "foo"]),
    ),
)
@pytest.mark.parametrize(
    "notation",
    ("tool.poetry.group.dev.dependencies", "tool.poetry.dev-dependencies"),
)
def test_poetry_collector(deps_data, notation, poetry_deps, depsconfig):
    """Collection of poetry deps"""
    # prepare source config
    srcname = "foo"
    collector = "poetry"

    input_conf = {
        "sources": {srcname: {"srctype": collector, "srcargs": ["dev"]}}
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    in_reqs, out_reqs = deps_data

    poetry_content = f"[{notation}]\n"
    poetry_content += "\n".join(in_reqs) + "\n"
    poetry_deps(poetry_content)

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize("poetry_config", ("", "[tool]"))
def test_poetry_collector_missing_config(
    poetry_config, poetry_deps, depsconfig
):
    """Collection of poetry's with missing config"""
    # prepare source config
    srcname = "foo"
    collector = "poetry"
    groupname = "bar"

    input_conf = {
        "sources": {srcname: {"srctype": collector, "srcargs": [groupname]}}
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    poetry_deps(poetry_config + "\n")

    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = "Poetry is not configured: missing tool.poetry"
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


@pytest.mark.parametrize(
    "poetry_config",
    ("[tool.poetry]", "[tool.poetry.group]", "[tool.poetry.group.test]"),
)
def test_poetry_collector_wrong_group(poetry_config, poetry_deps, depsconfig):
    """Collection of poetry's wrong group"""
    # prepare source config
    srcname = "foo"
    collector = "poetry"
    groupname = "bar"

    input_conf = {
        "sources": {srcname: {"srctype": collector, "srcargs": [groupname]}}
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    poetry_deps(poetry_config + "\n")

    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = (
        f"{groupname} is not configured: missing tool.poetry.group.{groupname}"
    )
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


def test_poetry_collector_missing_dependencies(poetry_deps, depsconfig):
    """Collection of poetry's missing dependencies"""
    # prepare source config
    srcname = "foo"
    collector = "poetry"
    groupname = "bar"

    input_conf = {
        "sources": {srcname: {"srctype": collector, "srcargs": [groupname]}}
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))
    poetry_deps(f"[tool.poetry.group.{groupname}]\n")

    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = (
        f"Dependencies are not configured for {groupname}: "
        f"missing tool.poetry.group.{groupname}.dependencies"
    )
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


@pytest.mark.parametrize("deps_data", PEP508_DEPS_DATA)
@pytest.mark.parametrize("config_type", ("toml", "ini"))
def test_tox_collector(deps_data, config_type, tox_deps, depsconfig):
    """Collection of tox deps"""
    # prepare source config
    srcname = "foo"
    collector = "tox"
    testenv = "testenv"

    in_reqs, out_reqs = deps_data

    tox_config_path = tox_deps(config_type, testenv, in_reqs)
    input_conf = {
        "sources": {
            srcname: {
                "srctype": collector,
                "srcargs": [str(tox_config_path), testenv],
            },
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize(
    "deps_data",
    (
        (["-r requirements.txt"], []),
        (["-r requirements.txt", "foo"], ["foo"]),
        (["-c constraints.txt"], []),
        (["-c constraints.txt", "foo"], ["foo"]),
    ),
)
@pytest.mark.parametrize("config_type", ("toml", "ini"))
def test_tox_collector_unsupported(
    deps_data, config_type, tox_deps, depsconfig
):
    """Collection of unsupported tox formats"""
    # prepare source config
    srcname = "foo"
    collector = "tox"
    testenv = "testenv"

    in_reqs, out_reqs = deps_data

    tox_config_path = tox_deps(config_type, testenv, in_reqs)
    input_conf = {
        "sources": {
            srcname: {
                "srctype": collector,
                "srcargs": [str(tox_config_path), testenv],
            },
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    deps_command("sync", depsconfig_path, srcnames=[])

    expected_conf = deepcopy(input_conf)
    if out_reqs:
        expected_conf["sources"][srcname]["deps"] = out_reqs
    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == expected_conf


@pytest.mark.parametrize("tox_config", ("", "[tool]", "[tool.tox]"))
def test_tox_collector_missing_configuration(
    tox_config, tmpdir, depsconfig, monkeypatch
):
    """Collection of tox with missing configuration"""
    # prepare source config
    srcname = "foo"
    collector = "tox"

    tox_config_path = tmpdir / "pyproject.toml"
    tox_config_path.write_text(tox_config + "\n", encoding="utf-8")
    input_conf = {
        "sources": {
            srcname: {
                "srctype": collector,
                "srcargs": [str(tox_config_path), "testenv"],
            },
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    monkeypatch.chdir(tmpdir)
    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = "Tox is not configured: missing tool.tox.legacy_tox_ini"
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


@pytest.mark.parametrize("config_type", ("toml", "ini"))
def test_tox_collector_missing_testenv(config_type, tox_deps, depsconfig):
    """Collection of missing tox testenv"""
    # prepare source config
    srcname = "foo"
    collector = "tox"
    testenv = "foo"

    tox_config_path = tox_deps(config_type, "testenv", [])

    input_conf = {
        "sources": {
            srcname: {
                "srctype": collector,
                "srcargs": [str(tox_config_path), testenv],
            },
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = f"Test environment is not configured: {testenv}"
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf


@pytest.mark.parametrize("config_type", ("toml", "ini"))
def test_tox_collector_missing_deps(config_type, tox_deps, depsconfig):
    """Collection of missing tox deps"""
    # prepare source config
    srcname = "foo"
    collector = "tox"
    testenv = "foo"

    tox_config_path = tox_deps(config_type, testenv, None)

    input_conf = {
        "sources": {
            srcname: {
                "srctype": collector,
                "srcargs": [str(tox_config_path), testenv],
            },
        }
    }
    depsconfig_path = depsconfig(json.dumps(input_conf))

    with pytest.raises(ValueError) as exc:
        deps_command("sync", depsconfig_path, srcnames=[])
    expected_err = (
        f"Dependencies are not configured for {testenv}: missing {testenv}.deps"
    )
    assert expected_err in str(exc.value)

    actual_conf = json.loads(depsconfig_path.read_text(encoding="utf-8"))
    assert actual_conf == input_conf
