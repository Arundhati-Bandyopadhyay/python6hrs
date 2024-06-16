class Programmer:
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
   
    def setSalary(self,s):
        self.salary=s
    def getSalary(self):
        return self.salary
    
    def setTech(self,t):
        self.Tech=t
    def getTech(self):
        return self.Tech
    
    
    
p1=Programmer()
p1.setName('Arundhati')
p1.setSalary('35000')
p1.setTech(['java','python'])

print(p1.getName())
print(p1.getSalary())
print(p1.getTech())
        

    