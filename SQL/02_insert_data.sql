-- USE chirag;
-- SELECT * FROM students;

-- Insert values into table

-- First method 
INSERT INTO students (name, age, grade, dob) VALUES ('Ayesha Khan', 16, '10th', '2007-05-15');

-- Second method
INSERT INTO students (name, age, grade) VALUES
('Ravi Sharma', 17, '11th'),
('Meena Joshi', 15, '9th'),
('Arjun Verma', 18, '12th'),
('Sara Ali', 16, '10th'),
('Karan Mehta', 17, '11th'),
('Tanya Roy', 15, '9th'),
('Vikram Singh', 18, '12th'),
('Anjali Desai', 16, '10th'),
('Farhan Zaidi', 17, '11th');

SELECT * FROM students; 