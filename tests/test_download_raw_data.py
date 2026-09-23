from src import download_raw_data


def test_download_file_skips_existing_file(tmp_path, monkeypatch):
    destination = tmp_path / "existing.parquet"
    destination.write_text("already exists")

    def fail_if_called(*args, **kwargs):
        raise AssertionError("urlretrieve should not be called")

    monkeypatch.setattr(
        download_raw_data,
        "urlretrieve",
        fail_if_called,
    )

    download_raw_data.download_file(
        "https://example.com/file.parquet",
        destination,
    )
