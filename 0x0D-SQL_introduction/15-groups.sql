-- List number of records with same score in second_table in database passed to mysql command
SELECT score, count(score) AS number FROM second_table
	GROUP BY score	
	ORDER BY count(score) DESC;
