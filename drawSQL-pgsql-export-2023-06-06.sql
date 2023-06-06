CREATE TABLE "Course Programs"(
    "id" INTEGER NOT NULL,
    "course" INTEGER NOT NULL,
    "description" TEXT NOT NULL
);
ALTER TABLE
    "Course Programs" ADD PRIMARY KEY("id");
CREATE TABLE "Students"(
    "id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "birthdate" DATE NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255) NOT NULL,
    "group_id" INTEGER NOT NULL
);
ALTER TABLE
    "Students" ADD PRIMARY KEY("id");
CREATE TABLE "Classrooms"(
    "id" INTEGER NOT NULL,
    "classroom_number" INTEGER NOT NULL,
    "building" INTEGER NOT NULL
);
ALTER TABLE
    "Classrooms" ADD PRIMARY KEY("id");
CREATE TABLE "Semesters"(
    "id" INTEGER NOT NULL,
    "semester_name" VARCHAR(255) NOT NULL,
    "begin_semester" DATE NOT NULL,
    "end_semester" BIGINT NOT NULL,
    "courses" INTEGER NOT NULL
);
ALTER TABLE
    "Semesters" ADD PRIMARY KEY("id");
CREATE TABLE "Teachers"(
    "id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "birthdate" DATE NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Teachers" ADD PRIMARY KEY("id");
CREATE TABLE "Courses"(
    "id" INTEGER NOT NULL,
    "course_name" VARCHAR(255) NOT NULL,
    "teacher" INTEGER NOT NULL
);
ALTER TABLE
    "Courses" ADD PRIMARY KEY("id");
CREATE TABLE "Grades"(
    "id" INTEGER NOT NULL,
    "student" INTEGER NOT NULL,
    "course" INTEGER NOT NULL,
    "grade" INTEGER NOT NULL
);
ALTER TABLE
    "Grades" ADD PRIMARY KEY("id");
CREATE TABLE "Exams"(
    "id" INTEGER NOT NULL,
    "course" INTEGER NOT NULL,
    "date" DATE NOT NULL,
    "classrooms" INTEGER NOT NULL
);
ALTER TABLE
    "Exams" ADD PRIMARY KEY("id");
CREATE TABLE "Departments"(
    "id" INTEGER NOT NULL,
    "departments_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Departments" ADD PRIMARY KEY("id");
CREATE TABLE "Schedule"(
    "id" INTEGER NOT NULL,
    "group" INTEGER NOT NULL,
    "day" DATE NOT NULL,
    "begin_lessons" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "end_lessons" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "classroom" INTEGER NOT NULL,
    "teacher" INTEGER NOT NULL
);
ALTER TABLE
    "Schedule" ADD PRIMARY KEY("id");
CREATE TABLE "Faculties"(
    "id" INTEGER NOT NULL,
    "faculties_name" VARCHAR(255) NOT NULL,
    "departments" INTEGER NOT NULL
);
ALTER TABLE
    "Faculties" ADD PRIMARY KEY("id");
CREATE TABLE "Buildings"(
    "id" INTEGER NOT NULL,
    "building_name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Buildings" ADD PRIMARY KEY("id");
CREATE TABLE "Curriculum"(
    "id" BIGINT NOT NULL,
    "specialty_name" VARCHAR(255) NOT NULL,
    "year_of_study" DATE NOT NULL,
    "course" INTEGER NOT NULL
);
ALTER TABLE
    "Curriculum" ADD PRIMARY KEY("id");
CREATE TABLE "Homeworks"(
    "id" INTEGER NOT NULL,
    "course" INTEGER NOT NULL,
    "description" TEXT NOT NULL
);
ALTER TABLE
    "Homeworks" ADD PRIMARY KEY("id");
CREATE TABLE "Groups"(
    "id" INTEGER NOT NULL,
    "group_name" VARCHAR(255) NOT NULL,
    "course" INTEGER NOT NULL,
    "departments_id" INTEGER NOT NULL
);
ALTER TABLE
    "Groups" ADD PRIMARY KEY("id");
ALTER TABLE
    "Grades" ADD CONSTRAINT "grades_student_foreign" FOREIGN KEY("student") REFERENCES "Students"("id");
ALTER TABLE
    "Courses" ADD CONSTRAINT "courses_id_foreign" FOREIGN KEY("id") REFERENCES "Curriculum"("id");
ALTER TABLE
    "Groups" ADD CONSTRAINT "groups_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE
    "Faculties" ADD CONSTRAINT "faculties_departments_foreign" FOREIGN KEY("departments") REFERENCES "Departments"("id");
ALTER TABLE
    "Schedule" ADD CONSTRAINT "schedule_teacher_foreign" FOREIGN KEY("teacher") REFERENCES "Teachers"("id");
ALTER TABLE
    "Students" ADD CONSTRAINT "students_group_id_foreign" FOREIGN KEY("group_id") REFERENCES "Courses"("id");
ALTER TABLE
    "Exams" ADD CONSTRAINT "exams_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE
    "Classrooms" ADD CONSTRAINT "classrooms_building_foreign" FOREIGN KEY("building") REFERENCES "Buildings"("id");
ALTER TABLE
    "Groups" ADD CONSTRAINT "groups_departments_id_foreign" FOREIGN KEY("departments_id") REFERENCES "Departments"("id");
ALTER TABLE
    "Courses" ADD CONSTRAINT "courses_teacher_foreign" FOREIGN KEY("teacher") REFERENCES "Teachers"("id");
ALTER TABLE
    "Semesters" ADD CONSTRAINT "semesters_courses_foreign" FOREIGN KEY("courses") REFERENCES "Courses"("id");
ALTER TABLE
    "Homeworks" ADD CONSTRAINT "homeworks_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE
    "Schedule" ADD CONSTRAINT "schedule_group_foreign" FOREIGN KEY("group") REFERENCES "Groups"("id");
ALTER TABLE
    "Schedule" ADD CONSTRAINT "schedule_classroom_foreign" FOREIGN KEY("classroom") REFERENCES "Classrooms"("id");
ALTER TABLE
    "Exams" ADD CONSTRAINT "exams_classrooms_foreign" FOREIGN KEY("classrooms") REFERENCES "Classrooms"("id");
ALTER TABLE
    "Grades" ADD CONSTRAINT "grades_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");
ALTER TABLE
    "Course Programs" ADD CONSTRAINT "course programs_course_foreign" FOREIGN KEY("course") REFERENCES "Courses"("id");