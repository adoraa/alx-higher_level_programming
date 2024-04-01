-- Select genre and count of shows linked to each genre
SELECT tv_show_genres.genre AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_show_genres ON tv_show_genres.id = tv_show_genres.id
GROUP BY tv_show_genres.name
ORDER BY number_of_shows DESC;
