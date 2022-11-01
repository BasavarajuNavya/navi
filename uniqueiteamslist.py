list=[1,22,23,22,44,5,6,7,7,5,2,1,2,4,5,66,6,66,66,8,88,10]
l1=[]
count=0
for i in list:
    if i not in l1:
         count+=1
         l1.append(i)
print("the number of unique values are:",count)
print("the unique values are:",l1)