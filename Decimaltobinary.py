#Dcimal To Binary
def binary(A):
    Binary = []
    while A > 0:
        B = A//2
        remainder = A % 2
        Binary.insert(0,remainder)
        A = B
    return (Binary)