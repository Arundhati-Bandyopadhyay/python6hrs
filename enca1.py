class Student:
    def __init__(self):
        self.__id=123
        self.__name='Dip'
    def display(self):
        print(self.__id)
        print(self.__name)

s=Student()
s.display()
print(s._Student__id)
       