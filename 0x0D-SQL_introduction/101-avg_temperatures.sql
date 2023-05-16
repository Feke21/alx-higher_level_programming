-- displays the avg temp (Fahrenheit) by city ordered by temp (descending)
-- display average value
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;
