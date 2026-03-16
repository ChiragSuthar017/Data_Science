CREATE DATABASE school;
USE school;

CREATE TABLE classes(
class_id INT PRIMARY KEY AUTO_INCREMENT,
class_name VARCHAR(30) NOT NULL);

CREATE TABLE students(
std_id INT AUTO_INCREMENT PRIMARY KEY,
std_name VARCHAR(30) NOT NULL,
class_id INT,
FOREIGN KEY(class_id) REFERENCES classes(class_id) 
ON UPDATE CASCADE  ON DELETE SET NULL);

-- ON UPDATE CASCADE : if class id is change, it will update automaticallt in the student table.
-- ON DELETE SET NULL : if class id is delete, the related student will have class is set to null.

-- insert into classes 
INSERT INTO classes(class_name) VALUES ('Math') , ('Science') , ('History');

-- insert into students
INSERT INTO students(std_name , class_id) VALUES
('Alice' , 1),
('Bob',2),
('Charlie',1);

SELECT * FROM classes;
SELECT * FROM students;

UPDATE classes SET class_id = 101 Where class_id = 1;
UPDATE classes SET class_id = 102 Where class_id = 2;
UPDATE classes SET class_id = 103 Where class_id = 3;

DELETE FROM classes WHERE class_id = 102;

SELECT * FROM students;
SELECT * FROM classes;