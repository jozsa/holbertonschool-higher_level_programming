-- List all genres from database passed into mysql command & count of shows in each genre
SELECT name AS genre, count(genre_id) AS number_of_shows 
FROM tv_genres RIGHT JOIN tv_show_genres
	ON (tv_genres.id = tv_show_genres.genre_id)
GROUP BY name
ORDER BY number_of_shows DESC;
