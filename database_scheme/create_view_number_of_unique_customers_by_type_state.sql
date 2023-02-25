CREATE OR REPLACE VIEW `artful-turbine-378406.pizza_delivery.number_of_unique_customers_by_type_state`
AS
SELECT state, type
     , count(DISTINCT customer_id) AS number_of_unique_customers
FROM `artful-turbine-378406.pizza_delivery.orders_state`
WHERE order_date > CURRENT_DATETIME() - INTERVAL 12 month
GROUP BY state, type;
