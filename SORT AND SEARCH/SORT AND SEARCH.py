import bubsort

OPT = input("SELCET OPTION \n 1 BUBBLE SORT \n 2 LINEAR SEARCH")
if OPT == "1":
    L = input("enter your list")
    G = bubsort(L)
    print(G)
if OPT == "2":
    tarval = int(input("tarval"))
    L1 = input("enter your list")
    A = linser(tarval,L1)
    print(A)