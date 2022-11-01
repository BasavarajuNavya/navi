


list=[1,1,2,2,2,2,2,3,3,4,4,5,5,6,6,7,7,7,7,7,8,8,9,11,12,12,12,12,12]
print("the original list:" +  str(list))
k=4
l1=[]
for i in list:
    l2=list.count(i)
    if l2>k and i not in l1:
        l1.append(i)
print("the required elements are:"+ str(l1))