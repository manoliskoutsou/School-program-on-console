class StudentPerCourse:
    def __init__ (self, student_id, course_id):
        self._student_id = student_id
        self._course_id = course_id

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
    def course_id(self,course_id):
        self._course_id= course_id
        

    def __repr__ (self):
        return(f"({self.student_id}, {self.course_id})")
