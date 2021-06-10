#Emma Hoffman
#started from Lucas Williams code

print("What is your name?")
name=input()
user=name.title()
print(user)
varChoice =" "
def menu():         # declaring a function o
    print("*"*28)
    print("*"," "*6,"Game"," "*12,"*")
    print("*"," "*9,"Menu"," "*9,"*")
    print("*"," "*24,"*")
    print("*"," "*2,"1- Part 1"," "*10,"*")
    print("*"," "*2,"2- Part 2"," "*10,"*")
    print("*"," "*2,"3- Part 3"," "* 10,"*")
    print("*"," "*2,"4- Part 4"," " *10,"*")
    print("*"," "*2,"5- Part 5"," " *10,"*")
    print("*"," "*2,"6- Part 6"," " *10,"*")
    print("*"," "*2,"7- Part 7"," " *10,"*")
    print("*"," "*2,"8- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,L4,L5,L6,L7 or EX", end= " ")
    varChoice = input()    #local variable 
    return varChoice 
 
def score ():
    print ("Scores")
    print ("23434    peter")
    print ("22556    emma")
    print ("17804    lucas")
    print ("567      ben")
    print ("200       sam")
def gamePause():
    print ("do you want to change levels?")
    level = input()
    if level !='no':
        varChoice = menu()
 
while varChoice != 8:
    if varChoice == 1:
        print ("You are in level 1")
        print("please enter your name")
        txt=input()
        x=txt.capitalize()
        print(x)
        gamePause()

    if varChoice == 2:
        print ("You are in level 2")
        print("What is your favorite color?")
        txt=input()
        x=txt.center(45)
        print(x)
        gamePause()
    
    if varChoice == 3:
        score ()
        print("Who has the best score?")
        txt=input()
        mylist=[True,False,False,True]
        x=any(mylist)
        print(x)
        gamePause()

    if varChoice == 4:
        print("You are in level 4")
        print("How would you rate this game, from 1-10?")
        txt=input()
        x=txt.isdigit()
        print(x)
        gamePause()
    
    if varChoice == 5:
        print("You are in level 5")
        print("Choose a fruit")
        txt=input()
        x=txt.swapcase()
        print(x)
        gamePause()

    if varChoice == 6:
        print("You are in level 6")
        print("What word would you like to input?")
        txt=input()
        x=txt.lower()
        print(x)
        gamePause()
    
    if varChoice == 7:
        print("You are in level 7")
        print("Type a sentence")
        txt=input()
        x=txt.encode()
        print(x)
        gamePause()

    varChoice = menu ()
print ("goodbye, have a nice day")