-- Create unique_id table on database passed to mysql command
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT '1' UNIQUE,
	name VARCHAR(256));
