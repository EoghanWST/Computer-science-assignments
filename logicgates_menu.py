import logicgates
print("enter the name of the gate you want to use from this list:")
print("AND,OR,XOR")
gate = input("")

if gate == "AND":
    print("type 1 to see truthtable, type 2 to enter inputs")
    U = input("")
    if U == "1":
        for x in range(2):
            for y in range(2):
                print(x,y,logicgates.AND_gate(x,y))
    if U == "2":
        x = int(input("enter a"))
        y = int(input("enter b"))
        print(x,y,logicgates.AND_gate(x,y))
    
    
    
if gate == "OR":
    print("type 1 to see truthtable, type 2 to enter inputs")
    U = input("")
    if U == "1":
        for x in range(2):
            for y in range(2):
                print(x,y,logicgates.OR_gate(x,y))
    if U == "2":
        x = int(input("enter a"))
        y = int(input("enter b"))
        print(x,y,logicgates.OR_gate(x,y))
        
if gate == "XOR":
    print("type 1 to see truthtable, type 2 to enter inputs")
    U = input("")
    if U == "1":
        for x in range(2):
            for y in range(2):
                print(x,y,logicgates.XOR_gate(x,y))
    if U == "2":
        x = int(input("enter a"))
        y = int(input("enter b"))
        print(x,y,logicgates.XOR_gate(x,y))