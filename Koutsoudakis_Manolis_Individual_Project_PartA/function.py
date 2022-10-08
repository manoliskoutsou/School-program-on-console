from courses import Course
from assignments import Assignment
from students import Student
from trainers import Trainer
from studentspercourse import StudentPerCourse
from trainerspercourse import TrainerPerCourse
from assignmentspercourse import AssignmentPerCourse
from assignmentsperstudentpercourse import AssignmentPerStudentPerCourse
import datetime

# lists

assignments = []
courses = []
students = []
trainers = []
students_per_course = []
trainers_per_course = []
assignments_per_course = []
assignment_per_student_per_course = []


def show_list(list):
    for item in list:
        print(item)

def show_list_with_id(list):
    for item in list:
        print(f"{item.id}: {item}")


# menu options
def create_course(courses):
    try:
        print("Title: ")
        title = str(input())
        print("Stream: ")
        stream = str(input())
        print("1 - Full Time \n2 - Part Time")
        type = int(input())
        if type == 1:
            type = "full_time"
        elif type == 2:
            type = "part_time"
        print("Start Date: ")
        start_date = int(input())
        print("End Date: ")
        end_date = int(input())
        course = Course(title, stream, type, start_date, end_date)
        courses.append(course)
    except:
        print("No valid entry! Please try again")

def create_student(students):
    try:
        print("First Name: ")
        firstName = str(input())
        print("Last Name: ")
        lastName = str(input())
        print("Date of Birthday: ")
        dateOfBirth = datetime.date(int(input("add year of birth: ")),int(input("add month of birth: ")),int(input("add day of birth: ")))
        print("Tuition Fees: ")
        tuitionFees = int(input())
        student = Student(firstName, lastName, dateOfBirth, tuitionFees)
        students.append(student)
    except:
        print("No valid entry! Please try again")


def create_trainer(trainers):
    try:
        print("First Name: ")
        firstName = str(input())
        print("Last Name: ")
        lastName = str(input())
        print("Subject: ")
        subject = str(input())
        trainer = Trainer(firstName, lastName, subject)
        trainers.append(trainer)
    except:
        print("No valid entry! Please try again")


def create_assignment(assignments):
    try:
        print("Title: ")
        title = str(input())
        print("Description: ")
        description = str(input())
        print("Sub Date Time: ")
        subDateTime = datetime.date(int(input("add year: ")),int(input("add month: ")),int(input("add day: ")))
        print("Oral Mark: ")
        oralMark = int(input())
        print("Total Mark: ")
        totalMark = int(input())
        assignment = Assignment(title, description, subDateTime, oralMark, totalMark)
        assignments.append(assignment)
    except:
        print("No valid entry! Please try again")


def create_studentpercourse(students_per_course, students, courses):
    try:
        show_list_with_id(students)
        print("Please select a student")
        student_id = int(input())
        show_list_with_id(courses)
        print("Please select a course")
        course_id = int(input())
        students_per_course.append(StudentPerCourse(student_id,course_id))
    except:
        print("No valid entry! Please try again")

   
def show_studentspercourse(students_per_course, students , courses):
    print("Students per course")
    print()
    for course in courses:
        print(f"{course} \n students:")
        for student in students:
            for student_per_course in students_per_course:
                if (student.id == student_per_course.student_id and course.id == student_per_course.course_id):
                    print(student)
   

def create_trainerpercourse( trainers_per_course, trainers, courses):
    try:
        show_list_with_id(trainers)
        print("Please select a trainer")
        trainer_id = int(input())
        show_list_with_id(courses)
        print("Please select a course")
        course_id = int(input())
        trainers_per_course.append(TrainerPerCourse(trainer_id,course_id))
    except:
        print("No valid entry! Please try again")
   
  
def show_trainerspercourse(trainers_per_course, trainers, courses):
    print("Trainers per course")
    print()
    for course in courses:
        print(f"{course} \n trainers:")
        for trainer in trainers:
            for trainer_per_course in trainers_per_course:
                if (trainer.id == trainer_per_course.trainer_id and course.id == trainer_per_course.course_id):
                    print(trainer)
   


