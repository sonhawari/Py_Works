SELECT starttime, name
FROM cd.bookings
JOIN cd.facilities ON   cd.bookings.facid = cd.facilities.facid
WHERE cd.bookings.facid BETWEEN 0 AND 1
ORDER BY cd.bookings.starttime