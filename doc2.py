# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest
list=[['g','f','g',],['i','s'],['b','e','s','t']]
print("The original list is:"+ str(list))
# Using join() + list comprehension
res = ''.join(ele for sub in list for ele in sub)
print("The string after joining is:"+res)