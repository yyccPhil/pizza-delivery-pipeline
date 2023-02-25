CREATE TABLE `artful-turbine-378406.pizza_delivery.orders_state`
AS
SELECT order_id, customer_id, state, population, type, qty, retail_price, order_date
FROM (
    SELECT state, order_id, customer_id, type, qty, retail_price, order_date
    FROM `artful-turbine-378406.pizza_delivery.orders` o
    LEFT JOIN `artful-turbine-378406.pizza_delivery.customers` c USING(customer_id)
    WHERE order_date > CURRENT_DATETIME() - INTERVAL 12 month
) oc
LEFT JOIN `artful-turbine-378406.pizza_delivery.state_population` sp on oc.state = sp.name;

-- DROP TABLE `artful-turbine-378406.pizza_delivery.orders_state`;