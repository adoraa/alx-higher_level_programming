-- Retrieves the top 3 cities with the highest average temperature during July and August
-- from the temperatures table in the hbtn_0c_0 database, ordered by temperature in descending order.
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
