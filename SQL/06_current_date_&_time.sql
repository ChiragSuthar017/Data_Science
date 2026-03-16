USE chirag;

-- get current date
SELECT CURRENT_DATE;
-- get current time
SELECT CURRENT_TIME;

-- timestamp and now() both return current date and time

SELECT CURRENT_TIMESTAMP;
SELECT NOW();

-- return local date and time of the mysql server
SELECT LOCALTIME;
SELECT LOCALTIMESTAMP; 

-- insert current time in table

UPDATE students SET dob = current_date() WHERE id = 2;
SELECT * FROM students;