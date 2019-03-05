-- List all cities of California found in database passed into mysql command
SELECT id, name 
FROM cities
WHERE state_id =
	(SELECT id 
	 FROM states
	 WHERE name = 'California')
	GROUP BY id, name
	ORDER BY id ASC;
