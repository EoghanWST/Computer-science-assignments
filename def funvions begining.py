import random
"""def triple(x,y,z):
    print("hello")
    return x+y+z
    
result = triple(2,2,2)
print(result)"""

#

"""def sub1():
 a = int(input("Enter a Number"))
 b = 0
 while b < x:
     b = b + 1
     print (b)
     

result = sub1()"""
#119
"""def hilow():
    high = int(input("Enter a High Number"))
    low = int(input("Enter a Low Number"))
    return random.randint(low,high)
def numthink():
    print("I am thinking of a number")
    return int(input("quess"))

def numcheck(cn,qn):
    if cn == qn:
        print("correct")
    
comp_num =hilow()
quess_num =numthink()
result =numcheck(comp_num,quess_num)"""

#120
print("1) Addition")
print("2) Subtraction")
a = input("Enter 1 or 2:")

def Add():
    b = int(random.randint(5,20))
    c = int(random.randint(5,20))
    print("num1:",a)
    print("num2:",b)
    d = int(input("What is num1 added with num2 "))
    e = c + b
    return d , e

def Sub():
    b = int(random.randint(25,50))
    c = int(random.randint(1,25))
    print("num1:",a)
    print("num2:",b)
    d = int(input("What is num1 minus num2 "))
    e = c - b
    return d , e

if a == "1":
    awns =Add()
if a == "2":
    awnss = Sub()

def 















