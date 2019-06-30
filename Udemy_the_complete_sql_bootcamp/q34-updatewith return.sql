UPDATE link
SET description = 'New Desc'
WHERE id = 1
RETURNING id,url,name,description;