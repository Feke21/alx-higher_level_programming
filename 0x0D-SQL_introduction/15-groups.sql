-- lists number of records with the same score in second_table of databasde hbtn_0c_0
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
