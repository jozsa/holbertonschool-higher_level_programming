-- Create htbn_0d_usa database and cities table if they don't exist.
-- state_id will be FOREIGN KEY that references to states table id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id)
		REFERENCES states(id)
);
