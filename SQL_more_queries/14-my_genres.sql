-- Script that imports the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)

SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;