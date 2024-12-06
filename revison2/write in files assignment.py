"""#105
outfile = open("Numbers.txt",'w')
outfile.write("1,2,3,4,5")
outfile.close()

#106
outfile = open("Names.txt",'w')
outfile.write("Johm\nJames\nJinkleheim\nThe\nFirst")
outfile.close()

#107
infile = open("Names.txt",'r')
nums = infile.read()
print(nums)
infile.close()

#108
outfile = open("Names.txt",'a')
A = input("Add a name to file")
outfile.write(A)
outfile.close()

infile = open("Names.txt",'r')
nums = infile.read()
print(nums)
infile.close()
"""
#109
A = int(input("1) Create a new file\n2)Display The File\nAdd a new item to file\nMake a selection 1, 2 or 3"))
if A == 1:
    B = (input("what would you like to write"))
    file109 = open("file109.txt",'w')
    file109.write(B)
    file109.close()
if A == 2:
    file109A = open("file109.txt",'r')
    file109 = file109A.read()
    print(file109)
    file109A.close()
if A == 3:
    file109A = open("file109A.txt",'a')
    A = input("Add something to the file")
    file109A.write(A)
    file109A.close()
    