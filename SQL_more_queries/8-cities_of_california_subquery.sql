--  lists all the cities of California
SELECT * FROM hbtn_0d_usa.cities WERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY id ASC;
