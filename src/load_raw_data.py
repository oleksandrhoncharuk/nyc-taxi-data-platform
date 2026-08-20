import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

TRIPS_FILE = "data/raw/yellow_tripdata_2026-01.parquet"
ZONES_FILE = "data/raw/taxi_zone_lookup.csv"

def main():
    load_dotenv()

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")

    database_url = (
        f"postgresql+psycopg://"
        f"{user}:{password}@{host}:{port}/{database}"
    )

    engine = create_engine(database_url)

    print("Reading taxi zones...")
    zones = pd.read_csv(ZONES_FILE)

    print("Loading taxi zones into PostgreSQL...")
    zones.to_sql(
        name="taxi_zones",
        con=engine,
        schema="raw",
        if_exists="replace",
        index=False,
    )

    print("Reading yellow taxi trips...")
    trips = pd.read_parquet(TRIPS_FILE)

    print(f"Trips to load: {len(trips)}")

    print("Loading trips into PostgreSQL...")
    trips.to_sql(
        name="yellow_taxi_trips",
        con=engine,
        schema="raw",
        if_exists="replace",
        index=False,
        chunksize=10_000,
    )

    print("Loading completed.")

if __name__ == "__main__":
    main()