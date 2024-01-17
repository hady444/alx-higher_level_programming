-- Write a script that displays the average temperature (Fahrenheit) by city
SELECT city, AVG(value) as avg_temp FROM second_table GROUP BY city ORDER BY avg_temp DESC;
