l1=[1,2,3,4,5]
l3=[6,7,8,9,10]
lst=[]
# for i in range(len(lst)):
#     lst.append(l1[i]*l3[i])

lst=[l1[i]*l3[i] for i in range (len(lst))]

print(lst)


 