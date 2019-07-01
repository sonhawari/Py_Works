SELECT starttime
FROM cd.members
JOIN cd.bookings ON cd.members.memid = cd.bookings.memid
WHERE cd.members.firstname = 'David' AND cd.members.surname = 'Farrell'
ORDER BY starttime ASC