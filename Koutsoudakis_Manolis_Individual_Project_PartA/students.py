import itertools

class Student:
    studentNew_id = itertools.count().__next__
    def __init__(self, firstName, lastName ,dateOfBirth, tuitionFees):
         self.id = Student.studentNew_id()
         self.__firstName = firstName
         self.__lastName = lastName
         self.__dateOfBirth = dateOfBirth
         self.__tuitionFees = tuitionFees
         self.courses = []


    @property
    def firstName(self):
         return self.__firstName
    @firstName.setter 
    def firstName(self, firstName):
         self.__firstName = firstName

    @property
    def lastName(self):
         return self.__lastName
    @lastName.setter 
    def lastName(self, lastName):
         self.__lastName = lastName 

    @property
    def dateOfBirth(self):
         return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth):
         self.__dateOfBirth = dateOfBirth

    @property
    def tuitionFees(self):
         return self.__tuitionFees
    @tuitionFees.setter
    def tuitionFees(self, tuitionFees):
         self.__tuitionFees = tuitionFees

    def __repr__ (self):
        return f"{self.firstName} {self.lastName}, with date of birth {self.dateOfBirth} and the fees are: {self.tuitionFees}"

    def add_course(self, course):
         self.courses.append(course)

    def hasCourses(self):
         return len(self.courses)>0
     
    def print_courses(self):
         for i in range(len(self.courses)):
              print(self.courses[i])

    def show_students(students):
         for student in students.hasCourses():
              print(student)
