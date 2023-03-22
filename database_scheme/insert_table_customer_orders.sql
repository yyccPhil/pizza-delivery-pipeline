-- CREATE OR REPLACE TABLE `torqata-yuan-pizza-delivery.pizza_delivery.customer_orders`
-- AS
-- SELECT *
-- FROM `torqata-yuan-pizza-delivery.pizza_delivery.orders`
-- LEFT JOIN (
--   SELECT * FROM EXTERNAL_QUERY("torqata-yuan-pizza-delivery.us.mysql-torqata-pizza-delivery", "SELECT * FROM customers;")
-- ) c USING (customer_id);


INSERT INTO `torqata-yuan-pizza-delivery.pizza_delivery.customer_orders` (customer_id, order_id, type, qty, retail_price_USD, order_date, name, address, city, state, zip_code)
  SELECT *
  FROM `torqata-yuan-pizza-delivery.pizza_delivery.orders`
  LEFT JOIN (
    SELECT * FROM EXTERNAL_QUERY("torqata-yuan-pizza-delivery.us.mysql-torqata-pizza-delivery", "SELECT * FROM customers;")
  ) c USING (customer_id)
  WHERE order_date > CURRENT_DATETIME() - INTERVAL 1 day;