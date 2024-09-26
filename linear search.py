def linser (tarval,L):
    x = 0
    while True:
        pos = L[x]
        if pos == tarval:
            return(tarval,"is in position",L.index(pos))
            break
        if pos != tarval:
            x = x + 1
