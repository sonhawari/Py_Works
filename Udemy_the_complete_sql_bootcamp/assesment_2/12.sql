SELECT facid, COUNT(*)
FROM cd.bookings
WHERE starttime >= '2012-09-01'
GROUP BY facid
ORDER BY facid 