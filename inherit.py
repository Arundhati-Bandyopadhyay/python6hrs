class BMW:
    def __init__(self,make,model):

        self.make=make
        self.model=model
class threeseries(BMW):
    def __init__(self,cruisecontroled, make, model):
        BMW.__init__(self,make, model)
        self.cruisecontroled=cruisecontroled
       
class fiveseries(BMW):
    def __init__(self,parkassist, make, model):
        BMW.__init__(self,make, model)
        self.parkassist=parkassist

ts=threeseries(True,'BMW','456')
print(ts.cruisecontroled)
Fs=fiveseries(False,'BMW','489')
print(Fs.parkassist)


       

    