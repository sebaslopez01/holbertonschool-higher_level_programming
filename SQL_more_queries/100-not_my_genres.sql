-- Not my genre
SELECT tv_genres.name FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id NOT IN (SELECT id FROM tv_shows WHERE title = 'Dexter') ORDER BY tv_genres.name;
