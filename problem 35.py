#list approach
import math
number = 100
sqrt = math.sqrt(number)

numbers=[]
i=1
for digit in range (1,100):
    numbers.append(digit)
print numbers
for digit in numbers:
    is_prime=True
    for x in range (int(math.ceil(math.sqrt(13195)))+1):
        if x>1:
            if  13195 % x==0:
                is_prime=False
            if is_prime==False:
                numbers.remove(x)
print numbers
#object approach
import math
class Number:
    digita= [range(1,100)]
    def __init__(self, digit):
        self.a=digita
        
    def switch(self):
        self.a
