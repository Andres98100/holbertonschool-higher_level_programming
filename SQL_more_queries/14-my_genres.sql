-- lists all genres of the show Dexter
SELECT tg.name
FROM tv_genres AS tg
JOIN tv_show_genres AS thg
    ON thg.genre_id = tg.id
JOIN tv_shows AS ts
    ON ts.id = thg.show_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name;
