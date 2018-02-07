#making random list
import math
from random import randint
random_list=[]
for i in range (1000):
    random_list.append(randint(0,1000))
print random_list

#minmium
for x in range (1000):
    min(random_list)
print min(random_list)



#add variable to other list
sorted_list= []

#loop it
while len(random_list)>0:
    a=min(random_list)
    sorted_list.append(a)
    random_list.remove(a)
print sorted_list
