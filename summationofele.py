# list=[1,12,123,1234,12345,123456,1234567]
# print("The given list is:"+ str(list))
# b=[]
# for i in list:
#     sum=0
#     for j in str(i):
#         sum=sum+int(j)
#     b.append(sum)
# print("the list after summation is:" + str(b))


# using while loop


list=[1,12,123,1234,12345,123456,1234567]
i=0
b=[]
while i<len(list):
    num=list[i]
    sum=0
    while num>0:
        r=num%10
        sum=sum+r
        num=num//10
    b.append(sum)    
    i=i+1
print("The given list is " + str(list))
print("The list after summation is:",b)