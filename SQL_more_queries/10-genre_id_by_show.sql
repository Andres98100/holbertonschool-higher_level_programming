-- lists all shows contained in a database
SELECT sht.title, shg.genre_id
FROM tv_shows AS sht
JOIN tv_show_genres AS shg
    ON sht.id = shg.show_id
ORDER BY sht.title, shg.genre_id;
