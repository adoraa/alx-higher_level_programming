-- Retrieves the maximum temperature of each state from the temperatures table
-- in the hbtn_0c_0 database, ordered by state name.
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
