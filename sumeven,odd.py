elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sumeven=0
sumodd=0
for i in elements:
    if(i%2==0):
        sumeven+=i
    else:
        sumodd+=i
print("sum of even numbers is:",sumeven)
print("sum of odd numbers is:",sumodd)
