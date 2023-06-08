/*Часть 2: SQL запросы*/

/*Выбрать всех студентов, обучающихся на курсе "Математика".*/
SELECT *
FROM "Students"
INNER JOIN "Courses" ON "Students"."group_id" = "Courses"."id"
WHERE "Courses"."course_name" = 'Математика';
/*Обновить оценку студента по курсу.*/
UPDATE "Grades" SET grade = 5 WHERE student = 1 AND course = 1;
/*Выбрать всех преподавателей, которые преподают в здании №3.*/
SELECT *
FROM "Teachers"
WHERE id IN (
  SELECT DISTINCT teacher
  FROM "Courses"
  WHERE id IN (
    SELECT id
    FROM "Classrooms"
    WHERE building = 3
  )
);
/*Удалить задание для самостоятельной работы, которое было создано более года назад.*/
DELETE FROM "Homeworks" 
WHERE course IN (
    SELECT id FROM "Courses" 
    WHERE id IN (
        SELECT courses FROM "Semesters" 
        WHERE end_semester < NOW() - INTERVAL '1 year'
    )
);
/*Добавить новый семестр в учебный год*/
INSERT INTO "Semesters" (semester_name, begin_semester, end_semester, courses) VALUES ('Осенний семестр 2023', '2023-09-01', '2023-12-31', (SELECT COUNT(*) FROM "Courses"))
