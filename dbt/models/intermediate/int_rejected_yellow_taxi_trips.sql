SELECT
    *,

    CASE
        WHEN dropoff_datetime < pickup_datetime
            THEN 'dropoff_before_pickup'

        WHEN pickup_datetime < TO_DATE(source_month || '-01', 'YYYY-MM-DD')
          OR pickup_datetime >= TO_DATE(source_month || '-01', 'YYYY-MM-DD') + INTERVAL '1 month'
            THEN 'outside_expected_month'

        WHEN trip_distance > 1000
            THEN 'extreme_trip_distance'

        ELSE 'unknown'
    END AS rejection_reason

FROM {{ ref('stg_yellow_taxi_trips') }}

WHERE dropoff_datetime < pickup_datetime

    OR pickup_datetime < TO_DATE(source_month || '-01', 'YYYY-MM-DD')
    OR pickup_datetime >= TO_DATE(source_month || '-01', 'YYYY-MM-DD') + INTERVAL '1 month'

    OR trip_distance > 1000
