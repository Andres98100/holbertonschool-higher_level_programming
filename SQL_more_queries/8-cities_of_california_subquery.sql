--  lists all the cities of California
SELECT id, name FROM cities WhERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
