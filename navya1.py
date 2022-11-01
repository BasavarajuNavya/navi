# # matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
# # flatten_matrix = []
  
# # for sublist in matrix:
# #     for val in sublist:
# #         flatten_matrix.append(val)
          
# # print(flatten_matrix)

# # flatten matrix:

# # matrix=[[1,2,3],[4,5,6],[7,8,9,10,11,12,13]]
# # flatten_matrix=[]
# # for sublist in matrix:
# #     for val in sublist:
# #         flatten_matrix.append(val)
# # print(flatten_matrix)

# # planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
# # flatten_planets=[]
# # for sublist in planets:
# #     for planet in sublist:
          
# #         if len(planet) < 6:
# #             flatten_planets.append(planet)
          
# # print(flatten_planets)
    

# # matrix = [[1, 2, 3, 4, 5],
# #       [6, 7, 8, 9, 10],
# #       [11, 12, 13, 14, 15],
# #       [16, 17, 18, 19, 20]]
# # i = 0
# # y = (len(matrix)-1)
# # while i < len(matrix):
# #     if i == 0:
# #         # print 1st row.
# #         for rows in matrix[i]:
# #             print(rows,end=" ")

# #     # print all the last element of every rows, except 1st and last row.
# #     elif i != 0 and i != y:
# #         print(matrix[i][-1],end=" ")

# #     # print the last row in reverse.
# #     elif i == y and i != 0:
# #         matrix[i].sort(reverse=True)
# #         for row in matrix[i]:
# #             print(row,end=" ")

# #         print(matrix[i-1][0],end=" ")       # print the 1st element of 3rd row.

# #         # print the 1st four elements of 2nd row.
# #         for r in matrix[1][0:4]:
# #             print(r,end=" ")

# #         # finally print the rest of the elements in reverse.
# #         matrix[2].sort(reverse=True)
# #         for r_remain in matrix[2][1:4]:
# #             print(r_remain,end=" ")

# #     i += 1
# aTuple=("orange")
# print(type(aTuple)







# user=int(input("enter the dogs age"))
# if user==1 and user==15+-2*4:
#     print(15)
#     print(15+9)
# if user>3:
#     print(15+-2*4)
# elif user>4:
#     print(15+9-3*4)
# else:
#     print("no")

# user=int(input("enter the dogs age and human age"))
# if user==1 and user==15+9-2*4:
#     print("human age")
# if user>=3 and user>=4: 
#     print("dog age",user)
# # else:
#     print("no")

# print("dog age",)else:
#     print("no")

# Name=['Navya','Jyothi','Mani','Rama','Meena','sreelekha']
# city=['Anantapur','kadapa','hindupur','viyayavada','Anantapur','tirupathi']
# age=[25,23,24,26,27,28]
# z=zip(Name,city,age)
# for Name,city,age in z:
#     print("%s the city name is %s and the age is %s"%(Name,city,age))

# x = [1]
# print(id(x),':',x) #=> 4501046920 : [1]
# x.append(5)
# x.extend([6,7])
# print(id(x),':',x) #=> 4501046920 : [1, 5, 6, 7]

# a=[1,2,3,4,5]
# b=[6,7,8]
# a.append(b)
# print(a)

i=5
while i>=1:
    k=0
    while k<=5-i:
        print("",end=" ")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i-1
    print()
    



