<!-- ONE ON ONE -->

CREATE TABLE branch_name (
	id SERIAL PRIMARY KEY,
	b_name VARCHAR (100),
	dean VARCHAR (100)
);

CREATE TABLE branch_location(
	branch_id int,
	city VARCHAR (100),
	country VARCHAR (100),
	FOREIGN KEY (branch_id) REFERENCES branch_name(id)
);

INSERT INTO branch_name(b_name, dean)
VALUES ('Spring Farm', 'T. Walker'),('View Mount', 'L. Jones'), ('North Lake', 'M. Thomas')

INSERT INTO branch_location(branch_id, city, country)
VALUES (2, 'Rosedale', 'Canada'),(1, 'Vaughan', 'Canada'), (3, 'Fairmount', 'Johannesburg')

SELECT b_name, dean, city, country FROM branch_name
JOIN branch_location ON branch_name.id = branch_location.branch_id;

<!-- ONE ON MANY -->

CREATE TABLE professor(
	id SERIAL PRIMARY KEY,
	l_name VARCHAR (100),
	age int
);

CREATE TABLE lessons (
	id SERIAL PRIMARY KEY,
	p_id int,
	subject VARCHAR (100),
	hour TIME,
	FOREIGN KEY (p_id) REFERENCES professor(id) ON DELETE CASCADE
);

INSERT INTO professor (l_name, age)
VALUES ('Bernardo', '56'), ('Jefferson', '40'), ('Davidson', 70)

INSERT INTO lessons (p_id, subject, hour)
VALUES ('2', 'Maths', '13:00:00'),('2', 'Maths', '13:45:00'),
('2', 'Computer Science', '08:30:00'), ('1', 'English Literature', '12:15:00'),
('3', 'Psychology', '13:00:00'), ('1', 'Journling', '10:30:00')

SELECT p_id, subject, hour, l_name, age FROM professor
JOIN lessons ON professor.id = lessons.p_id

<!-- MANY TO MANY -->

CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	f_name VARCHAR (50),
	l_name VARCHAR (100)
);

CREATE TABLE classes (
	id SERIAL PRIMARY KEY,
	subject VARCHAR (100),
	grade int
);

CREATE TABLE students_classes (
	student_id int,
	class_id int,
	FOREIGN KEY (student_id) REFERENCES students(id),
	FOREIGN KEY (class_id) REFERENCES classes(id)
);


INSERT INTO students (f_name, l_name)
VALUES ('Sarah', 'Sanders'), ('Michael', 'Davis'), ('Betty', 'Barker'), ('Scott', 'Benson')

INSERT INTO classes (subject)
VALUES ('English Literature'), ('Maths'), ('Computer Science'), ('Psychology'),
('Physics'), ('Chemistry'), ('Programing')


INSERT INTO students_classes (student_id, class_id)
VALUES ((SELECT id FROM students WHERE l_name = 'Sanders'), (SELECT id FROM classes WHERE subject = 'English Literature')),
((SELECT id FROM students WHERE l_name = 'Sanders'), (SELECT id FROM classes WHERE subject = 'Maths')),
((SELECT id FROM students WHERE l_name = 'Sanders'), (SELECT id FROM classes WHERE subject = 'Computer Science')),
((SELECT id FROM students WHERE l_name = 'Sanders'), (SELECT id FROM classes WHERE subject = 'Programming')),
((SELECT id FROM students WHERE l_name = 'Benson'), (SELECT id FROM classes WHERE subject = 'English Literature')),
((SELECT id FROM students WHERE l_name = 'Benson'), (SELECT id FROM classes WHERE subject = 'Psychology')),
((SELECT id FROM students WHERE f_name = 'Scott'), (SELECT id FROM classes WHERE subject = 'English Literature')),
((SELECT id FROM students WHERE f_name = 'Scott'), (SELECT id FROM classes WHERE subject = 'Physics')),
((SELECT id FROM students WHERE l_name = 'Barker'), (SELECT id FROM classes WHERE subject = 'Physics')),
((SELECT id FROM students WHERE l_name = 'Barker'), (SELECT id FROM classes WHERE subject = 'Chemistry'))



SELECT f_name, l_name, subject FROM students
JOIN students_classes ON students.id = students_classes.student_id
JOIN classes ON students_classes.class_id = classes.id