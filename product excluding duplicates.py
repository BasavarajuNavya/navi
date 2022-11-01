
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
 
# using naive method
# Duplication Removal List Product
x = list(set(test_list))
prod = 1
for i in x:
    prod *= i
 
# printing list after removal
print("Duplication removal list product : " + str(prod))