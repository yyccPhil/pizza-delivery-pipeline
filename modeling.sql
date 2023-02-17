CREAT VIEW best_sell AS
-- Prices most
SELECT o.type AS type
	, sum(o.retail_price) AS total_income
	, c.state AS state
FROM order o
LEFT JOIN customer c USING (customer_id)
GROUP BY o.type, c.state
ORDER BY total_income DESC

-- Qty most

-- SELECT o.type AS type
-- 	, sum(o.qty) AS total_qty
-- 	, c.state AS state
-- FROM order o
-- LEFT JOIN customer c USING (customer_id)
-- GROUP BY o.type, c.state
-- ORDER BY total_qty DESC





SELECT sum(o.qty) AS total_qty
JOIN (
	SELECT type
	FROM best_sell
	WHERE state = {}
	LIMIT 3
) top_3 using (type)
FROM order o
WHERE o.order_date > now() - INTERVAL 12 month
GROUP BY type

SELECT sum(o.retail_price) AS total_retail
JOIN (
	SELECT type
	FROM best_sell
	WHERE state = {}
	LIMIT 3
) top_3 using (type)
FROM order o
WHERE o.order_date > now() - INTERVAL 12 month
GROUP BY type


SELECT sum(o.retail_price) / count(DISTINCT customer_id) AS per_retail
JOIN (
	SELECT type
	FROM best_sell
	WHERE state = {}
	LIMIT 3
) top_3 using (type)
FROM order o
WHERE o.order_date > now() - INTERVAL 12 month
GROUP BY type


SELECT count(DISTINCT customer_id) AS total_cus
JOIN (
	SELECT type
	FROM best_sell
	WHERE state = {}
	LIMIT 3
) top_3 using (type)
FROM order o
WHERE o.order_date > now() - INTERVAL 12 month
GROUP BY type



