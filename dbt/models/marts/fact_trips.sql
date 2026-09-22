SELECT
    vendor_id,

    trip_date,
    pickup_datetime,
    dropoff_datetime,
    trip_duration_minutes,

    passenger_count,
    trip_distance,

    pickup_location_id,
    dropoff_location_id,

    rate_code_id,
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

FROM {{ ref('int_yellow_taxi_trips') }}