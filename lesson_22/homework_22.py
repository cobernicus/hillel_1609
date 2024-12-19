from pony.orm import Database, Required, Set, db_session, select
import random

# Create the database
db = Database()

# Data models
class Student(db.Entity):
    name = Required(str)
    courses = Set('Course')

class Course(db.Entity):
    name = Required(str)
    students = Set(Student)

# Bind the database to SQLite
db.bind(provider='sqlite', filename=':memory:')
db.generate_mapping(create_tables=True)

# 1. Create courses and students, and assign them randomly to courses
with db_session:
    course_names = ['Math', 'Physics', 'Chemistry', 'Literature', 'Biology']
    courses = {name: Course(name=name) for name in course_names}

    student_names = [f'Student{i}' for i in range(1, 21)]
    for name in student_names:
        student = Student(name=name)
        student.courses.add(random.choice(list(courses.values())))

    # 2. Add a new student and register them for a course within the same transaction
    new_student = Student(name='New Student')
    new_student.courses.add(courses['Math'])

    # Queries within the same transaction
    # Students registered for a specific course
    math_students = select(s for s in Student if 'Math' in s.courses.name)[:]
    print('Students registered for Math:')
    for student in math_students:
        print(student.name)

    # Courses a specific student is registered for
    student_courses = select(c for c in Course if 'New Student' in c.students.name)[:]
    print('Courses for New Student:')
    for course in student_courses:
        print(course.name)

    # 3. Update and delete data within the same transaction
    # Update student data
    student = Student.get(name='New Student')
    student.name = 'Updated Student'

    # Delete student
    student_to_delete = Student.get(name='Updated Student')
    student_to_delete.delete()

    # Verify deletion
    student = Student.get(name='Updated Student')
    print('Student after deletion:', student)  # Should print None since the student is deleted
