-- Number by Score
SELECT score, COUNT(score) AS 'number' FROM second_table ORDER BY COUNT(score) DESC;
