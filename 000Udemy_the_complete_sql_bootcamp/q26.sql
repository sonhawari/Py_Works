SELECT a. customer_id, a.first_name, a.last_name,b.customer_id, b.first_name, b.last_name
FROM customer AS  a, customer AS b
WHERE a.first_name = b.last_name