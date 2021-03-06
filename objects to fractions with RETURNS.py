import math
from random import randint
from fractions import gcd
class Fraction:
    numerator = 0
    denominator= 0
    
    def __init__(self, numerator, denominator):
        self.numerator=(numerator)
        self.denominator=(denominator)
    def fraction(self):
         a= str(self.numerator) + "/" + str(self.denominator)
         return a
#each fraction is in 2 PARTS: name.numerator and name.denominator
#multiplying the denominators and numinators will get a new fraction
#1.denominator*2.denominator= a
#2.numerator * 1.denominator= b
#2.denominator * 1.numerator= c
#add numerators for NEW NUMERATOR 
    def add(self, user2):
        a=int(self.denominator)* int(user2.denominator)
        b=int(user2.numerator)* int(self.denominator)
        c=int (user2.denominator)* int(self.numerator)
        d= str(c+b) + "/" + str(a)
        return d
        
    def decimal(self):
        x=float(self.numerator)/float(self.denominator) 
        return str(x)
        
    def subtract(self, user2):
        a=int(self.denominator)* int(user2.denominator)
        b=int(user2.numerator)* int(self.denominator)
        c=int (user2.denominator)* int(self.numerator)
        d= str(c-b) + "/" + str(a)
        return d
        
    def mixedfraction(self):
        x=int(self.numerator)/int(self.denominator)
        y=int(self.numerator)%int(self.denominator)
        z=int(self.denominator)
        a= str(x) + " " + str(y)+ "/" +str(z)
        return a
        
    def multiply(self, user2):
        a=int(self.denominator)* int(user2.denominator)
        b=int(user2.numerator)*int(self.numerator)
        c= str(b) + "/" + str(a)
        return a,b
        
    def divide(self, user2):
        a=int(self.denominator)* int(user2.numerator)
        b=int(user2.denominator)*int(self.numerator)
        c= str(b) + "/" + str(a)
        return a,b
        
    def simplify(self):
        x=gcd(int(self.numerator), int(self.denominator))
        y=int(self.numerator)/x
        z=int(self.denominator)/x
        a= str(y) + "/" + str(z)
        return x,y
    
n=10
d=12
y=16
z=18
f=Fraction(n, d) 
user2=Fraction(y, z)
#2 arguments in definition of function, so put tbe other user in parentheses
print (f.simplify())
