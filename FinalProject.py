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

    def enroll_course(self, course):
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


    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        sum=0
        if self.courses_list:
            for course in self.courses_list:
                sum += course.course_mark
            return sum / len(self.courses_list)
        else:
            print("No courses enrolled.")
            return 0

# in Global Scope
# TODO 8 declare empty students list


students_list = []

while True:

    # TODO 9 handle Exception for selection input

    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit\n"))
        if selection == 1:

            # TODO 10 make sure that Student number is not exists before
            student_number = input("Enter Student Number : ")
            for student in students_list:
                if student.student_number == student_number :
                    print("Student with the same number already exists.")
            else:
                student_name = input("Enter Student Name : ")
                while True:
                    try:
                        student_age = int(input("Enter Student Age : "))
                        break
                    except:
                        print("Invalid Value")

            # TODO 11 create student object and append it to students list
            new_student = Student(student_name, student_age, student_number)
            students_list.append(new_student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number : ")
            # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
            for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Exist")
        elif selection == 3:
            student_number = input("Enter Student Number : ")
            # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
            for student in students_list:
                if student.student_number == student_number:
                    student_details = student.get_student_details()
                    print("Student Details:")
                    for key, value in student_details.items():
                        print(f"{key}: {value}")
                break
            else:
                print("Student Not Exist")
        elif selection == 4:
            student_number = input("Enter Student Number")
            # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
            for student in students_list:
                if student.student_number == student_number:
                    print(f'avareg : {student.get_student_average()}\n')
            else:
                print("Student Not Exist")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

