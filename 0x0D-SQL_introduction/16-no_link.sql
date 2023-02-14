-- Select all records with name in descending order of hbtn_0c_0.second_table
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
