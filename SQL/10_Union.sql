SELECT * FROM students;
SELECT * FROM marks;

SELECT name FROM students 
UNION
SELECT subject FROM marks;

-- By default UNION remove duplicate rows.
-- If you want to kepp duplicate rows, use UNION ALL.

SELECT name FROM students 
UNION
SELECT subject FROM marks;