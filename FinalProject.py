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