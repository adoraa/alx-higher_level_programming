-- Displays the average temperature (in Fahrenheit)
-- by city ordered by descending temperature.
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
