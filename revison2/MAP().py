"""
list_0_int = ["1","2","3"]

def return_me_an_int(x):
    return int (x)

print(list_0_int)
result =  list(map(return_me_an_int,list_0_int))
print(result)"""


list_0_int = [1,2,3]
b = [4,5,6]
c = [7,8,9]

def return_me_total(x,y,z):
    return x + y + z

result =  list(map(return_me_total,list_0_int,b,c))
print(result)


words = ['apple','banana','cherry']

#1
def return_me_first_letter(x):

    return x[0]

result =  list(map(return_me_first_letter,words))
print(result)

#2
s = [' hello ', ' world ', ' python ']

def return_me_upper(x):
    return x.upper()

result =  list(map(return_me_upper,s))
print(result)

#3

def return_me_sripped(x):
    return x.strip()

result =  list(map(return_me_sripped,s))
print(result)

#4
celsius = [0, 20, 37, 100]
def return_me_farrenheight(x):
    return (x*9/5)+32

result =  list(map(return_me_farrenheight,celsius))
print(result)



