-- Join cities and states tables to display all cities contained in database passed into mysql command
SELECT cities.id, cities.name, states.name 
FROM cities 
	JOIN states ON (cities.state_id = states.id)
ORDER BY cities.id ASC;
