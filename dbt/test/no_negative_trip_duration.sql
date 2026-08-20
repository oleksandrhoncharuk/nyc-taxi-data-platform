SELECT *
FROM {{ ref('int_yellow_taxi_trips') }}
WHERE trip_duration_minutes < 0