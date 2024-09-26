f = open("exercise.csv","r")
header = f.readline()
listoflines = []
for line in f:
    line = line.strip()
    line = line.split(',')
    listoflines.append(line)
    
print(listoflines)
lisloflines[0][0]