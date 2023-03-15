-- 
SELECT cities.id, cities.name, states.id
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
