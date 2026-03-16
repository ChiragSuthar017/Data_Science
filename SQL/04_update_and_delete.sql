USE chirag;

-- update statement
UPDATE students SET grade = '10' WHERE grade = '10th';
UPDATE students SET age = 17, grade = '10th' where id = 3;
UPDATE students SET name = 'unknown' WHERE name IS NULL;
SELECT * FROM students;

-- Delete statement 
DELETE FROM students WHERE grade IS NUll;
-- remove all data from the table
# DELETE FROM students;
-- completely remove the table 
# DROP TAble students;   