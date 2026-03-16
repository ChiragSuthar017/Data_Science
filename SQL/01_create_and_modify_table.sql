USE chirag;

# Create table
CREATE TABLE student(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(20) NOT NULL DEFAULT 'NO Name',
age INT,
grade VARCHAR(10),
date_of_birth DATE);

SELECT * FROM student;
DESC student;

# MODIFY

# Rename table
RENAME TABLE student TO students;
# Rename coulmn
ALTER TABLE students RENAME COLUMN date_of_birth TO dob;
# Add column
ALTER TABLE students ADD COLUMN  admission_date date;
# Delete column
ALTER TABLE students DROP column admission_date;
# To change the data type or constraints of an existing column
ALTER TABLE students MODIFY COLUMN name varchar(50) default NULL;
# Changing the Order of Columns
ALTER TABLE students MODIFY COLUMN grade VARCHAR(30) AFTER dob;

SELECT * FROM students;