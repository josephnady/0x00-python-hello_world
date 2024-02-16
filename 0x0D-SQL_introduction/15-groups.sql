-- select and count and sum
SELECT score, COUNT(DISTINCT (score)) AS 'number'
FROM second_table
GROUP BY score;

