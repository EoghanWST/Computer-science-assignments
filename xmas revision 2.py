# for odd you do , 2% == 0 , EVEN 2% == 1
# 1:
#
while True:
   
    user = int(input(" Lets see if the number you enter is odd or even"))
    if user % 2== 0:
           print("The number is EVEN")
    else:
           print(" the number is ODD")
#even = 2% == 0
#odd = 2% == 1
#          
 
#
#2
b = int(input("insert your age so we can check if your eligible to vote!"))
if b >= 18:
    print("YOUR ELIGIBLE TO VOTE")
else:
    print("you cant vote FOO")
   
   
 
#3
NU1 = int(input("enter one number"))
NU2 = int(input("enter a second number"))
 
if NU1> NU2:
    print(NU1 ,"is the greatest number  ")
if NU2>NU1:
    print(NU2, "is the greatest number  ")
#  
#4
#
while True:
   
 
    bananas  = int(input("Enter a  number  "))
    if bananas  >= 1:
        print("positive  ")
    if bananas == 0:
        print("Zero  ")
    if bananas < 0:
        print("negative  ")
#      
#5
kid = 12
#teen = 13,19
#adult = 20,59
#senior = 60
#
while True:
    a = int(input("Enter your age: "))
 
    if a <= 12:
        print("You're a child!")
    elif a <= 19:
        print("You're a teenager!")
    elif a <= 59:
        print("You're an adult!")
    else:
        print("You're a senior citizen!")
#        
#6
#monday = 1
#tuesday = 2
#wednesday = 3
#thursday = 4
#friday = 5
#saturday = 6
#sunday = 7
 
#
day = int(input("Enter a number from 1 to 7: "))
 
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("ERROR")
   
#
   
#7
# used float for decimals
 
#
weight = float(input("Enter your weight in KG"))
print("your weight is", weight , "kg")
height = float(input("enter your height in METERS"))
print(" your height is ", height, "m")
 
BMI = weight / (height * height)
print(BMI)
if BMI < 18.5:
    print("you are underweight")
elif 18.5 <= BMI <= 24.9:
    print(" you are a normal weight gg")
elif 25 <= BMI <= 29.9:
    print("you are overweight :(")
else:
    print(" YOU ARE OBESE :c")
   
 
#8
sub1 = float(input("What grade did you get in maths?"))
sub2 = float(input("What grade did you get in history?"))
sub3= float(input("What grade  did you get in COMPUTER SCIENCE??"))
 
avg = sub1+sub2+sub3 / 3
 
#banana = avg =  %2.f
print(banana)
#
#9
#
#b^2 - 4AC
a = int(input("whats the coefficient of x²?"))
b = int(input("whats the coefficient of X?"))
c = int(input("whats the constant?"))
#lol= 2
poo = -4
roots = b*b-poo*a*c
 
print(roots)
print ("the roots of the equation", a,"x²", b,"x", "+", c)
#
 
#10
#LOWEST TO HIGHEST
#
a= int(input("write a number"))
b= int(input("write a second number"))
c= int(input("write a third number"))
 
MJ = [a,b,c]
MJ.sort()
print(MJ)
#
 
#11
# BIGGEST NUMBER TO LOWEST
a= int(input("write a number"))
b= int(input("write a second number"))
c= int(input("write a third number"))
Mk = [a,b,c]
Mk.sort()
Mk.reverse()
print(Mk)
 
 
#12
caca = input("Enter a letter")
#ban = ["a" , "e" , "i" , "o" , "u"]
if caca == ("a" or "e" or "i" or "o" or "u"):
    print("thats a vowel")
else:
    print("thats a consanant")
   
#13  
year = int(input("Enter a year: "))    
if year % 4 == 0:
    print(year, "is a leap year!")
   
elif year % 100 == 0:
    print(year, "is a leap year!")
   
elif year % 400 == 0:
    print(year, "is a leap year!")
else:
    print("its a normal year")
   
#14
   
baka = int(input("Enter the number of calls: "))    
if baka <= 100:
        bill = 200
elif baka <= 150:
        bill = 200 + (baka - 100) * 0.60
elif baka <= 200:
        bill = 200 + 50 * 0.60 + (baka - 150) * 0.50
else:
        bill = 200 + 50 * 0.60 + 50 * 0.50 + (baka - 200) * 0.40
       
print("€", bill, "is the amount")