#L = input("enter your list")
def bubsort(L):
    numlist = L.split()  
    numlist = [int(num) for num in numlist]
    print(numlist)


    lenum = len(numlist)

    X = 0
    Y = lenum - 1
    Pass = 0
    while X != Y:
        A = 0
        B = 0
        while A != Y:
            pos = numlist[A]
            pos2 = numlist[A+1]
            if pos > pos2:
                numlist.remove(pos)
                numlist.insert(A+1,pos)
                A = A + 1
                print(numlist,"SWAP")
            if pos < pos2:
                A = A + 1
                print(numlist,"NO SWAP")
            
        X=X+1
        Pass = Pass + 1
        print("end of pass",Pass)
    return(Pass,"passes to receive sorted", numlist)
