-- Genre id by show
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.genre_id >= 1 ORDER BY tv_shows.title, tv_show_genres.genre_id;
