SELECT * FROM neco
LEFT OUTER JOIN neco2
ON neco.name = neco2.name
WHERE neco2.id is null