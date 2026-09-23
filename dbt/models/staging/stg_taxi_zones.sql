SELECT
    "LocationID" AS location_id,
    "Borough" AS borough,
    "Zone" AS zone,
    service_zone
FROM {{ source('raw', 'taxi_zones') }}
