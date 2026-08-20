from pathlib import Path
from urllib.request import urlretrieve

RAW_DIR = Path("data/raw")

TRIPS_URL = (
    "https://d37ci6vzurychx.cloudfront.net/"
    "trip-data/yellow_tripdata_2026-01.parquet"
)

ZONES_URL = (
    "https://d37ci6vzurychx.cloudfront.net/"
    "misc/taxi_zone_lookup.csv"
)

def download_file(url: str, destination: Path):
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        print(f"Already exists, skipping: {destination}")
        return

    print(f"Donwloading {url}")
    urlretrieve(url, destination)
    print(f"Downloaded: {destination}")

def main():
    download_file(
        TRIPS_URL,
        RAW_DIR / "yellow_tripdata_2026-01.parquet",
    )

    download_file(
        ZONES_URL,
        RAW_DIR / "taxi_zone_lookup.csv",
    )

if __name__ == "__main__":
    main()