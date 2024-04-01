-- List shows by their rating sum
SELECT title, SUM(rate) AS rating
FROM tv_shows
INNER JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
