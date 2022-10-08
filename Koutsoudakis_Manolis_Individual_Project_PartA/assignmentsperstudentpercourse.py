
class AssignmentPerStudentPerCourse:
     def __init__ (self, assignment_id, student_id, course_id) :
         self._assignment_id = assignment_id
         self._student_id = student_id
         self._course_id = course_id

        
     @property
     def assignment_id(self):
        return self._assignment_id
     @assignment_id.setter
     def assignment_id(self, assignment_id):
        self._assignment_id = assignment_id

     @property
     def student_id(self):
        return self._student_id
     @student_id.setter
     def student_id(self, student_id):
        self._student_id = student_id

     @property
     def course_id(self):
        return self._course_id
     @course_id.setter
     def set_course_id(self,value):
        self._course_id= value
   

    

     def __repr__ (self):
        return(f"({self.assignment_id}, {self.student_id}, {self.course_id})")