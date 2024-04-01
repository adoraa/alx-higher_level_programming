-- List shows by their rating sum
SELECT title, SUM(rate) AS rating_sum
FROM tv_shows
INNER JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY title
ORDER BY rating_sum DESC;
