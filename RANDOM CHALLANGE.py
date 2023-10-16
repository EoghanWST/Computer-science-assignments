import random
#52
"""mynum= random.randint(0,100)
print(mynum)"""
#53
"""mynum = random.choice(["apple","banna","orange","garpe","pineapple"])
print(mynum)"""
#55
"""ht = random.choice(["heads","tails"])
hta = input("HEADS OR TAILS ")
if hta == ht:
    print(ht)
    print("you win")
else:
    print(ht)
    print("i win")"""
#56
"""ra = random.randint(1,5)
a = True
while a == True:
    ca = int(input("Pick a number!"))
    if ca == ra:
        print("Well done")
    while ca<ra or ca>ra:
        if ca<ra:
            print("WRONG TOO LOW")
        if ca>ra:
            print("WRONG TOO HIGH")
        if cb == ra:
            print("Well done")
            break"""
#57
""""ra = random.randint(1,10)
a = True
while a == True:
    ca = int(input("Pick a number!"))
    if ca == ra:
        print("Well done")
    while ca<ra or ca>ra:
        if ca<ra:
            print("WRONG TOO LOW")
        if ca>ra:
            print("WRONG TOO HIGH")
        if cb == ra:
            print("Well done")
            break"""

#58
"""x = 0
Z = True
a=[]
score= 0
while x < 11:
    a.insert(0,random.randint(1,25))
    x=x+1
print(a)

print("QUIZ TIME")
while Z == True:
    AWNS1 = a[0] + a[1]
    in1 = int(input("what is " + str(a[0]) + " plus " + str(a[1]) + " :"))
    if in1 == AWNS1:
        score= score + 1
        print ("correct")
    if in1 != AWNS1:
        print ("incorrect")
        
    AWNS2 = a[2] - a[3]
    in2 = int(input("what is " + str(a[2]) + " minus " + str(a[3]) + " :"))
    if in2 == AWNS2:
        score= score + 1
        print ("correct")
    if in2 != AWNS2:
        print ("incorrect")
        
    AWNS3 = a[4] * a[5]
    in3 = int(input("what is " + str(a[4]) + " times " + str(a[5]) + " :"))
    if in3 == AWNS3:
        score= score + 1
        print ("correct")
    if in3 != AWNS3:
        print ("incorrect")
    
    AWNS4 = a[6] * a[7]
    in4 = int(input("what is " + str(a[6]) + " times " + str(a[7]) + " :"))
    if in4 == AWNS4:
        score= score + 1
        print ("correct")
    if in4 != AWNS4:
        print ("incorrect")

    AWNS5 = a[8] + a[9] * a[10]
    in5 = int(input("what is " + str(a[8]) + " plus " + str(a[9]) + " times " + str(a[10]) +  " :"))
    if in5 == AWNS5:
        score= score + 1
        print ("correct")
    if in5 != AWNS5:
        print ("incorrect")
    break
print ("YOU SCORED", score, "OUT OF 5")"""

"""#59
P = True
x = 0
A = random.choice(["red","orange","yellow","green","blue"])
B = ["red","orange","yellow","green","blue"]
print(B)
while P == True:
    C = input("GUESS WHICH COLOUR I CHOSE ")
    if C == A:
        print("YOU GOT ME")
        break
    if C == "red":
        print("WRONG i left yo mom on red lil buddy")
    if C == "orange":
        print("WRONG bet your orange like Trump lil buddy")
    if C == "yellow":
        print("WRONG yellow minion headass")
    if C == "green":
        print("WRONG you green and sick lil guy?")
    if C == "blue":
        print("WRONG blue smurf headass?")"""




    
    
    


    











