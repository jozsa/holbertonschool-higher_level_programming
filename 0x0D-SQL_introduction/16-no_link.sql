-- List all records with name from second_table from database passed to mysql command
SELECT score, name FROM second_table
	WHERE name IS NOT NULL	
	GROUP BY score, name
	ORDER BY score DESC;
