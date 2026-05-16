USE emp;
SELECT  * FROM employees;

-- CONCATE() function.
SELECT first_name , last_name , CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

-- get current date or time
SELECT NOW();

-- get length of name or other 
SELECT first_name, LENGTH(first_name) AS len FROM employees;


SELECT first_name, ROUND(DATEDIFF(NOW(), join_date)/365,2) AS total_years FROM employees;