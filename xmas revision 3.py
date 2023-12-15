#1
 
"""
 
for i in range (1,11):
 
    print(i)
 
 
#2
 
 
for a in range(20,0,-1):
 
    print(a)
 
 


 



#6
 
for h  in  [1,2,3,4,5]:
 
   print("happy birthday")





#3

 
for num in range(1, 11):

    if num % 2 == 0:

        print(num)


#4


n = 20
 
 
for i in range(1,n):

     print(i)
  

#5


n = 20

for z in range(1,n,2):

    print(z)

 
#7


n = int(input("Enter a number: "))
 
print("The first", n, "terms of the series are:", end=" ")

for i in range(1, n+1):

    print(i**2, end=" ")
      

#8
 

a = int(input("Enter a number: "))
 
print("Multiplication table for", a)

for i in range(1, 13):

    print(a, "x", i, "=", a * i)


#9

for g in range(3,32,4):

    print(g)



#10

v = 2

ratio= 3
 
 
for i in range(6):

    a =   v * (ratio ** i)

    print(a)
    
#11
a = 0
c = 0
b = int(input("ENTER YOUR NUMBER"))
while a != b:
    a = a + 1
    c = c + a
print(c)
    
#12
g = 0
f = 0
a = 0
c = 0
b = int(input("ENTER YOUR NUMBER"))

for i in range(b):
    a = 1
    g = g + 1
    f = a/g
    c = c + f
c = round(c,2)
print(c)

#13
a = 0
b = 0
while a != 5:
    a = a + 1
    d = int(input("Enter number"))
    b = b + d
print(b)

#14
a = 0
b = 1
c = int(input("ENTER YOUR NUMBER"))
if c < 0:
    print("NEGITAVE NUMBERS CAN NOT BE FACTORIALED")
if c == 0:
    print("1")
if c > 0:
    while a != c:
        a = a + 1
        b = b * a
    print(b)

#15
a = int(input("Enter Base"))
b = int(input("Enter exponent"))
c = 1
f = -1
d = a
while c != b and f != b:
    d = d * a
    c = c + 1
    f = f - 1
if b < 0:
    d = 1/d
print (d)"""


