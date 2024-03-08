#1
def add(x,y):
    a  = x + y
    return(a)
#2
def add_un(x):
    un = ("un")
    b = un + x
    return(b)
#3
def plaidrome(x):
    a = x[::-1]
    if a == x:
        b = (x,"is a palindrome")
        return(b)
    if a != x:
        a = (x,"is not a palindrome")
        return(a)
#4
def numc(x):
    G = 0
    F = -1
    O = 0
    O1 = 0
    E = 0
    E1 = 0
    
    while G != len(x):
        a = x[F]
        F = F - 1
        G = G + 1
        
        if a % 2 == 0:
            E = E + 1
            E1 = E1 + a

        if a % 2 == 1:
            O = O + 1
            O1 = O1 + a
            
        if O > 0:
            OA = O1/O
        else:
            OA = 0
            
        if E > 0:
            EA = E1/E
        else:
            EA = 0

            

    
    return (E,O,E1,O1,EA,OA)