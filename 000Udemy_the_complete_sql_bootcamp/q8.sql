SELECT title, COUNT(title) AS copies_at_store1
FROM inventory
INNER JOIN film ON inventory.film_id = film.film_id
WHERE store_id =1
GROUP BY title
ORDER BY title