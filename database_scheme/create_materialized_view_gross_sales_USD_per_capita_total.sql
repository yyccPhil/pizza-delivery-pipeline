-- DROP MATERIALIZED VIEW `torqata-yuan-pizza-delivery.pizza_delivery.gross_sales_USD_per_capita_total`;

CREATE MATERIALIZED VIEW `torqata-yuan-pizza-delivery.pizza_delivery.gross_sales_USD_per_capita_total`
AS
SELECT state, type, (gross_sales_USD / population) AS gross_sales_USD_per_capita
FROM `torqata-yuan-pizza-delivery.pizza_delivery.agg_orders_by_type_state` a
INNER JOIN `torqata-yuan-pizza-delivery.pizza_delivery.state_population` sp ON (a.state = sp.name);