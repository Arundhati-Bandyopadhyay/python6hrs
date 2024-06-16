import os,sys

if os.path.isfile("ab.txt"):
    f=open('ab.txt','r')
else:
    print('File does not exists')
    sys.exit()

s=f.read()
print(s)
f.close()