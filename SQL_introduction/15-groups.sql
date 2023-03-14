-- lists the number of records with the same score
SELECT COUNT(score) AS number FROM second_table WHERE score = score ORDER BY score DESC;
