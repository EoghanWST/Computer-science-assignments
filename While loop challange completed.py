#45
"""total = 0
while total <= 50:
        number = int(input("Add number "))
        total = total + number
        print (total)
print ("total is over fifty")"""

#46
"""num1 = 0
while num1 <= 5:
    num1 = int(input("enter a number"))
print("last number entered was: ")
print(num1)"""

#47
"""num = 0
E = 0
morenumbers = True
B = int(input("enter a number: "))
C = int(input("enter a number to add to your first number: "))
num = B + C
while morenumbers:
     D = (input("add another number? y/n:"))
     if D == "n":
         break
     if D == "y":
         E = int(input("Enter yout next number tp be added"))
         num = X + E
print ("total:")
print (num)"""

#48
"""cont = True
invilist = []
while cont == True:
    B = input("would you like to invite somone to the party list? ")
    if B == ("n"):
        break
    if B == ("y"):
        C = input("who would you like to add? ")
        invilist.insert(2,C)
print (invilist)"""

#49
"""A = True
C = 0
while A == True:
    B =int(input("ENTER A NUMBER "))
    if B < 50:
        print("TOO LOW")
        C = C+1
    if B > 50:
        print("TOO HIGH")
        C = C+1
    if B == 50:
        print("Well DONE YOU TOOK" ,C, "GUESSES ")"""
#50
"""A = True

while A == True:
    B =int(input("ENTER A NUMBER "))
    if B < 10:
        print("TOO LOW")
    if B > 20:
        print("TOO HIGH")
    if B >= 10 and B <= 20:
        print("THANK YOU")"""

#51
bottles = 10
B = bottles - 1
while True:
    
    print("there are", bottles, "green bottles stiing on a wall,", bottles, "green bottles stiing on a wall")
    bottles1 = int(input("and if one green bottle should accidently fall there would be ? green bottles sitting on the wall "))
    B = bottles - 1
    if bottles1 == B:
        bottles = bottles - 1
    if bottles1 != B:
        print ("wrong")
    if bottles == 0:
        break
print("there are no more green bottles sitting on a wall")





