def linser (tarval,L1):
    L = L1.split()  
    L = [int(num) for num in L]
    print(numlist)
    x = 0
    while True:
        pos = L[x]
        if pos == tarval:
            return(tarval,"is in position",L.index(pos))
            break
        if pos != tarval:
            x = x + 1