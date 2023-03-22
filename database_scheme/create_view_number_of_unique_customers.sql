CREATE OR REPLACE VIEW `torqata-yuan-pizza-delivery.pizza_delivery.number_of_unique_customers`
AS
SELECT * from (
    SELECT state, type, number_of_unique_customers
        , rank() over(PARTITION BY state ORDER BY number_of_unique_customers DESC) AS rnk
    FROM `torqata-yuan-pizza-delivery.pizza_delivery.agg_orders_by_type_state`
) t1
WHERE t1.rnk < 4;