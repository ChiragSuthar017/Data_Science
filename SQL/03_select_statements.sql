USE chirag;

-- basic select staement
SELECT * FROM students;
-- retrieve specific column
SELECT name, age FROM students;
-- where clause
SELECT * FROM students where age >= 18;
-- null values
SELECT * FROM students where dob IS NULL;
SELECT * FROM students where dob IS NOT NULL;
-- combining conditions
SELECT * FROM students WHERE grade = '10th' AND age >= 16;
SELECT * FROM students WHERE grade = '9th' OR grade = '12th';
-- complex conditions
SELECT * FROM students WHERE (grade = '10th' OR grade = '11th') AND age >= 16;
-- sorting results with order by
-- sort by ascending order
SELECT * FROM students ORDER BY age ASC;
-- sort by descending order
SELECT * FROM students ORDER BY age DESC;
-- limiting results with limit
-- get only 5 row
SELECT * FROM students LIMIT 5;
-- get 5 row starting from 3rd row(offset 2)
SELECT * FROM students LIMIT 2 , 5;
-- using wildcards with like
SELECT * FROM students WHERE name LIKE 'A%';
SELECT * FROM students WHERE name LIKE '_a%';
SELECT * FROM students WHERE name LIKE '%y';