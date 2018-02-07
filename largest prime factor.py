#factors
#import math 
#factor=1
#factors =[]
#for number in range (1,13195):
 #   if 13195 % number==0:
  #      factors.append (number)
#prime
#ceil = rounds so the sqrt will pass
#int = makes the element in parentheses a number
#for number in factors:
 #   is_prime=True
  #  for erys in range (int(math.ceil(math.sqrt(13195)))+1):
   #     if erys>1:
    #        if  13195 % erys==0:
    #            is_prime=False
     #       if is_prime==False:
      #          factors.remove(erys)
#print factors

#correct collab me and erys
import math
number = 600851475143
sqrt = math.sqrt(number)

# find factors
factors = []
for i in range (2,int(math.ceil(sqrt))):
    if number % i == 0:
        factors.append(i)
# prime factors
for factor in factors:
    is_prime = True
    for new_factor in range (2,int(math.ceil(math.sqrt(factor)) + 1)):
            if factor % new_factor == 0:
                factors.remove(factor)
# max prime factor
print(factors[len(factors) - 1])

