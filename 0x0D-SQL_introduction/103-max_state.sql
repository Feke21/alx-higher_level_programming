-- display the max temp each state (ordered by state name)
-- display max valueof a column in a table
SELECT `state`, MAX(`value`) 'max_temp' FROM `temperatures` GROUP BY `state` ORDER BY `state` ASC;
