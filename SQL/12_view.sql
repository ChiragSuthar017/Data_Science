USE emp;
SELECT * FROM employees;

-- create view
CREATE VIEW total_year AS SELECT first_name, department, salary, join_date, ROUND(DATEDIFF(NOW(), join_date)/365, 2) AS total_years FROM employees;
SELECT * FROM total_year;

-- update view
CREATE OR REPLACE VIEW total_years AS SELECT first_name, last_name, department, salary, join_date, ROUND(DATEDIFF(NOW(), join_date)/365, 2) AS total_years FROM employees;
SELECT * FROM total_years;

-- delete view  
DROP VIEW total_year;