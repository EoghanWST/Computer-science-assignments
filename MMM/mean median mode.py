F = open ("C:/Users/19EWest.ACC/MMM/NumL.txt",'r')
x = F.read()
OPT = input("SELECT OPTION \n 1 MEAN  \n 2 MEDIAN  \n 3 MODE  \n 4 FREQUENCY  ")
x = x.split()
x = sorted(x)
print(x)
L = []
for i in x:
    L.append(int(i))

def mean(L):
    Tot = sum(L)
    Len = len(L)
    mean = Tot/Len
    return(mean)

def med(L):
    Len = len(L)
    Half = int(Len / 2)
    if Len % 2 == 0:
        median = int((int(L[Half]) + int(L[Half - 1])) / 2)
        return(L[median])
    else:
        A = round(Half)
        median = int(L[A])
        return(median)
    
def Mode(L):
    Mode= 0
    check = []
    n = len(L)
    for i in range (0,n):
        if L[i] not in check:
            check.append(L[i])
            b = L[i]
            frequency = L.count(b)
            if frequency > Mode:
                Mode = b
    print(Mode)

def freq(L):
    check = []
    n = len(L)
    for i in range (0,n):
        if L[i] not in check:
            check.append(L[i])
            b = L[i]
            frequency = L.count(b)
            print(b, "occurs" , frequency, "amount of times")
            

if OPT == "1":
    Awns =mean(L)
    print(Awns)

if OPT == "2":
    Awns =med(L)
    print(Awns)

if OPT == "3":
    Awns =Mode(L)
    
if OPT == "4":
    Awns =freq(L)