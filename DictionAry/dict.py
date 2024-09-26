f = open("book.txt","r")
header = f.read()
header = header.lower()
f = open("book.txt","r")
 
dictionary = {}

for line in f:
    line = line.strip()
    line = line.split()
    for word in line:
        if word in dictionary:
            dictionary[word] = dictionary[word] +1
        else: dictionary[word] = 1
 







"""
f = open("book.txt","r")
header = f.read()
header = header.lower()


def freq(L):
    check = [" "]
    n = len(L)
    for i in range (0,n):
        if L[i] not in check:
            check.append(L[i])
            b = L[i]
            frequency = L.count(b)
            print(b,":",frequency)

A = input("WORD FRQ = 1 \nCHAR FRQ = 2\n")
if A == "1":
    print("Word:Count")
    L1 = (header.split())
    Awns =freq(L1)
if A == "2":
    print("Char:Count")
    L = header
    Awns =freq(L)"""
    
    
