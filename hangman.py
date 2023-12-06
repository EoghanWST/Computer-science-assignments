#DEFINITIONS
import random
score = 0
lives = 7
wordlist = ["albert","broom","ireland","table","mitochondria","farmhouse","jungle","llama","indicate","hangman","driver"]
word1 =(random.choice(wordlist))
Word = []
j=0
while j != len(word1):
    b = word1[j]
    Word.insert(j,b)
    j = j + 1
wordcount = len(Word)
Wordfil = ["-"]*(wordcount)
Fullword = 0
awnsT = []
awnsF = []

#MAIN BODY CODE
#check if letter in in word return value for position and the letter
while True:
    Q = input("QUESS A LETTER")
    a = Word.count(Q)
    if a > 0:
        b = Word.index(Q)
        d = Word.count(Q)
        c = awnsT.count(Q)
        #IF GUESS IS IN WORD
        if c == 0:
            add = True
        for car in range( len(Word)):
            if Word[car] == Q:
                Wordfil[car] = Q        
                Fullword = Fullword + 1
            awnsT.insert(0,Q)
            #print (Q,"appers",d,"times")
    #IF QUESS IS NOT IN WORD
    if a == 0:
        c = awnsF.count(Q)
        if c == 0:
            add = False
            awnsF.insert(0,Q)
            lives = lives - 1
        
    #USER END STATEMENTS
    print("lives =",lives,"/",7)

    #print("lives =",lives)
    print(Wordfil)
    #hangman display code
    if lives == 7:
        print("        ____ ")
        print("       |    |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 6:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 5:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("       |    |")
        print("            |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 4:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("       |    |")
        print("       |    |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 3:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|    |")
        print("       |    |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 2:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("       |    |")
        print("            |")
        print("            |")
        print("    ________|")
    if lives == 1:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("       |    |")
        print("      /     |")
        print("            |")
        print("    ________|")
    if lives == 0:
        print("        ____ ")
        print("       |    |")
        print("       0    |")
        print("      /|\   |")
        print("       |    |")
        print("      / \   |")
        print("            |")
        print(" yo ass ded |")
        print("    ________|")
        break
    #print("correct guesses",awnsT)
    print("incorrect guesses",awnsF)
    if Fullword == len(Word):
        print("WELL DONE")
        break
    