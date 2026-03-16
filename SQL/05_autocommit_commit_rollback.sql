USE chirag;

-- sql run by default autocommit mode
-- disable autocommit 
SET autocommit = 0;

-- the commit statement is used to permanemtly save all changes
START TRANSACTION;

UPDATE students SET age = age + 1 WHERE id = 3;

COMMIT;
SELECT * FROM students;

-- rollback
-- the rollback is used to undo changes

START TRANSACTION;

UPDATE students SET age  = age - 1 WHERE id = 3;

ROLLBACK;
SELECT * FROM students;

-- disable autocommit 
set autocommit = 1;