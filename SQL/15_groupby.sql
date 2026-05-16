-- USE emp;
SELECT * FROM employees;

-- cout employees of departments
SELECT department, count(*) AS total FROM employees GROUP BY department;

SELECT department, address, COUNT(*) AS total_emp , AVG(salary) AS avg FROM employees GROUP BY department, address;

-- sum of total sum salary
SELECT department, sum(salary) AS total_salary FROM employees GROUP BY department WITH ROLLUP;

-- after GROUP BY we can't use WHERE
SELECT department, sum(salary) AS total_salary FROM employees GROUP BY department HAVING sum(salary) > 900000;

-- use both WHERE and HAVING
SELECT first_name, department, address FROM employees WHERE address =  'Delhi'  GROUP BY department, first_name HAVING department = 'HR';
