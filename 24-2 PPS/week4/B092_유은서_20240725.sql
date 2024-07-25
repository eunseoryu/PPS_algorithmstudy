SELECT *
FROM Cinema AS C
WHERE C.id % 2 = 1 AND C.description NOT LIKE '%boring%'
ORDER BY C.rating DESC;
