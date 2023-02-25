CREATE OR REPLACE VIEW `artful-turbine-378406.pizza_delivery.gross_sales_USD`
AS
SELECT * from (
    SELECT state, type, gross_sales_USD
        , rank() over(PARTITION BY state ORDER BY gross_sales_USD DESC) AS rnk
    FROM `artful-turbine-378406.pizza_delivery.agg_orders_by_type_state`
) t1
WHERE t1.rnk < 4;
