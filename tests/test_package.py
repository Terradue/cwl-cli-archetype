from importlib.metadata import PackageNotFoundError

from cwl_cli_archetype import (
    _get_version,
    _serialize_template,
    _to_mapping,
    create_archetype,
)


def _sample_filter(value):
    return value


def test_to_mapping_uses_trimmed_private_function_names():
    mapping = _to_mapping([_sample_filter])

    assert mapping == {"sample_filter": _sample_filter}


def test_get_version_returns_installed_package_version(monkeypatch):
    monkeypatch.setattr("cwl_cli_archetype.version", lambda _: "1.2.3")

    assert _get_version() == "1.2.3"


def test_get_version_returns_na_when_package_is_missing(monkeypatch):
    def raise_package_not_found(_: str):
        raise PackageNotFoundError

    monkeypatch.setattr("cwl_cli_archetype.version", raise_package_not_found)

    assert _get_version() == "N/A"


def test_serialize_template_renders_template_content(tmp_path, monkeypatch):
    monkeypatch.setattr("cwl_cli_archetype._get_version", lambda: "9.9.9")

    output_file = tmp_path / "sample" / "Dockerfile"
    _serialize_template("demo-tool", ["demo-tool"], "Dockerfile", output_file)

    content = output_file.read_text()

    assert output_file.exists()
    assert "ENV VIRTUAL_ENV=/app/envs/demo-tool" in content
    assert "COPY --chown=1001:0 . /app" in content


def test_create_archetype_creates_cwl_and_one_dockerfile_per_clt(tmp_path, monkeypatch):
    monkeypatch.setattr("cwl_cli_archetype._get_version", lambda: "2.0.0")

    create_archetype(["alpha", "beta"], tmp_path)

    workflow_file = tmp_path / "cwl-workflow" / "clts.cwl"
    alpha_dockerfile = tmp_path / "alpha" / "Dockerfile"
    beta_dockerfile = tmp_path / "beta" / "Dockerfile"

    workflow_content = workflow_file.read_text()
    alpha_content = alpha_dockerfile.read_text()
    beta_content = beta_dockerfile.read_text()

    assert workflow_file.exists()
    assert alpha_dockerfile.exists()
    assert beta_dockerfile.exists()
    assert "id: alpha" in workflow_content
    assert "id: beta" in workflow_content
    assert "dockerPull: <registry>/<image-prefix>/alpha:0.0.1" in workflow_content
    assert "dockerPull: <registry>/<image-prefix>/beta:0.0.1" in workflow_content
    assert "ENV VIRTUAL_ENV=/app/envs/alpha" in alpha_content
    assert "ENV VIRTUAL_ENV=/app/envs/beta" in beta_content
