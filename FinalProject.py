"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Alaa' Hani Eliwa
Delivery Date :31-8-2023
"""

# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)

import uuid


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    student_count = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.student_count += 1

# TODO 5 define a method to enroll new course to student courses list

    def enroll_course(self, course ):
        self.courses_list.append(course)

# method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        if self.courses_list:
            for course in self.courses_list:
                print(f"Course: {course.course_name}, Mark: {course.course_mark}")
        else:
            print("No courses enrolled.")
