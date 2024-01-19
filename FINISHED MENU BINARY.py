import BinarytoDecimal
import Decimaltobinary


print("To convert decimal to binary enter 1")
print("To convert binary to decimal enter 2")
print("To add two binarys enter 3")
P = input("")
if P == "1":
    A = int(input("Deciaml"))
    X = Decimaltobinary.binary(A)
    print(X)
if P == "2":
    Z = input("Enter Binary: ")
    BinaryA = Z.split()  
    BinaryA = [int(num) for num in BinaryA]
    y = BinarytoDecimal.decimal(BinaryA)
    print(y)
if P == "3":
    Z = input("Enter First Binary: ")
    BinaryA = Z.split()  
    BinaryA = [int(num) for num in BinaryA]  
    
    Z = input("Enter Second Binary: ")
    BinaryB = Z.split()  
    BinaryB = [int(num) for num in BinaryB]  
    
    X = BinarytoDecimal.decimal(BinaryA)
    Y = BinarytoDecimal.decimal(BinaryB)
    S = X + Y
    W = Decimaltobinary.binary(S)
    print(W)
