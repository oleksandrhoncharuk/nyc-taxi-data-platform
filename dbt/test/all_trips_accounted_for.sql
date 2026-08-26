SELECT
    staging_count,
    fact_count,
    rejected_count

FROM (
    SELECT
        (SELECT COUNT(*) FROM {{ ref('stg_yellow_taxi_trips') }})
            AS staging_count,

        (SELECT COUNT(*) FROM {{ ref('fact_trips') }})
            AS fact_count,

        (SELECT COUNT(*) FROM {{ ref('int_rejected_yellow_taxi_trips') }})
            AS rejected_count
) counts

WHERE staging_count != fact_count + rejected_count