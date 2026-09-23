import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text

DATA_MONTH = os.getenv("DATA_MONTH", "2026-01")

TRIPS_FILE = f"data/raw/yellow_tripdata_{DATA_MONTH}.parquet"
ZONES_FILE = "data/raw/taxi_zone_lookup.csv"


def reload_table(dataframe, table_name, engine):
    inspector = inspect(engine)

    if inspector.has_table(table_name, schema="raw"):
        print(f"Clearing raw.{table_name}...")

        with engine.begin() as connection:
            connection.execute(text(f'TRUNCATE TABLE raw."{table_name}"'))

    print(f"Loading raw.{table_name}...")

    dataframe.to_sql(
        name=table_name,
        con=engine,
        schema="raw",
        if_exists="append",
        index=False,
        chunksize=10_000,
    )


def reload_trip_month(dataframe, table_name, engine, data_month):
    inspector = inspect(engine)

    if inspector.has_table(table_name, schema="raw"):
        print(f"Removing existing {data_month} data...")
        with engine.begin() as connection:
            connection.execute(
                text(f'DELETE FROM raw."{table_name}" WHERE source_month = :data_month'),
                {"data_month": data_month},
            )

    print(f"Loading {data_month} into raw.{table_name}...")

    dataframe.to_sql(
        name=table_name,
        con=engine,
        schema="raw",
        if_exists="append",
        index=False,
        chunksize=10_000,
    )


def main():
    load_dotenv()

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    database = os.getenv("POSTGRES_DB")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")

    database_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

    engine = create_engine(database_url)

    print("Reading taxi zones...")
    zones = pd.read_csv(ZONES_FILE, keep_default_na=False)

    print("Loading taxi zones into PostgreSQL...")
    reload_table(zones, "taxi_zones", engine)
    # zones.to_sql(
    #     name="taxi_zones",
    #     con=engine,
    #     schema="raw",
    #     if_exists="replace",
    #     index=False,
    # )

    print("Reading yellow taxi trips...")
    trips = pd.read_parquet(TRIPS_FILE)

    trips["source_month"] = DATA_MONTH

    print(f"Trips to load: {len(trips)}")

    print("Loading trips into PostgreSQL...")
    reload_trip_month(
        trips,
        "yellow_taxi_trips",
        engine,
        DATA_MONTH,
    )
    # trips.to_sql(
    #     name="yellow_taxi_trips",
    #     con=engine,
    #     schema="raw",
    #     if_exists="replace",
    #     index=False,
    #     chunksize=10_000,
    # )

    print("Loading completed.")


if __name__ == "__main__":
    main()
