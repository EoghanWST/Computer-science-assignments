F = open ("C:/Users/19EWest.ACC/MMM/NumL.txt",'r')
x = F.read()
OPT = input("SELECT OPTION \n 1 MEAN  \n 2 MEDIAN  \n 3 MODE  \n 4 FREQUENCY  ")
x = x.split()
x = sorted(x)
print(x)
L = []
for i in x:
    L.append(int(i))

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
            
            
            
if OPT == "3":
    Awns =Mode(L)