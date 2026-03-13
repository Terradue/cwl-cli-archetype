from pathlib import Path

from click.testing import CliRunner

from cwl_cli_archetype.cli import main


def test_cli_requires_mandatory_options():
    runner = CliRunner()

    result = runner.invoke(main, [])

    assert result.exit_code != 0
    assert "Missing option '--clt-id'" in result.output


def test_cli_passes_multiple_ids_and_target_dir(monkeypatch, tmp_path):
    runner = CliRunner()
    captured = {}

    def fake_create_archetype(clt_ids, target_dir):
        captured["clt_ids"] = clt_ids
        captured["target_dir"] = target_dir

    monkeypatch.setattr("cwl_cli_archetype.cli.create_archetype", fake_create_archetype)

    result = runner.invoke(
        main,
        [
            "--clt-id",
            "alpha",
            "--clt-id",
            "beta",
            "--target-dir",
            str(tmp_path),
        ],
    )

    assert result.exit_code == 0
    assert captured["clt_ids"] == ("alpha", "beta")
    assert captured["target_dir"] == Path(tmp_path)
