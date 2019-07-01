SELECT rating, AVG(rental_rate)
FROM film
WHERE rating IN ('R','G','PG')
GROUP BY rating
HAVING AVG(rental_rate) <3;