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
    print("*"," "*2,"L1- Part 1"," "*10,"*")
    print("*"," "*2,"L2- Part 2"," "*10,"*")
    print("*"," "*2,"L3- Part 3"," "* 10,"*")
    print("*"," "*2,"L4- Part 4"," " *10,"*")
    print("*"," "*2,"L5- Part 5"," " *10,"*")
    print("*"," "*2,"L6- Part 6"," " *10,"*")
    print("*"," "*2,"L7- Part 7"," " *10,"*")
    print("*"," "*2,"L8- Exit Game"," "*7,"*")
    print("*"*28)
    print("Enter either L1,L2,L3,L4,L5,L6,L7 or EX", end= " ")
    option = input()    #local variable 
    return option
 
def score ():
    print ("Scores")
    print ("23434    peter")
    print ("22556    Emma")
    print ("17804    Lucas")
    print ("567      Ben")
    print ("200       Sam")
def gamePause():
    print ("do you want to keep playing?")
    level = input().upper()
    if "Y" in level:
        return True
    else:
        return False

varChoice=menu()  
while varChoice != "EX":
    if varChoice == "L1":
            print ("You are in level 1")
            print("please enter your name")
            txt=input()
            x=txt.capitalize()
            print(x)
            convert=gamePause()
    if varChoice == "L2":
            print ("You are in level 2")
            print("What is your favorite color?")
            txt=input()
            x=txt.center(45)
            print(x)
            convert=gamePause()
    if varChoice == "L3":
            score ()
            print("Who has the best score?")
            txt=input()
            mylist=[True,False,False,True]
            x=any(mylist)
            print(x)
            convert=gamePause()
    if varChoice == "L4":
            print("You are in level 4")
            print("How would you rate this game, from 1-10?")
            txt=input()
            x=txt.isdigit()
            print(x)
            convert=gamePause()
    if varChoice == "L5":
            print("You are in level 5")
            print("Choose a fruit")
            txt=input()
            x=txt.swapcase()
            print(x)
            convert=gamePause()
    if varChoice == "L6":
            print("You are in level 6")
            print("enter a word in capitals")
            txt=input()
            x=txt.lower()
            print(x)
            convert=gamePause()
    if varChoice == "L7":
        convert= True
        while convert:
            print("You are in level 7")
            print("Type a sentence")
            txt=input()
            x=txt.encode()
            print(x)
            convert=gamePause()

    varChoice = menu ()
print ("goodbye, have a nice day")