SELECT facid, COUNT(*) AS total
FROM cd.bookings
GROUP BY facid HAVING COUNT(*) > 1000
ORDER BY facid 