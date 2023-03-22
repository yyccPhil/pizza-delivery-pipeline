CREATE OR REPLACE VIEW `torqata-yuan-pizza-delivery.pizza_delivery.total_number_of_pizzas_sold`
AS
SELECT * from (
    SELECT state, type, total_number_of_pizzas_sold
        , rank() over(PARTITION BY state ORDER BY total_number_of_pizzas_sold DESC) AS rnk
    FROM `torqata-yuan-pizza-delivery.pizza_delivery.agg_orders_by_type_state`
) t1
WHERE t1.rnk < 4;