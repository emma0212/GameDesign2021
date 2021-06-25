#Emma Hoffman
#Creating a list of words
#randomly select word from list for user to guess
#give user turns
#show word to user when letters guessed
#play game as long as user wants

import random
import sys
import os
import time
import datetime

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 
name=input("What is your name ") 
answer=input("Do you want to guess a word? ").upper() #control the main loop 
score=0 #to total the number of wins 
while "Y" in answer: 
    print("Good luck ", name, "!") 
    word=random.choice(gameWords) 

    counter=len(word) 

    print(counter) 

    print (word)    #delete when we finish the code 

    turns= 10   #should we conider controlling this number when he/she misses 

    guesses='' 

    while turns>0 and counter >0: 
        for char in word: 
            if char in guesses: 
                print(char,end=' ') 
            else: 
                print('_', end =' ') 

        newGuess=input("\n\n Give me a letter ") 

        #check that the new letter has not been used before 

        if newGuess not in guesses: 

            if newGuess not in word: 

                turns -=1    #       turns = turns -1 

                print("Wrong! You have  ", turns, "guesses left") 

            else: 

                counter -=word.count(newGuess) #deleten repeated letters 

                print("nice guess!") 

            guesses += newGuess 

        else: 

            print("you used this one already") 

 
 

    if counter ==0: 

        print("Fantastic you are Champion") 

        score +=1 

    else: 

        print("Sorry, try harder next time") 

     # find a way to decide if the person won the game or not  

     # keep a count of how many words they guessed    

     # #ask user if the want to play again 
     
    answer=input("Do you want to play again? ").upper() 
print(name," your score is: ", score) 