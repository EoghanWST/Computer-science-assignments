#CEASARS CYPHER
#PART 1
#ii
"""ABCDEFGHIJKLMNOPQRSTUVWXYZ
   DEFGHIJKLMNOPQRSTUVWXYZABC"""
#ii
"""ATHLONE COMMUNITY COLLEGE
   DWKORQH FRPPXQLWB FROOHJH"""
#iii
k=0
cyp  = ["A","B","C","D","E","F","H","I","J","K","L","M","N","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
new_string = ""
abc = input("What is your message")
key = int(input ("what is your key"))
for ch in abc:
    if ch in cyp:
        index_position = cyp.index(ch)
        k= index_position + key
        if k > 25:
            k = k%26
        
        new_string = new_string + cyp[k]
print(new_string)

