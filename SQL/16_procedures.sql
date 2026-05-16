USE emp;
SELECT * FROM employees;

DELIMITER //

CREATE PROCEDURE list_emp()
BEGIN
	SELECT * FROM employees;
    SELECT * FROM employees WHERE department = 'IT';
END //

DELIMITER ;

CALL list_emp(); 

DELIMITER //

-- get employee detail by id
CREATE PROCEDURE list_id_emp(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE id = emp_id;
END //

DELIMITER ;

CALL list_id_emp(2);