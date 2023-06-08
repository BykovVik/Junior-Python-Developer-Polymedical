CREATE TABLE "Departments"(
    "id" SERIAL PRIMARY KEY,
    "departments_name" VARCHAR(255) NOT NULL
);

CREATE TABLE "Buildings"(
    "id" SERIAL PRIMARY KEY,
    "building_name" VARCHAR(255) NOT NULL
);

CREATE TABLE "Teachers"(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "birthdate" DATE NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255) NOT NULL
);

CREATE TABLE "Courses"(
    "id" SERIAL PRIMARY KEY,
    "course_name" VARCHAR(255) NOT NULL,
    "teacher" INTEGER NOT NULL REFERENCES "Teachers"("id")
);

CREATE TABLE "Course Programs"(
    "id" SERIAL PRIMARY KEY,
    "course" INTEGER NOT NULL REFERENCES "Courses"("id"),
    "description" TEXT NOT NULL
);

CREATE TABLE "Curriculum"(
    "id" SERIAL PRIMARY KEY,
    "specialty_name" VARCHAR(255) NOT NULL,
    "year_of_study" DATE NOT NULL,
    "course" INTEGER NOT NULL REFERENCES "Courses"("id")
);

CREATE TABLE "Groups"(
    "id" SERIAL PRIMARY KEY,
    "group_name" VARCHAR(255) NOT NULL,
    "course" INTEGER NOT NULL REFERENCES "Courses"("id"),
    "departments_id" INTEGER NOT NULL REFERENCES "Departments"("id")
);

CREATE TABLE "Students"(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "birthdate" DATE NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255) NOT NULL,
    "group_id" INTEGER NOT NULL REFERENCES "Groups"("id")
);

CREATE TABLE "Grades"(
    "id" SERIAL PRIMARY KEY,
    "student" INTEGER NOT NULL REFERENCES "Students"("id"),
    "course" INTEGER NOT NULL REFERENCES "Courses"("id"),
    "grade" INTEGER NOT NULL
);

CREATE TABLE "Classrooms"(
    "id" SERIAL PRIMARY KEY,
    "classroom_number" INTEGER NOT NULL,
    "building" INTEGER NOT NULL REFERENCES "Buildings"("id")
);

CREATE TABLE "Exams"(
    "id" SERIAL PRIMARY KEY,
    "course" INTEGER NOT NULL REFERENCES "Courses"("id"),
    "date" DATE NOT NULL,
    "classrooms" INTEGER NOT NULL REFERENCES "Classrooms"("id")
);

CREATE TABLE "Schedule"(
    "id" SERIAL PRIMARY KEY,
    "group" INTEGER NOT NULL REFERENCES "Groups"("id"),
    "day" DATE NOT NULL,
    "begin_lessons" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "end_lessons" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "classroom" INTEGER NOT NULL REFERENCES "Classrooms"("id"),
    "teacher" INTEGER NOT NULL REFERENCES "Teachers"("id")
);

CREATE TABLE "Faculties"(
    "id" SERIAL PRIMARY KEY,
    "faculties_name" VARCHAR(255) NOT NULL,
    "departments" INTEGER NOT NULL REFERENCES "Departments"("id")
);

CREATE TABLE "Homeworks"(
    "id" SERIAL PRIMARY KEY,
    "course" INTEGER NOT NULL REFERENCES "Courses"("id"),
    "description" TEXT NOT NULL
);

ALTER TABLE "Courses" ADD CONSTRAINT "courses_teacher_foreign" FOREIGN KEY("teacher") REFERENCES "Teachers"("id");
ALTER TABLE "Course Programs" ADD CONSTRAINT "course_programs_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE "Curriculum" ADD CONSTRAINT "curriculum_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE "Grades" ADD CONSTRAINT "grades_student_foreign" FOREIGN KEY("student") REFERENCES "Students"("id");
ALTER TABLE "Grades" ADD CONSTRAINT "grades_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE "Exams" ADD CONSTRAINT "exams_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE "Classrooms" ADD CONSTRAINT "classrooms_building_foreign" FOREIGN KEY("building") REFERENCES "Buildings"("id");
ALTER TABLE "Schedule" ADD CONSTRAINT "schedule_group_foreign" FOREIGN KEY("group") REFERENCES "Groups"("id");
ALTER TABLE "Schedule" ADD CONSTRAINT "schedule_classroom_foreign" FOREIGN KEY("classroom") REFERENCES "Classrooms"("id");
ALTER TABLE "Schedule" ADD CONSTRAINT "schedule_teacher_foreign" FOREIGN KEY("teacher") REFERENCES "Teachers"("id");
ALTER TABLE "Faculties" ADD CONSTRAINT "faculties_departments_foreign" FOREIGN KEY("departments") REFERENCES "Departments"("id");
ALTER TABLE "Groups" ADD CONSTRAINT "groups_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE "Groups" ADD CONSTRAINT "groups_departments_id_foreign" FOREIGN KEY("departments_id") REFERENCES "Departments"("id");