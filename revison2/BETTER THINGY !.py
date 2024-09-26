f = open("exercise.csv","r")
header = f.readline()

#getstuffoutofdocumentinator
#calories list
calories = [60,45,30,15,160,210,270,300,150,120,90,25]
#list of lists
listsOL = [list60 = [],list45 = [],list30 = [],list15 = [],list160 = [],list210 = [],list270 = [],list300 = [],list150 = [],list120 = [],list180 = [],list90 = [],list25 = []]
#list variables
list60 = []
list45 = []
list30 = []
list15 = []
list160 = []
list210 = []
list270 = []
list300 = []
list150 = []
list120 = []
list180 = []
list90 = []
list25 = []
#list of nums
ListONum = [num60 = 0,num45 = 0,num30 = 0,num15 = 0,num160 = 0,num210 = 0,num270 = 0,num300 = 0,num150 = 0,num120 = 0,num180 = 0,num90 = 0,num25 = 0]
#num variables
num60 = 0
num45 = 0
num30 = 0
num15 = 0
num160 = 0
num210 = 0
num270 = 0
num300 = 0
num150 = 0
num120 = 0
num180 = 0
num90= 0
num25 = 0

for line in f:
    line = line.strip()
    line = line.split(',')
    A = line[0]
    B = (line[-1])
    if B == "":
        continue
    else:
        B = float(B)
    if A == "60":
        list60.append(B)
        num60 = num60 + 1
    if A == "45":
        list45.append(B)
        num45 = num45 + 1
    if A == "30":
        list30.append(B)
        num30 = num30 + 1
    if A == "15":
        list15.append(B)
        num15 = num15 + 1
    if A == "160":
        list160.append(B)
        num160 = num160 + 1
    if A == "210":
        list210.append(B)
        num210 = num210 + 1
    if A == "270":
        list270.append(B)
        num270 = num270 + 1
    if A == "300":
        list300.append(B)
        num300 = num300 + 1
    if A == "150":
        list150.append(B)
        num150 = num150 + 1
    if A == "120":
        list120.append(B)
        num120 = num120 + 1
    if A == "180":
        list180.append(B)
        num180 = num180 + 1
    if A == "90":
        list90.append(B)
        num90 = num90 + 1
    if A == "25":
        list25.append(B)
        num25 = num25 + 1
        
def av(Cal,L,num):
    #av of 45
    tot = sum(L)
    av = tot/num
    #print(L)
    return('average of',Cal,av)


def avT20(Cal,L,num):
    #av of top 20 in 47
    L.sort()
    L2 = L[-20:]
    tot =sum(L2)
    av = tot/20
    #print(list47)
    return("average of top 20 in", av)

A = av(60,list60,num60)
B = avT20(60,list60,num60)
print(A)
print(B)





"""#compare 60 and 45 difrence/20 times 100/1
dif = av60 - av45
average = (av60+av45)/2
percentdif= (dif/average)*(100)
print("percentage diffrence between durations 60 and 45 is:",percentdif)"""

