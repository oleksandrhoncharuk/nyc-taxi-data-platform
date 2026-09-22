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
    cbd_congestion_fee,
    source_month

FROM {{ ref('stg_yellow_taxi_trips') }}

WHERE dropoff_datetime >= pickup_datetime
  AND pickup_datetime >= TO_DATE(source_month || '-01', 'YYYY-MM-DD')
  AND pickup_datetime < TO_DATE(source_month || '-01', 'YYYY-MM-DD') + INTERVAL '1 month'
  AND trip_distance <= 1000