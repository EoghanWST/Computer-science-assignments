import intro_defi
#1
"""
a = int(input("num 1: "))
b = int(input("num 2: "))
print(intro_defi.add(a,b))
"""
#2
""" 
st = ("nessasary")
print(intro_defi.add_un(st))
"""
#3
"""
pali = input("ENTER WORD ")
check = intro_defi.plaidrome(pali)
print(check)"""

#4
A = input("Enter numbers with spaces between: ")
nums = A.split()  
nums = [int(num) for num in nums]

E,O,E1,O1,EA,OA = intro_defi.numc(nums)
print("Amount of even numbers:",E)
print("Amount of odd numbers:",O)
print("Total of even numbers:",E1)
print("Total of odd numbers:",O1)
print("Average of even numbers:",EA)
print("Average of odd numbers:",OA)
