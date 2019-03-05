-- Create database hbtn_0d_usa and table states if they don't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
