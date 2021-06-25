#Emma Hoffman
#Started from Maria Suarez code
# 06/14/2021 
#Word Game 
# We are creating a list of words 
# randomly select a word from the list for the user to guess 
# give the user some turns 
# show the word to the user with the characters guessed   
# only play the game as long as the user has turns or has guessed the word 

 
 

import random 
def updateWord(word):   #function with a parameter
    for char in word: 
        if char in guesses: 
            print(char,end='_') 
        else: 
            print('_', end =' ') 
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
                print(char,end='_') 
    else: 
            print('_', end =' ')
    newGuess=input("\n\n Give me a letter ") 
    if newGuess not in guesses:
            if newGuess not in word:
                turns -=1       #tunrs=turns -1
                print("You are wrong. You have", turns, "guesses left")
            else:
                counter -=word.count(newGuess)   #delete repeated letters
                print("Good Guess")
            guesses += newGuess 
    else: 
            print("you used this one already")
    updateWord()
    if counter ==0: 
        print("\n Amazing, you won!") 
        score +=1 
    else: 
        print("Sorry, try harder next time") 
     # find a way to decide if the person won the game or not  
     # keep a count of how many words they guessed    
     # #ask user if the want to play again 

    answer=input("Do you want to play again? ").upper() 
print(name," your score is: ", score) 

