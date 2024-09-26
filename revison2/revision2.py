f = open("exercise.csv","r")
header = f.readline()

#getstuffoutofdocumentinator

#variables
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



num45 = 0
num60 = 0

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
        
#av of 60
tot60 = sum(list60)
av60 = tot60/num60
print(list60)
print("average of 60",av60)
#av of top 20 in 60
list60.sort()
list62 = list60[-20:]
tot62 =sum(list62)
av62 = tot62/20
#print(list62)
print("average of top 20 in 60", av62)

#av of 45
tot45 = sum(list45)
av45 = tot45/num45
#print(list45)
print("average of 45",av45)
#av of top 20 in 47
list45.sort()
list47 = list45[-20:]
tot47 =sum(list45)
av47 = tot47/20
#print(list47)
print("average of top 20 in 45", av47)

#compare 60 and 45 difrence/20 times 100/1
dif = av60 - av45
average = (av60+av45)/2
percentdif= (dif/average)*(100)
print("percentage diffrence between durations 60 and 45 is:",percentdif)
