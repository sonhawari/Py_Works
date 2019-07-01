SELECT 
payment_id,
amount,
first_name,
last_name
FROM payment
INNER JOIN staff ON payment.staff_id = staff.staff_id
