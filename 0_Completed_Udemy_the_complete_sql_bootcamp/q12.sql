SELECT * FROM neco
FULL OUTER JOIN neco2
ON neco.name = neco2.name
WHERE neco.id is null
OR neco2.id is null