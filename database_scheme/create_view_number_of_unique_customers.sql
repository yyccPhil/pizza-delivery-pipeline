CREATE OR REPLACE VIEW `artful-turbine-378406.pizza_delivery.number_of_unique_customers`
AS
SELECT * from (
    SELECT state, type, number_of_unique_customers
        , rank() over(PARTITION BY state ORDER BY number_of_unique_customers DESC) AS rnk
    FROM `artful-turbine-378406.pizza_delivery.number_of_unique_customers_by_type_state`
) t1
WHERE t1.rnk < 4;

