import function 

# lists
assignments = []
courses = []
students = []
trainers = []
students_per_course = []
trainers_per_course = []
assignments_per_course = []
assignments_per_student_per_course = []


function.data(students, trainers, assignments, courses, students_per_course, trainers_per_course, assignments_per_course, assignments_per_student_per_course)

# menu
def menu():
    print("WELCOME TO PRIVATE SCHOOL")

menu()

user_input = 0

while True :
    try:
        print("1.Students")
        print("2.Trainers")
        print("3.Assignments")
        print("4.Courses")
        print("5.Exit")
        user_input = int(input("Pick a Choice : "))
        if user_input == 1 :
            print("MENU \n1 Add Student \n2 Students List \n3 Add Student per Course \n4 Students per Course List \n5 Return to Main Menu \n Pick a choice: ")
            user_input = int(input())
            if user_input == 1:
                loop_student = 1
                while (loop_student == 1):
                    function.create_student(students)
                    print("\n1 Add New Student \n2 Main Menu \n Pick a choice: ")
                    loop_student = int(input())
                print(menu)
            elif user_input == 2:
                function.show_list(students)
                print(menu)
            elif user_input == 3:
                loop_students_per_course = 1
                while(loop_students_per_course == 1):
                    function.create_studentpercourse(students_per_course, students, courses)
                    print("\n1 Add New Student per Course \n2 Main Menu \n Pick a choice: ")
                    loop_students_per_course = int(input())
                print(menu)
            elif user_input == 4:
                function.show_studentspercourse(students_per_course, students , courses)
                print(menu)
            elif user_input == 5:
                print(menu)
        elif user_input == 2:
            print("MENU \n1 Add Trainer \n2 Trainers List \n3 Add Trainer per Course \n4 Trainers per Course List \n5 Return to Main Menu \n Pick a choice: ")
            user_input = int(input())
            if user_input == 1:
                loop_trainer = 1
                while (loop_trainer == 1):
                    function.create_trainer(trainers)
                    print("\n1 Add New Trainer \n2 Main Menu \n Pick a choice: ")
                    loop_student = int(input())
                print(menu)
            elif user_input == 2:
                function.show_list(trainers)
                print(menu)
            elif user_input == 3:
                loop_trainer_per_course = 1
                while(loop_trainer_per_course == 1):
                    function.create_trainerpercourse(trainers_per_course, trainers, courses)
                    print("\n1 Add New Trainer per Course \n2 Main Menu \n Pick a choice: ")
                    loop_trainer_per_course = int(input())
                print(menu)
            elif user_input == 4:
                function.show_trainerspercourse(trainers_per_course, trainers, courses)
                print(menu)
            elif user_input == 5:
                print(menu)
        elif user_input == 3:
            print("MENU \n1 Add Assignment \n2 Assignments List \n3 Add Assignment per Course \n4 Assignments per Course List \n5 Add Assignment_per_student_per_course \n6 Assignment_per_student_per_course list \n7 Return to Main Menu \n Pick a choice: ")
            user_input = int(input())
            if user_input == 1:
                loop_assignment = 1
                while (loop_assignment == 1):
                    function.create_assignment(assignments)
                    print("\n1 Add New Assignment \n2 Main Menu \n Pick a choice:  ")
                    loop_assignment = int(input())
                print(menu)
            elif user_input == 2:
                function.show_list(assignments)
                print(menu)
            elif user_input == 3:
                loop_assignment_per_course = 1
                while(loop_assignment_per_course == 1):
                    function.create_assignmentpercourse(assignments_per_course, assignments, courses)
                    print("\n1 Add New Assignment per Course \n2 Main Menu \n Pick a choice: ")
                    loop_assignment_per_course = int(input())
                print(menu)
            elif user_input == 4:
                function.show_assignmentspercourse(assignments_per_course, assignments, courses)
                print(menu)
            elif user_input == 5:
                loop_assignment_per_student_per_course = 1
                while(loop_assignment_per_student_per_course  == 1):
                    function.create_assignmentperstudentpercourse(assignments_per_student_per_course, assignments, students, courses)
                    print("\n1 Add New Assignment per Student per Course \n2 Main Menu \n Pick a choice: ")
                    loop_assignment_per_student_per_course = int(input())
                print(menu)
            elif user_input == 6:
                function.show_assignmentsperstudentpercourse(assignments_per_student_per_course, assignments , students, courses)
                print(menu)
            elif user_input == 7:
                print(menu)
        elif user_input == 4:
            print("MENU \n1 Add Course \n2 Courses List \n3 Return to Main Menu \n Pick a choice: ")
            user_input = int(input())
            if user_input == 1:
                loop_course = 1
                while (loop_course == 1):
                    function.create_course(courses)
                    print("\n1 Add New Course \n2 Main Menu \n Pick a choice: ")
                    loop_course = int(input())
                print(menu)
            elif user_input == 2:
                function.show_list(courses)
                print(menu)
            elif user_input == 3:
                print(menu)
        elif user_input == 5:
            break
        else:
            print("Wrong input, try again")
    except ValueError:
        print("No valid integer! Please try again")
        print(menu)




    
        

    





