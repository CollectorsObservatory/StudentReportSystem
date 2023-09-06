import random
import datetime
import re

now = datetime.datetime.now()  # to display date and time
time = now.strftime("%Y-%M-%d %H:%M%S")

name_pattern = r"^[A-Za-z]+$"  # to enter a correct student name , followed by this function


def is_valid_name(name):
    return bool(re.match(name_pattern, name))


student_list = []  # to store the name for students to access them when needed
student_codes = {}  # a dic that takes the name of the student and appoints the followingcode
student_grades = {}
student_subject = {}
student_subject_list = list(student_subject.values())

print("          Welcome to the Student Report System by *CollectorsObservatory*    ")
print(f"              *You logged in at {time}*               ")


class Student:
    """A class that defines the basic information for a student"""

    def __init__(self, name, familyname, grade, code):
        self.name = name
        self.familyname = familyname
        self.grade = grade
        self.code = random.randint(100000000, 999999999)
        self.fullname = name + " " + familyname

    def studentinfo(self):
        """Function will be used later in the options of the student grader, same for functions below"""
        return f"{self.fullname} ID: {self.code} has the following grade {self.grade}%"

    def studentcode(self):
        return f"{self.fullname} has the following unique student identifier {self.code}"


class Subject:
    """A class that completes the student grader program by allowing more features"""
    def __init__(self, subject_name, credit=3):
        self.subject_name = subject_name
        self.credit = credit
        self.subject_code = subject_name[0:3]
        self.enrolled_students = []

    def add_student(self, student):
        """to add student name's and IDS to the subject"""
        self.enrolled_students.append(student)
        return " "

    def generate_report(self):
        """Generates a report containing useful information"""
        report = f"Subject: {self.subject_name}\nCredits: {self.credit}\nSubject Code: {self.subject_code}" \
                 f"-{random.randint(1000, 9999)}\n"
        report += "Enrolled Students:\n"
        for student in self.enrolled_students:
            report += f"{student.fullname}: {student.grade}%\n"
        return report

    def __str__(self):
        """Custom str display for subject object"""
        return f"{self.subject_code}-{random.randint(1000, 9999)}"


print("                 *Type option for more actions*     ")  # used to simpfly user input and to add students easier
print(" ")
subject_input = str(input("Please choose a subject from the following \n"  # it only goes one subject at a time
                          "-Math -Python -Java -English: "))
# leaving room for data base integration for different subjects
# note that subject codes change with each entry because they are random , just for aesthetics
subject_list = ["math", "python", "java", "english"]
if subject_input.lower() in subject_list:
    subject_input = Subject(subject_name=subject_input)
else:
    print(f"{subject_input} not in the list, type the subject again")

while True:
        name = str(input("Please Enter student name : "))
        if name != "option" and is_valid_name(name):  # to keep adding students until the user changes the option
            family_name = str(input(f"Please enter {name}'s family name: "))
            if is_valid_name(family_name):
                grade = float(input(f"Please Enter {name}'s grade: "))
                if 0 < grade <= 100:
                    new_student = Student(name=name, familyname=family_name, grade=grade,
                                          code=random.randint(100000000, 999999999))
                    student_subject_list.append(subject_input)
                    student_list.append(new_student)
                    student_codes.update({new_student.code: new_student.fullname})
                    student_grades.update({new_student.fullname: new_student.grade})
                    student_subject.update({new_student.fullname: subject_input.subject_name})
                    subject_input.add_student(new_student)
                    print(f"{new_student.studentinfo()} at {subject_input}")

                    print(student_codes)
                else:
                    print("Grades should go from 0 to 100, enter the student name and try again")

        elif name == "option":  # Displays all the options, no option to change the subject for now
            print("Please choose an action:")
            print(" ")
            print("1- Display student's information")
            print(" ")
            print("2- Display students' secret code")
            print(" ")
            print("3- Display Student info(Enter unique ID)")
            print(" ")
            print("4- Display Subject report")
            print(" ")
            print("5- Exit Program")
            print(" ")

            choice = int(input("Choose the option: "))

            if choice == 1:
                for student in student_list:
                    print(student.studentinfo())

            elif choice == 2:
                for student in student_list:
                    print(student.studentcode())
                    break

            elif choice == 3:
                student_code = int(input("Enter student secret code: "))
                student_name = student_codes.get(student_code)
                student_grade = student_grades[student_name]
                print(f"the student name is {student_name} and it has the following grade {student_grade}%")
                break

            elif choice == 4:  # it will generate the report for the first subject chosen automatically
                print(subject_input.generate_report())

            elif choice == 5:
                print("Exiting School grader ...")
                break



