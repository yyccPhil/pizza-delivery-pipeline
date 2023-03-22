CREATE OR REPLACE VIEW `torqata-yuan-pizza-delivery.pizza_delivery.gross_sales_USD_per_capita`
AS
SELECT * from (
    SELECT state, type, gross_sales_USD_per_capita
        , rank() over(PARTITION BY state ORDER BY gross_sales_USD_per_capita DESC) AS rnk
    FROM `torqata-yuan-pizza-delivery.pizza_delivery.gross_sales_USD_per_capita_total`
) t1
WHERE t1.rnk < 4;
