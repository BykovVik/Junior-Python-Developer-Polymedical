# Junior-Python-Developer-Polymedical

## Ссылка на проект с ER-диаграммой <https://drawsql.app/teams/ponystudio/diagrams/university-management-systems>

### Course Programs: таблица программ курсов.
* id: уникальный идентификатор программы.
* course: идентификатор соответствующего курса.
* description: описание курса.
### Students: таблица студентов.
* id: уникальный идентификатор студента.
* name: имя студента.
* last_name: фамилия студента.
* birthdate: дата рождения студента.
* email: электронная почта студента.
* phone: номер телефона студента.
* group_id: идентификатор группы, в которой учится студент.
### Classrooms: таблица аудиторий.
* id: уникальный идентификатор аудитории.
* classroom_number: номер аудитории.
* building: идентификатор здания, в котором находится аудитория.
### Semesters: таблица семестров.
* id: уникальный идентификатор семестра.
* semester_name: название семестра.
* begin_semester: дата начала семестра.
* end_semester: дата окончания семестра.
* courses: количество курсов в семестре.
### Teachers: таблица преподавателей.
* id: уникальный идентификатор преподавателя.
* name: имя преподавателя.
* last_name: фамилия преподавателя.
* birthdate: дата рождения преподавателя.
* email: электронная почта преподавателя.
* phone: номер телефона преподавателя.
### Courses: таблица курсов.
* id: уникальный идентификатор курса.
* course_name: название курса.
* teacher: идентификатор преподавателя, который ведет этот курс.
### Grades: таблица оценок.
* id: уникальный идентификатор оценки.
* student: идентификатор студента, которому выставлена оценка.
* course: идентификатор курса, по которому выставлена оценка.
* grade: числовое значение оценки.
### Exams: таблица экзаменов.
* id: уникальный идентификатор экзамена.
* course: идентификатор курса, на который назначен экзамен.
* date: дата проведения экзамена.
* classrooms: идентификатор аудитории, где будет проводиться экзамен.
### Departments: таблица отделений/факультетов.
* id: уникальный идентификатор отделения/факультета.
* departments_name: название отделения/факультета.
### Schedule: таблица расписания занятий.
* id: уникальный идентификатор записи в расписании.
* group: идентификатор группы, которой назначено занятие.
* day: дата проведения занятия.
* begin_lessons: время начала занятия.
* end_lessons: время окончания занятия.
* classroom: идентификатор аудитории, в которой будет проводиться занятие.
* teacher: идентификатор преподавателя, который будет вести занятие.
### Faculties: таблица факультетов.
* id: уникальный идентификатор факультета.
* faculties_name: название факультета.
* departments: идентификатор отделения/факультета, к которому относится этот факультет.
### Buildings: таблица зданий.
* id: уникальный идентификатор здания
* building_name: название здания.
### Curriculum: таблица учебных планов.
* id: уникальный идентификатор учебного плана.
* specialty_name: название специальности по этому учебному плану.
* year_of_study: год обучения.
* course: идентификатор курса, связанный с этим учебным планом.
### Homeworks: таблица домашних заданий.
* id: уникальный идентификатор домашнего задания.
* course: идентификатор курса, к которому относится это домашнее задание.
* description: описание домашнего задания.
### Groups: таблица групп.
* id: уникальный идентификатор группы.
* group_name: название группы.
* course: идентификатор курса, который изучает эта группа.
* departments_id: идентификатор отделения/факультета, к которому принадлежит эта группа.
