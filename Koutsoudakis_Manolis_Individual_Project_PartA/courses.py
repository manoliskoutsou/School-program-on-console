import itertools

class Course:
     courseNew_id = itertools.count().__next__
     def __init__(self, title, stream, type, start_date, end_date):
        self.id = Course.courseNew_id()
        self.__title = title
        self.__stream = stream
        self.__type = type
        self.__start_date = start_date
        self.__end_date = end_date
        
        
     @property
     def title(self):
         return self.__title
     @title.setter
     def title(self, title):
         self.__title = title

     @property
     def stream(self):
         return self.__stream
     @stream.setter
     def stream(self, stream):
         self.__stream = stream   

     @property
     def type(self):
         return self.__type
     @type.setter
     def type(self, type):
         self._type = type

     @property
     def start_date(self):
         return self.__start_date
     @start_date.setter
     def start_date(self, start_date):
         self.__start_date = start_date

     @property
     def end_day(self):
         return self.__end_date
     @end_day.setter
     def end_date(self, end_date):
         self.__end_date = end_date
       
     def __repr__ (self):
         return f"title : {self.title}, stream : {self.stream}, type : {self.type}, start date : {self.start_date}, end date : {self.end_date}"

    

    


    


    