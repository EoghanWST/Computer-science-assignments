"""#1
 
a = input (" Hello what's your name?  ")
print(" Hello" , a)
 
#2
one = int(input("Enter one number"))
two = int(input(" Enter a second number"))
 
add = one+two
print(one , "and" , two ,"added is " , add)
 
 
#3 celcius to Farenheit
 
farenheight = int(input("Enter a temperature in farenheight to get it in celcius"))
celcius = (farenheight-32)*5/9
 
 
print (celcius, "celcius")
         
#4  ur an addiction
print("lets find the simple interest.")
bas  = int(input(" insert the principal number"))
lol = int(input("insert time"))
xd = int(input("insert rate"))
         
ab = bas*lol*xd
print(" the simple interest is " , ab)
 
 
#5
second  = 1
minute = 60
hour = 3600
 
#a= second/second
#print(a)
 
lolz = int(input(" insert the number of seconds and the code will give you the hours , minutes and time"))
 
pz = lolz//hour
 
wa = pz//minute
bo = minute//60
 
print(pz, "hours",wa ,"minutes" , "and " , bo ,"seconds" )
 
#6
 
variable1  = int(input("enter a number"))
variable2 = int(input("enter a second number"))
print(variable1)
print(variable2)
 
 
#7
 
 
 
#8
a = int(input("insert a number to be the radius of a circle to FIND the area  "))
pi = 3.14
bob = a*pi*pi
circ = 2*pi*a
print(bob, "is the area of the circle" , "and" ,  circ ,"is the circumference")
 
 
#9
leng = int(input("What is your desired length of this rectangle  "))
wi = int(input("What is your desired width of this rectangle  "))
area = leng*wi
ci = 2*(leng+wi)
print(area, "is the area and" , ci , "is the circumference of the rectangle")"""
 
"""#10
A = 7 #int(input("enter side A"))
B = 6 #int(input("enter side B"))
C = 5 #int(input("enter side C"))

S = (A + B + C)/2

print (S)

Area = (S*(S - A)*(S - B)*(S - C))**0.5
print ("Area is egual to", Area)"""

#11
P = 5 #int(input("Enter pricipal"))
R =  10000 #int(input("Enter rate"))
T =   10 #int(input("enter Time"))

a = P*(1 + R/100)**T - P
print(a)
