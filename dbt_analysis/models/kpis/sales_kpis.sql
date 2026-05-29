{{ config(
    materialized='table',
    location_root='s3a://warehouse/gold'
    ) 
}}

SELECT
    month,
    category,
    SUM(units_sold)  AS total_units_sold,
    SUM(revenue)     AS total_revenue,
    AVG(revenue)     AS avg_revenue
FROM delta.`s3a://spark-data/gold/sales`
GROUP BY
    month,
    category
ORDER BY
    month,
    category