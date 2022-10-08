from trainers import Trainer
from courses import Course


class TrainerPerCourse(Trainer, Course):
    def __init__ (self, trainer_id, course_id):
        self._trainer_id = trainer_id
        self._course_id = course_id

    @property
    def trainer_id(self):
        return self._trainer_id
    @trainer_id.setter
    def trainer_id(self, trainer_id):
        self._trainer_id = trainer_id

    @property
    def course_id(self):
        return self._course_id
    @course_id.setter
    def course_id(self, course_id):
        self._course_id = course_id

    def __repr__ (self):
        return(f"({self.trainer_id}, {self.course_id})")