import pandas as pd

TRIPS_FILE = "data/raw/yellow_tripdata_2026-01.parquet"
ZONES_FILE = "data/raw/taxi_zone_lookup.csv"

trips = pd.read_parquet(TRIPS_FILE)
zones = pd.read_csv(ZONES_FILE)

print("=== TRIPS ===")
print(f"Rows: {len(trips)}")
print(f"Columns: {len(trips.columns)}")

print("\nColumn names:")
print(trips.columns.tolist())

print("\nData types:")
print(trips.dtypes)

print("\nFirst 5 rows:")
print(trips.head())

print("\nMissing values:")
print(trips.isna().sum())

print("\nPickup date range:")
print(trips["tpep_pickup_datetime"].min())
print(trips["tpep_pickup_datetime"].max())


print("\n=== ZONES ===")
print(f"Rows: {len(zones)}")
print(f"Columns: {len(zones.columns)}")

print("\nColumn names:")
print(zones.columns.tolist())

print("\nData types:")
print(zones.dtypes)

print("\nFirst 5 rows:")
print(zones.head())
