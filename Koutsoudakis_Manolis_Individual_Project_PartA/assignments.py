import itertools

class Assignment:
    assingmentNew_id = itertools.count().__next__
    def __init__(self, title, description, subDateTime, oralMark, totalMark):
        self.id=Assignment.assingmentNew_id()
        self.__title = title
        self.__description = description
        self.__subDateTime = subDateTime
        self.__oralMark = oralMark
        self.__totalMark = totalMark
        

    @property
    def title(self):
         return self.__title
    @title.setter
    def title(self, title):
         self.__title = title

    @property
    def description(self):
         return self.__description
    @description.setter    
    def description(self, description):
         self.__description = description 

    @property
    def subDateTime(self):
         return self.__subDateTime
    @subDateTime.setter    
    def subDateTime(self, subDateTime):
         self.__subDateTime = subDateTime

    @property
    def oralMark(self):
         return self.__oralMark
    @oralMark.setter    
    def oralMark(self, oralMark):
         self.__oralMark = oralMark
            
    @property
    def totalMark(self):
         return self.__totalMark
    @totalMark.setter
    def totalMark(self, totalMark):
         self.__totalMark = totalMark

          
    def __repr__ (self):
        return f"{self.title},the description is {self.description},the subDateTime is {self.subDateTime},the oralMark is {self.oralMark} and the totalMark is {self.totalMark}"
    

    

    

   

 


