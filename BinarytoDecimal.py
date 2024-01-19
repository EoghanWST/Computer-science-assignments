#Binary to Decimal
def decimal(BinaryA):
    Y = 0
    D = 0
    L = -1
    Len =len(BinaryA)
    while Y < Len:
        B = int(BinaryA[L])
        C = B*2**Y
        D = D + C
        Y=Y+1
        L = L -1
    return(D)
