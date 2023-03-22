CREATE OR REPLACE TABLE `torqata-yuan-pizza-delivery.pizza_delivery.agg_orders_by_type_state`
AS
SELECT state, type
     , sum(qty) AS total_number_of_pizzas_sold
     , sum(retail_price_USD) AS gross_sales_USD
     , count(DISTINCT customer_id) AS number_of_unique_customers
FROM `torqata-yuan-pizza-delivery.pizza_delivery.customer_orders`
WHERE order_date > CURRENT_DATETIME() - INTERVAL 12 month
GROUP BY state, type;