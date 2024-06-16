import pickle,student # type: ignore

f=open("Student.dat","wb")
s=student.Student(123,'john',90)
pickle.dump(s,f)
f.close()