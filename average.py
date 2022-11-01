# a=list()
# n=int(input("enter the range:"))
# print("the elements are:")
# for i in range(int(n)):
#     k=int(input(""))
#     a.append(k)
# su=sum(a)
# avg=su/n
# print("sum:",su)
# print("average:",avg)

a=list()
n=int(input("Enter the len:"))
print("The elements are:")
i=0
while i<n:
    k=int(input(""))
    a.append(k)
    i=i+1
sm=sum(a)
avg=sm/n
print("sthe sum is:",sm)
print("The average is:",avg)