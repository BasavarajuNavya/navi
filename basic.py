# list=[1,1,1,2,3,3,4,5,6,6]
# i=0
# b=[]
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i]) 
#     i=i+1
# print(b)



# i=0
# b=[]
# while i<len(list):
#     c=list.count(list[i])
#     if c==1:
#         b.append(list[i])
                                                      #     i=i+1
# print(b)

# list=[2,4,7,8,12,9]
# even=[]
# odd=[]
# i=0                                                                                                                                                                                                 
# while i<len(list):
#     if list[i]%2==0:
#         even.append(list[i])
#     else:
#         odd.append(list[i])
#     i=i+1
# print("the even num are:",even)
# print("the odd num are:",odd)


# list1=[5,2,3]
# list2=[10,5,3,2]
# list3=list1+list2
# s=0
# i=0
# while i<len(list3):
#     s=s+list3[i]
#     i=i+1
# print("sum of elements is:",s)

# l=[1,2,3,4,5,6,6,7,7,8,8,10,11]
# x=len(l)
# print("the count is",x)

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# i=0
# while i<len(a)-3:
#     c=[a[i],a[i+1],a[i+2]]
#     b.append(c)
#     i=i+3
# print(b)

# a=[55,22,10]
# i=0
# while i<len(a):
#     d=a[i]
#     i=i+1
#     print(d,end=" ")    


# a=[1,2,5,7,10]
# sum=0
# count=0
# i=0
# while i<len(a):
#     sum=sum+a[i]
#     count=count+1
#     i=i+1
# print("the sum  of two lists is:",sum) 
# print("count is:",count) 


# list=[1,2,3,4,5]
# list.reverse()
# print(list)

# b=[1,2,3][1,1,2]
# i=0
# s=0
# while i<len(b):
#     s=s+b[i]
#     i=i+1

# i=0
# sum=0
# while i<len(c):
#     sum=sum+c[i]
#     i=i+1
# print(sum,s)


# a=[1,2,3]
# d=sum(a)
# f=[1,1,2]
# e=sum(f)
# print(d,e)

l=[3,4,5,20,5,25,1,3]
x=l.count(5)
print(x)