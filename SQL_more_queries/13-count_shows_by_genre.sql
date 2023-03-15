-- numerate and displays the number of shows linked to each.
SELECT tg.name AS genre, COUNT(tg.id) AS number_of_shows
FROM tv_genres AS tg
JOIN tv_show_genres AS thg
    ON tg.id = thg.genre_id
GROUP BY tg.id
ORDER BY number_of_shows DESC;