def create_assignmentpercourse( assignments_per_course, assignments, courses):
    try:
        show_list_with_id(assignments)
        print("Please select an assigmnent")
        assignment_id = int(input())
        show_list_with_id(courses)
        print("Please select a course")
        course_id = int(input())
        assignments_per_course.append(AssignmentPerCourse(assignment_id,course_id))
    except:
        print("No valid entry! Please try again")


def show_assignmentspercourse(assignments_per_course, assignments , courses):
    print("Assignments per course")
    print()
    for course in courses:
        print(f"{course} \n assignments:")
        for assignment in assignments:
            for assignment_per_course in assignments_per_course:
                if (assignment.id == assignment_per_course.assignment_id and course.id == assignment_per_course.course_id):
                    print(assignment)



def create_assignmentperstudentpercourse(assignments_per_student_per_course , assignments, students, courses):
    try:
        show_list_with_id(assignments)
        print("Please select an assigmnent")
        assignment_id = int(input())
        show_list_with_id(students)
        print("Please select a Student")
        student_id = int(input())
        show_list_with_id(courses)
        print("Please select a course")
        course_id = int(input())
        assignments_per_student_per_course.append(AssignmentPerStudentPerCourse(assignment_id, student_id, course_id))
    except:
        print("No valid entry! Please try again")


def show_assignmentsperstudentpercourse(assignments_per_student_per_course, assignments , students, courses):
    print("Assignments per student per course")
    print()
    for course in courses:
        print(f"{course} \n students:")
        for student in students:
             print(f"{student} \n assignments:")
             for assignment in assignments:
                for assignment_per_student_per_course in assignments_per_student_per_course:
                    if assignment.id == assignment_per_student_per_course.assignment_id and student.id == assignment_per_student_per_course.student_id and course.id == assignment_per_student_per_course.course_id:
                        print(assignment)





