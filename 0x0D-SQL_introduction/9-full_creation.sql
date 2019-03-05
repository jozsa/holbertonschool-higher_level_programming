-- Create second_table in database passed in to mysql command
CREATE table IF NOT EXISTS second_table (id INT,
	name VARCHAR(256), score INT);
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES ('1', "John", '10');
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES ('2', "Alex", '3');
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES ('3', "Bob", '14');
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES ('4', "George", '8');
