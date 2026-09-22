WITH raw_counts AS (
    SELECT
        source_month,
        COUNT(*) AS raw_count
    FROM {{ ref('stg_yellow_taxi_trips') }}
    GROUP BY source_month
),

valid_counts AS (
    SELECT
        source_month,
        COUNT(*) AS valid_count
    FROM {{ ref('fact_trips') }}
    GROUP BY source_month
),

rejected_counts AS (
    SELECT
        source_month,
        COUNT(*) AS rejected_count
    FROM {{ ref('int_rejected_yellow_taxi_trips') }}
    GROUP BY source_month
)

SELECT
    raw.source_month,
    raw.raw_count,
    COALESCE(valid.valid_count, 0) AS valid_count,
    COALESCE(rejected.rejected_count, 0) AS rejected_count

FROM raw_counts AS raw

LEFT JOIN valid_counts AS valid
    ON raw.source_month = valid.source_month

LEFT JOIN rejected_counts AS rejected
    ON raw.source_month = rejected.source_month

WHERE raw.raw_count !=
      COALESCE(valid.valid_count, 0)
      + COALESCE(rejected.rejected_count, 0)