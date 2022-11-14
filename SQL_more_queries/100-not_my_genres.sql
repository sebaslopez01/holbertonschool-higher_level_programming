-- Not my genre
SELECT DISTINCT tv_genres.name FROM tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE show_id != ( SELECT id FROM tv_shows WHERE title = 'Dexter') ORDER BY tv_genres.name;
