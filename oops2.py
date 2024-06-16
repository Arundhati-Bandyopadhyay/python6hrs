from builtins import sum
class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def avg(self):
        noOfrate=len(self.ratings)
        avg=sum(self.ratings)/noOfrate
        print(avg)
    
c1=Course('java',[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.avg()
        