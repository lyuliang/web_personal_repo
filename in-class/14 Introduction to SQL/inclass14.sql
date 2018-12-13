-- 1. Insert two new students into the database.
INSERT INTO sio_student (andrew_id, first_name, last_name) VALUES ('LYULIANL', 'LYULIANG', 'LIU');
INSERT INTO sio_student (andrew_id, first_name, last_name) VALUES ('XIAOMINW', 'XIAOMING', 'WANG');
-- 2. Get all student information for all students.
SELECT * FROM STUDENT 
-- 3. Get the course names (and just the course names) for all courses.
SELECT COURSE_NAME FROM COURSE 
-- 4. Get all students with the last name Lee.
SELECT * FROM STUDENT WHERE LAST_NAME = 'LEE'
-- 5. Order the results of the previous query by the students’ first names.
SELECT * FROM STUDENT WHERE LAST_NAME = 'LEE' ORDERBY FIRST_NAME
-- 6. Get all students whose first name contains ha.
SELECT * FROM STUDENT WHERE FIRST_NAME LIKE '%HA%'
-- 7. Get the number of students whose first name contains ha.
SELECT COUNT(*) FROM STUDENT WHERE FIRST_NAME LIKE '%HA%'
-- 8. Get the number of students in each course. (This is a single query.)
SELECT COUNT(STUDENT) FROM COURSE GROUPBY COURSE_NAME 