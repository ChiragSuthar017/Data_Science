USE emp;
SELECT * FROM employees;

-- create index for  single columns
CREATE INDEX idxss ON employees(department);

-- create index for multiple columns
CREATE INDEX idx ON employees(department, salary);

-- index
DROP INDEX idxss ON employees;

-- show all index
SHOW INDEX FROM employees;