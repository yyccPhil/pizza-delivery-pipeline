CREATE TABLE detailed_order AS

SELECT customer_id, state, population, qty, retail_price, order_date
FROM (SELECT o.customer_id, state, qty, retail_price, order_date
      FROM orders o
               LEFT JOIN customers c on o.customer_id = c.customer_id) t1
LEFT JOIN state s on s.name = t1.state;


ALTER TABLE detailed_order ADD detailed_order_id INT NOT NULL
PRIMARY KEY AUTO_INCREMENT FIRST;

# DROP TABLE pizza_types;
