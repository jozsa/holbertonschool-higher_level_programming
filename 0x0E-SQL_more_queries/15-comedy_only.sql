-- List all Comedy shows in database passed to mysql command
SELECT title
FROM tv_shows
	JOIN tv_show_genres
		ON (tv_shows.id = tv_show_genres.show_id)
	JOIN tv_genres
		ON (tv_show_genres.genre_id = tv_genres.id)
		AND tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
