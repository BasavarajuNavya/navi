# # a=[2,3,4,[3,6,7,[2,5,9]]]
# # b=[]
# # i=0
# # sum=0
# # while i<len(a):
# #     c=a[i]
# #     if type(b)==list:
# #         j=0
# #         while j<len(b):
# #             d=b[j]
# #             if type(d)==list:
# #                 k=0
# #                 while k<len(d):
# #                     e=d[k]
# #                     if type(e)==

# #     sum=sum+a[i]
# #     i=i+1
# # print(sum)


# a=[2,3,4,[3,6,7,[2,5,9]]]
# b=[]
# i=0
# sum=0
# c=[]
# while i<len(a):
#     if type (a[i])==list:
#         j=0
#         num=0
#         while j<len(a[i]):
#             if type (a[i][j])==list:
#                 k=0
#                 co=0
#                 while k<len(a[i][j]):
#                     co+=a[i][j][k]
#                     k=k+1
#             else:
#                 num+=a[i][j]
#             j=j+1
#             c.append(co)
#         c.append(num)
#     else:
#         sum+=a[i]
#     i=i+1
# c.append(sum)
# print(c)
            




# # b=[]
# # b.append(a[2])
# # b.append(a[3][2])
# # b.append(a[3][3][-1])
# # max=0
# # i=0
# # while i<len(b):
# #     num=b[i]
# #     if num>max:
# #         max=num
# #     i=i+1
# # print(max)

# a=[2,3,4,[3,6,7,[2,5,9]]]
# b=[]
# b.append(a[2])
# b.append(a[3][2])
# b.append(a[3][3][-1])
# max=0
# i=0
# while i<len(b):
#     num=b[i]
#     if num>max:
#         max=num
#     i=i+1
# print(b)
# print("the maximum number is:",max)
# 1