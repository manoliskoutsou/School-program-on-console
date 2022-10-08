class AssignmentPerCourse:
    def __init__ (self, assignment_id, course_id):
        self._assignment_id = assignment_id
        self._course_id = course_id

    @property
    def assignment_id(self):
        return self._assignment_id
    @assignment_id.setter
    def assignment_id(self, assignment_id):
        self._assignment_id = assignment_id

    @property
    def course_id(self):
        return self._course_id
    @course_id.setter
    def course_id(self,course_id):
        self._course_id= course_id

    def __repr__ (self):
        return(f"({self.assignment_id}, {self.course_id})")