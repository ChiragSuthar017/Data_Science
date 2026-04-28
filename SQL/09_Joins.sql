SELECT * FROM students;
SELECT * FROM marks;

-- INNER JOIN
SELECT students.name, marks.subject, marks.student_id FROM students INNER JOIN marks ON students.id = marks.student_id;

-- LEFT JOIN
SELECT students.name, marks.subject, marks.student_id FROM students LEFT JOIN marks ON students.id = marks.student_id;

-- RIGHT JOIN
SELECT students.name, marks.subject, marks.student_id FROM students RIGHT JOIN marks ON students.id = marks.student_id;

-- CROSS JOIN
SELECT students.name, marks.subject, marks.student_id FROM students CROSS JOIN marks;