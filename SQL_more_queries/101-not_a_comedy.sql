-- No comedy
SELECT DISTINCT tv_shows.title FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_genres.name != 'Comedy' AND genre_id IS NULL ORDER BY tv_shows.title;
