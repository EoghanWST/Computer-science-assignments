#uninator
A = "balls" #input("Word")
def uninator(x):
    unned = "un" + x
    return(unned)

"""unnedW = uninator(A)
print(unnedW)"""

#pluralinator
def pluralinator(x):
    plural = x + "s"
    return(plural)
"""Pluralw = pluralinator(A)
print(Pluralw)"""

#middlecharinator
"""A = ("jam")
def middlecharinator(x):
    Len = len(x)
    mc = Len//2
    if Len % 2 == 0:
        return(x[mc:mc+2])
    else:
        return(x[mc])
    
midchar = middlecharinator(A)
print(midchar)"""

#circareainator
def circareainator(x):
    r = x/2
    r2 = r*r
    CA = 3.14*r2
    return (CA)

#rectareainator
def  rectareainator(x,y):
   a =  x*y
   return(a)

#circperminator
def circperminator(x):
    r = x/2
    A = 2*3.14*r
    return(A)
#recperiminator
def recperiminator(x,y):
    H = 2*x
    W = 2*7
    perim = H + W
    return(perim)
  

