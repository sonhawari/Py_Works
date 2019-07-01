SELECT title, name movie_language
FROM film
JOIN language lan ON lan.language_id = film.language_id;
