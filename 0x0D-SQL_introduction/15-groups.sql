-- select and count and sum
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;

