SELECT *
FROM departments

SELECT department_id as id
FROM departments

SELECT employee_id as id
FROM employees

SELECT *
FROM regions

SELECT *
FROM employees

SELECT 
first_name,
last_name,
email
FROM employees
WHERE region_id= 3

SELECT 
	DISTINCT(department) as "Unique Departments"
FROM employees

SELECT 
	gender,
	COUNT(gender) as "No. of Employees"
FROM employees
WHERE salary>10000
GROUP BY gender




