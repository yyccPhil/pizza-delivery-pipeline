CREATE OR REPLACE VIEW `artful-turbine-378406.pizza_delivery.gross_sales_USD_per_capita`
AS
SELECT * from (
    SELECT state, type, gross_sales_USD_per_capita
        , rank() over(PARTITION BY state ORDER BY gross_sales_USD_per_capita DESC) AS rnk
    FROM `artful-turbine-378406.pizza_delivery.gross_sales_USD_per_capita_by_type_state`
) t1
WHERE t1.rnk < 4;
