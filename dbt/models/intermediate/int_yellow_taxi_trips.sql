SELECT
    vendor_id,
    pickup_datetime,
    dropoff_datetime,

    pickup_datetime::date AS trip_date,

    EXTRACT(
        EPOCH FROM (dropoff_datetime - pickup_datetime)
    ) / 60.0 AS trip_duration_minutes,

    passenger_count,
    trip_distance,
    rate_code_id,
    store_and_fwd_flag,

    pickup_location_id,
    dropoff_location_id,

    payment_type,

    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge,
    airport_fee,
    cbd_congestion_fee

FROM {{ ref('stg_yellow_taxi_trips') }}

WHERE dropoff_datetime >= pickup_datetime
  AND pickup_datetime >= TIMESTAMP '2026-01-01 00:00:00'
  AND pickup_datetime < TIMESTAMP '2026-02-01 00:00:00'
  AND trip_distance <= 1000