# dummy data
def data(students, trainers, assignments, courses, students_per_course, trainers_per_course, assignments_per_course, assignments_per_student_per_course):

    student1 = Student( "Manolis", "Koutsoudakis","1985-06-10", "2500")
    student2 = Student( "Stratos", "Kontelos","1985-08-11", "2500")
    student3 = Student( "Bruna", "Doga","1985-07-01", "2500")
    student4 = Student( "Efi", "Likoudi","1985-02-10", "2500")
    student5 = Student( "Olga", "Giftaki","1985-08-01", "2500")

    students.append(student1)
    students.append(student2)
    students.append(student3)
    students.append(student4)
    students.append(student5)

    trainer1 = Trainer("Stefanos", "Papadopoulos", "python")
    trainer2 = Trainer("Ilias", "Mantalos", "java")
    trainer3 = Trainer("Georgia", "Paraskeuopoulou", "c++, java")
    trainer4 = Trainer("Nikolaos", "Kamitsos", "sql")
    trainer5 = Trainer("Antonis", "Karavas", "javascript")

    trainers.append(trainer1)
    trainers.append(trainer2)
    trainers.append(trainer3)
    trainers.append(trainer4)
    trainers.append(trainer5)

    assignment1 = Assignment("Evaluation","Evaluation","2021-10-10", "10","10")
    assignment2 = Assignment("Total Cost","Total Cost","2021-10-10", "8","8")
    assignment3 = Assignment("Total Loss","Total Loss","2021-10-10", "7","7")
    assignment4 = Assignment("Balance","Balance","2021-10-10", "9","9")
    assignment5 = Assignment("Costs","Costs","2021-10-10", "8","8")

    assignments.append(assignment1)
    assignments.append(assignment2)
    assignments.append(assignment3)
    assignments.append(assignment4)
    assignments.append(assignment5)

    course1 = Course("CB 1", "java", "Full Time", "2021-10-10", "2022-10-10")
    course2 = Course("CB 2", "python", "Part Time", "2021-10-10", "2022-10-10")
    course3 = Course("CB 3", "c++", "Full Time", "2021-10-10", "2022-10-10")
    course4 = Course("CB 4", "sql", "Part Time", "2021-10-10", "2022-10-10")
    course5 = Course("CB 5", "python", "Full Time", "2021-10-10", "2022-10-10")

    courses.append(course1)
    courses.append(course2)
    courses.append(course3)
    courses.append(course4)
    courses.append(course5)


    student_per_course1 = StudentPerCourse(student_id = 1,course_id = 1)
    student_per_course2 = StudentPerCourse(student_id = 0,course_id = 0)
    student_per_course3 = StudentPerCourse(student_id = 1,course_id = 2)
    student_per_course4 = StudentPerCourse(student_id = 2,course_id = 0)
    student_per_course5 = StudentPerCourse(student_id = 3,course_id = 3)

    students_per_course.append(student_per_course1)
    students_per_course.append(student_per_course2)
    students_per_course.append(student_per_course3)
    students_per_course.append(student_per_course4)
    students_per_course.append(student_per_course5)

 
    
    trainer_per_course1 = TrainerPerCourse(trainer_id = 1,course_id = 1)
    trainer_per_course2 = TrainerPerCourse(trainer_id = 2,course_id = 2)
    trainer_per_course3 = TrainerPerCourse(trainer_id = 3,course_id = 4)
    trainer_per_course4 = TrainerPerCourse(trainer_id = 3,course_id = 0)
    trainer_per_course5 = TrainerPerCourse(trainer_id = 4,course_id = 1)
     
    trainers_per_course.append(trainer_per_course1)
    trainers_per_course.append(trainer_per_course2)
    trainers_per_course.append(trainer_per_course3)
    trainers_per_course.append(trainer_per_course4)
    trainers_per_course.append(trainer_per_course5)



    assignment_per_course1 = AssignmentPerCourse(assignment_id = 1,course_id = 0)
    assignment_per_course2 = AssignmentPerCourse(assignment_id = 1,course_id = 2)
    assignment_per_course3 = AssignmentPerCourse(assignment_id = 2,course_id = 3)
    assignment_per_course4 = AssignmentPerCourse(assignment_id = 0,course_id = 4)
    assignment_per_course5 = AssignmentPerCourse(assignment_id = 2,course_id = 1)

    assignments_per_course.append(assignment_per_course1)
    assignments_per_course.append(assignment_per_course2)
    assignments_per_course.append(assignment_per_course3)
    assignments_per_course.append(assignment_per_course4)
    assignments_per_course.append(assignment_per_course5)


    assignment_per_student_per_course1 = AssignmentPerStudentPerCourse(assignment_id =1, student_id = 1, course_id = 3)
    assignment_per_student_per_course2 = AssignmentPerStudentPerCourse(assignment_id =0, student_id = 2, course_id = 1)
    assignment_per_student_per_course3 = AssignmentPerStudentPerCourse(assignment_id =1, student_id = 0, course_id = 4)
    assignment_per_student_per_course4 = AssignmentPerStudentPerCourse(assignment_id =2, student_id = 3, course_id = 0)
    assignment_per_student_per_course5 = AssignmentPerStudentPerCourse(assignment_id =3, student_id = 5, course_id = 5)
    assignment_per_student_per_course6 = AssignmentPerStudentPerCourse(assignment_id =0, student_id = 0, course_id = 0)
    assignment_per_student_per_course7 = AssignmentPerStudentPerCourse(assignment_id =0, student_id = 1, course_id = 3)
    assignment_per_student_per_course8 = AssignmentPerStudentPerCourse(assignment_id =1, student_id = 0, course_id = 1)
    assignment_per_student_per_course9 = AssignmentPerStudentPerCourse(assignment_id =4, student_id = 1, course_id = 2)
    assignment_per_student_per_course10 = AssignmentPerStudentPerCourse(assignment_id =1, student_id = 1, course_id = 5)


    assignments_per_student_per_course.append(assignment_per_student_per_course1)
    assignments_per_student_per_course.append(assignment_per_student_per_course2)
    assignments_per_student_per_course.append(assignment_per_student_per_course3)
    assignments_per_student_per_course.append(assignment_per_student_per_course4)
    assignments_per_student_per_course.append(assignment_per_student_per_course5)
    assignments_per_student_per_course.append(assignment_per_student_per_course6)
    assignments_per_student_per_course.append(assignment_per_student_per_course7)
    assignments_per_student_per_course.append(assignment_per_student_per_course8)
    assignments_per_student_per_course.append(assignment_per_student_per_course9)
    assignments_per_student_per_course.append(assignment_per_student_per_course10)













