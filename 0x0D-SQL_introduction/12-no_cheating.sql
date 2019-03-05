-- Update Bob's score to 10 in second_table of database passed to mysql command
UPDATE `second_table`
SET
	`score` = '10'
WHERE `second_table`.`name` = 'Bob';
