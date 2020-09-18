<!-- BASIC SELECT STATEMENT -->

SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees

SELECT * FROM employees WHERE department_id = 7

SELECT * FROM employees ORDER BY first_name DESC

SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary ASC

SELECT sum(salary) FROM employees

SELECT min(salary), max(salary) FROM employees

SELECT avg(salary), count(employee_id) FROM employees

SELECT UPPER(first_name) FROM employees

SELECT substring(first_name, 1,3) FROM employees

SELECT sum(171*214+625)

SELECT first_name, last_name FROM employees

SELECT first_name, last_name, (SELECT length(CONCAT(first_name, last_name))) FROM employees

SELECT * FROM employees WHERE first_name LIKE '%[0-9]%'

SELECT * FROM employees limit 10

SELECT ROUND(salary/12) FROM employees

<!-- CREATES TABLES -->

CREATE TABLE countries (
	id SERIAL PRIMARY KEY,
	country_name VARCHAR (100),
	region_id VARCHAR (100)
);

ERROR - table already exists

CREATE TABLE dup_countries(
	id SERIAL PRIMARY KEY,
	country_name VARCHAR (100),
	region_id VARCHAR (100)
);

<!-- 9 (jobs) -->

CREATE TABLE jobs(
	job_id SERIAL PRIMARY KEY,
	job_title VARCHAR (50) DEFAULT '',
	min_salary INT DEFAULT 8000,
	max_salary INT DEFAULT NULL
);

