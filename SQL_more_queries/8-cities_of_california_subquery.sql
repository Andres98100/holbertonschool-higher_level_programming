--  lists all the cities of California
SELECT * FROM hbtn_0d_usa.cities WhERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY id ASC;
