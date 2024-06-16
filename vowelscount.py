String=input("enter the string")
Str=String.lower()

c=0
for i in Str:
    if(i=='a' or i=='a' or i=='e' or i=='o' or i=='u'):
        c+=1
if(c==0):
    print("no vowels")
else:
    print(str(c))