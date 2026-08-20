SELECT *
FROM {{ ref('int_yellow_taxi_trips') }}
WHERE trip_distance < 0