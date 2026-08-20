SELECT 
    *,

    CASE 
        WHEN dropoff_datetime < pickup_datetime
            THEN 'dropoff_before_pickup'

        WHEN pickup_datetime < TIMESTAMP '2026-01-01 00:00:00'
          OR pickup_datetime >= TIMESTAMP '2026-02-01 00:00:00'
            THEN 'outside_expected_month'

        WHEN trip_distance > 1000
            THEN 'extreme_trip_distance'

        ELSE 'unknown'
    END AS rejection_reason

FROM {{ ref('stg_yellow_taxi_trips') }}

WHERE dropoff_datetime < pickup_datetime

    OR pickup_datetime < TIMESTAMP '2026-01-01 00:00:00'
    OR pickup_datetime >= TIMESTAMP '2026-02-01 00:00:00'

    OR trip_distance > 1000
