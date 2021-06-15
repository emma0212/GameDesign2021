#Emma Hoffman
import random
import sys
import os
import time
import datetime

os.system('cls')
#Global variables
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
name =input("What is your name?")
score = 0 #to total number of wins
file= "EmmaGame.txt"
dt=datetime.datetime.now()
linef="\t"+str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)+"\t"+dt.strftime("%A")
def menu(): #create menu to get code
    #PUT SOMETHING IN MENU
    #1 play game
    #2 print score
    #3 change player
    #4 exit game
    return input("What is your choice?")
def updateWord(word, guesses): # function with a parameter to update word
    for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
def printScore():
    FileRead=open(file, 'r')
    print(FileRead.read())
    FileRead.close()
    #Open file as read and print the file
def updateScore(score):
    FileWrite=open(file, 'a')
    line=name+"|t"+ linef +"\t"+ str(score)
    line="The highest score is"+ str(score)
    FileWrite.write("\n"+ line)
    FileWrite.close()
    #open the file and update the score list
        #Name       #Date       #Scor

def PlayGame(answer):       #my function to play the game
    while "Y" in answer:  
        os.system('cls')  
        print(name," Good luck")
word=random.choice(gameWords)
counter=len(word)
print(counter)
print(word)     #delete wien finish code
turns=10  # find better way to create turns
guesses=''
updateWord(word, guesses)
while turns >0 and counter>0:
        newGuess=input("\n Give me a letter ")
        #check that 
        if newGuess not in guesses:
            if newGuess not in word:
                turns -=1
                print ("Sorry that is wrong you still have ", turns," turns")   
        else:
            counter -=word.count(newGuess) #delete repeated letters
            print ("Nice Guess!")  
        guesses += newGuess
else:
        print("You have already used this letter")
        updateWord(word, guesses)
        #end of loop with turns
if counter ==0:
    # print ("")
    print("\n That was amazing, you win")
    score += 1
else:
    print("Sorry, maybe next time")

    answer = input("Do you wish to play again?").upper()
    updateScore(score)
#your main program
check=True

while check:
    varChoice = menu()
    if "1" in varChoice:
            PlayGame("Y", score)
    elif "2" in varChoice:
            printScore()
            input("presss enter when done")
            os.system('cls')
    elif "3" in varChoice:
        name=input("What is your name?")
    else:
        print("Thank you for playing my game! ")
        check=False
        time.sleep(1)
        
        #find a way to print score in order(highest to lowest)