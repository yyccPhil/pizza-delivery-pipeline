CREATE OR REPLACE VIEW `artful-turbine-378406.pizza_delivery.gross_sales_USD_per_capita_by_type_state`
AS
SELECT state, type
     , (gross_sales_USD / population) AS gross_sales_USD_per_capita
FROM `artful-turbine-378406.pizza_delivery.agg_orders_by_type_state`;
