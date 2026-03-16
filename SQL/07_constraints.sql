USE chirag;

-- NOT NULL : column cannot contain null values
-- UNIQUE : all values in column are distict(no duplicates)
-- DEFAULT : sets defaults values for columns if none is provided during insert
-- CHECK CONSTRAINT : validates that values in a column meet a specific conditions

CREATE TABLE user(
id INT NOT NULL,
username VARCHAR(30) UNIQUE,
age INT CHECK (age >= 18),
address VARCHAR(60) DEFAULT 'unknow');

-- NAMING CONSTRAINTS 
-- You can give explicit names to constraints. This makes them easier to reference, especially when altering or dropping them later
CREATE TABLE employee(
id INT PRIMARY KEY,
name VARCHAR(100),
age INT CONSTRAINT low_age CHECK (age >= 18));

INSERT INTO employee VALUES(102, 'chirag', 20);
INSERT INTO employee VALUES(101, 'anshul', 17);
SELECT * FROM employee;