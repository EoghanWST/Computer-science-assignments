"and"
def AND_gate(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0
    
print(AND_gate(1,1))


"or"
def OR_gate(a,b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1

print(OR_gate(1,0))

"xor"
def XOR_gate(a,b):
    if a == 0 and b == 0:
        return 0
    if a == 1 and b == 1:
        return 0
    else:
        return 1

print(XOR_gate(0,0))


