import turtle
import random
"""turtle.shape("turtle")
scr = turtle.Screen()
scr.bgcolor("white")
turtle.color("black","red")
turtle.begin_fill()
turtle.pendown()
turtle.pensize(3)

a=0
b=0
while a < 4:
    turtle.forward(80)
    turtle.left(90)
    a=a+1
    
turtle.left(180)
turtle.forward(80)
turtle.right(90)
turtle.forward(80)


while b < 3:
    turtle.left(90)
    turtle.forward(80)
    b=b+1

turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(200)"""



turtle.shape("turtle")
scr = turtle.Screen()
scr.bgcolor("white")
turtle.color("purple","red")
turtle.pendown()
turtle.left(90)
turtle.pensize(3)

#60
a=0

"""while a < 4:
    turtle.forward(80)
    turtle.left(90)
    a=a+1"""
#62
"""while a < 3:
    turtle.forward(80)
    turtle.left(120)
    a=a+1"""
#63
"""turtle.left(180)
turtle.forward(100)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)"""
#64
"""r = 50
turtle.circle(r)"""
#not a q
"""while a == 0:
    turtle.left(44)
    turtle.forward(180)"""
#63
"""while a == 0:
    turtle.left(144)
    turtle.forward(100)"""
#65
"""while a < 8:
    A = random.choice(["red","orange","yellow","green","blue","purple"])
    turtle.color(A)
    turtle.forward(100)
    turtle.right(45)
    a = a + 1"""
#68 0FSET 30 LOOPPS 12 TIMES
"""a = 0
while a < 12:
    b=0
    while  b < 8:
        turtle.forward(100)
        turtle.right(45)
        b= b+1
    turtle.right(30)
    a = a + 1"""
#69
"""b=0
A = random.randint(10,200)
B = random.randint(0,360)
C = random.randint(1,2)

while  b < 30:
    turtle.forward(A)
    if C == 1:
        turtle.right(B)
        b = b=1
    if C ==2:
        turtle.left(B)
        b = b+1"""

 






for i in range(2): 
    turtle.forward(100) 
    turtle.left(90) 
    turtle.forward(150) 
    turtle.left(90) 
  
# bottom left side 
turtle.goto(50,50) 
  
# forming back rectangle face 
for i in range(2): 
    turtle.forward(100) 
    turtle.left(90) 
    turtle.forward(150) 
    turtle.left(90) 
  
# bottom right side 
turtle.goto(-100,50) 
turtle.goto(-150,0) 
  
# top right side 
turtle.goto(-150,100) 
turtle.goto(-100,150)

# top right side 
turtle.goto(50,150) 
turtle.goto(0,100) 
  




















turtle.exitonclick()
