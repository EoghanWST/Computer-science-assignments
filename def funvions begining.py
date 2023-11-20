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

"""print("1) Addition")
print("2) Subtraction")
a = input("Enter 1 or 2:")

def Add():
    b = int(random.randint(5,20))
    c = int(random.randint(5,20))
    print("num1:",b)
    print("num2:",c)
    d = int(input("What is num1 added with num2 "))
    e = b + c
    return [d , e]

def Sub():
    b = int(random.randint(25,50))
    c = int(random.randint(1,25))
    print("num1:",b)
    print("num2:",c)
    d = int(input("What is num1 minus num2 "))
    e = b - c
    return [d , e]

def check(x,y):
    if x  ==  y:
        print("correct you win")
    if x != y:
        print("wrong the correct awnser is", x)

if a == "1":
    awns =Add()
    awns =check(awns[1],awns[0])
if a == "2":
    awnss = Sub()
    awnss = check(awnss[1],awnss[0])"""

#121

namelist = ["may","bee","not"]
def menu():
    print("1: ADD A NAME\n2: CHANGE A NAME\n3: DELETE A NAME\n4: VIEW ALL ANME IN LIST\n5: END")
    a=int(input("ENTER NO OF DESIRED OPTION"))
    return a

def addname():
    while True:
        b = input("ENTER NAME TO ADD TO LIST")
        namelist.append(b)
        print(namelist)
        c=input("WOULD YOU LIKE TO ADD ANOTHER NAME: y/n?")
        if c == "n":
            return None

def changename():
    while True:
        print(namelist)
        b = input("ENTER NAME TO CHANGE")
        c=namelist.index(b)
        namelist.remove(b)
        d = input("WHAT WOULD YOU LIKE TO CHANGE NAME TO")
        namelist.insert(c,d)
        print(namelist)
        e=input("WOULD YOU LIKE TO CHANGE ANOTHER NAME: y/n?")
        if e == "n":
            return None

def deletename():
    while True:
        print(namelist)
        b = input("ENTER NAME TO DELETE")
        namelist.remove(b)
        print(namelist)
        c = input("DELETE ANOTHER NAME: y/n?")
        if c == "n":
            return None

def fulllist():
    print(namelist)


option = menu()

while option != 5:
    if option == 1:
        addname()
    if option == 2:
        changename()
    if option == 3:
        deletename()
    if option == 4:
        fulllist()
    option = menu()
if option == 5:
    exit()

option = menu()
    

    


