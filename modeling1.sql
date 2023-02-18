CREATE MATERIALIZED VIEW orders_by_pizza_types AS

SELECT state, type, total_number_of_pizzas_sold, gross_sales_USD, (gross_sales_USD / population) AS gross_sales_USD_per_capita, number_of_unique_customers
FROM (
  SELECT state, type, sum(qty) AS total_number_of_pizzas_sold, sum(retail_price) AS gross_sales_USD, count(DISTINCT customer_id) AS number_of_unique_customers
  FROM orders o
  LEFT JOIN customers c USING (customer_id)
  WHERE o.order_date > now() - INTERVAL 12 month
  GROUP BY state, type
) op
LEFT JOIN state_population s ON s.name = op.state



-- Total number of pizzas sold over the last 12 months for each type
SELECT state, type, total_number_of_pizzas_sold
FROM orders_by_pizza_types
WHERE state = {}
ORDER BY total_number_of_pizzas_sold DESC
LIMIT 3

-- Gross sales over the last 12 months for each type
SELECT state, type, gross_sales_USD
FROM orders_by_pizza_types
WHERE state = {}
ORDER BY total_number_of_pizzas_sold DESC
LIMIT 3

-- Gross sales per capita over the last 12 months for each type
SELECT state, type, gross_sales_USD_per_capita
FROM orders_by_pizza_types
WHERE state = {}
ORDER BY total_number_of_pizzas_sold DESC
LIMIT 3

-- Number of unique customers who ordered the item at least once over the last 12 months for each type
SELECT state, type, number_of_unique_customers
FROM orders_by_pizza_types
WHERE state = {}
ORDER BY total_number_of_pizzas_sold DESC
LIMIT 3
