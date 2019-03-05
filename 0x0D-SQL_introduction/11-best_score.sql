-- List all records with score >= 10 in second_table of database passed as arg to mysql
SELECT score, name FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
