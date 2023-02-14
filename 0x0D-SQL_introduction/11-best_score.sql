-- Select customize best score row of hbtn_0c_0.second_table
SELECT `score`, `name`
FROM `second_table`
WHERE `score`>=10
ORDER BY `score` DESC;
