--  script that lists the number of records with the same score in the table second_table
SELECT `score`, COUNT(`score`) as number ORDER BY number DESC GROUP BY score;
