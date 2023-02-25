DROP MATERIALIZED VIEW `artful-turbine-378406.pizza_delivery.agg_orders_by_type_state`;

CREATE OR REPLACE MATERIALIZED VIEW `artful-turbine-378406.pizza_delivery.agg_orders_by_type_state`
AS
SELECT state, type, population
     , total_number_of_pizzas_sold
     , gross_sales_USD
FROM (
    SELECT state, type, population
         , sum(qty) AS total_number_of_pizzas_sold
         , sum(retail_price) AS gross_sales_USD
    FROM `artful-turbine-378406.pizza_delivery.orders_state`
    GROUP BY state, type, population
) t1;
