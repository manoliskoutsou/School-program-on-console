import itertools

class Trainer:
    trainerNew_id = itertools.count().__next__
    def __init__(self, firstName, lastName, subject):
        self.id = Trainer.trainerNew_id()
        self.__firstName = firstName
        self.__lastName = lastName
        self.__subject = subject



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
    def subject(self):
         return self.__subject
    @subject.setter
    def subject(self, subject):
         self.__subject = subject  
     

    def __repr__ (self):
        return f"{self.firstName} {self.lastName} with subject {self.subject}"


