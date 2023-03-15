-- lists all shows contained in the database and show null
SELECT sht.title, shg.genre_id
FROM tv_shows AS sht
LEFT JOIN tv_show_genres AS shg
    ON sht.id = shg.show_id
ORDER BY sht.title, shg.genre_id;
