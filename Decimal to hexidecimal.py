#Dcimal To Hexidecimal
A = int(input("Deciaml"))
def binary(A):
    Binary = []
    while A > 0:
        B = A//16
        remainder = A % 16
        if remainder == 10:
            remainder = "A"
        if remainder == 11:
            remainder = "B"
        if remainder == 12:
            remainder = "C"
        if remainder == 13:
            remainder = "D"
        if remainder == 14:
            remainder = "E"
        if remainder == 15:
            remainder = "F"
        
        
        
        
        
        Binary.insert(0,remainder)
        A = B
    
    return (Binary)

X = binary(A)
print(X)