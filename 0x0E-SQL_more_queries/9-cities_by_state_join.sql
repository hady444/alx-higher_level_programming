-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT id, name, states.name from cities
JOIN states ON state_id = states.id
ORDER BY cities.id;
