#7
print("%s" % 3)
print("%d" % 3.14)
print("%f" %3)
print("%s" %"hi!")

 

 

# u have to change line 4 from F to S as it has error
#8
# experiment with math
import math
r = 5

 

print("Radius: %d, Area: %157.2f," % (r, 2*math.pi*r))

 

 

# so when u say import math PYTHON knows what math is???

 

# IF u  put number before ".2F" it makes it distant


msg = "hi %s. how are you"

 

name = "Hey!!!"

 

print(msg%name)
#9
word = "james"
print(word[0:5:2])

word2 = "JhonDipPeta"
word3 = "JaSonAy"
b=word2[4:7]
c=word3[2:5]
print(word2[4:7])
print(word3[2:5])

string1 = "Aunt"
string2 = "Kelly"
d = string1[0:2]+ string2[:] + string1[2:4]
print(d)
