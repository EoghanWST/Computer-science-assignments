import SolidFunc
Menu = input("1) AREA OF CIRC\n2) PERIM OF CIRC\n3) AREA OF REC\n4) PERIM OF REC")
if Menu == "1":
    C = int(input("enter diameter"))
    Awn = SolidFunc.circareainator(C)
    print(Awn)
if Menu == "2":
    B = int(input("enter diameter"))
    Awn = SolidFunc.circperminator(B)
    print(Awn)
if Menu == "3":
    H = int(input("enter the height:  "))
    W = int(input("enter the width:  "))
    Awn = SolidFunc.rectareainator(H,W)
    print(Awn)
if Menu == "4":
    H = int(input("enter the height:  "))
    W = int(input("enter the width:  "))
    Awn = SolidFunc.recperiminator(H,W)
    print(Awn)