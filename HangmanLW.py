#Emma Hoffman
#06/21/2021
#Creating a hangman version of game:
#Using images in list, use fonts, and render them

from typing import Text 
import pygame, math, random, sys, time, os 

pygame.init()  
os.system('cls') 

#create our screen or window 
WIDTH=800 
HEIGHT=500 
screen = pygame.display.set_mode((WIDTH,HEIGHT))  
pygame.display.set_caption("Hangman") 
# Define Colors 
WHITE=[255,255,255] 
BLACK=[0,0,0] 
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 
images = [] 
for i in range(7): 
    image= pygame.image.load("Images/hangman"+str(i)+".png") 
    images.append(image) 
    # screen.blit(images[i],(80,100)) 
    # pygame.display.update() 
    # pygame.time.delay(500) 
#Set up fonts 
TitleFont = pygame.font.SysFont("comicsans", 70) 
WordFont = pygame.font.SysFont("comicsans", 50) 
LetterFont = pygame.font.SysFont("comicsans",40) 
#Define letters for rectangular buttons 
A=65 
Wbox=30 
dist=10 
letters=[]#an array of arrays   [[x, y, ltr, boolean]] 
startx= round((WIDTH - (Wbox + dist)*13) /2) #int function round 
starty= 350 
#load the letters into our double array 
for i in range(26): 
    x=startx+dist*2+((Wbox + dist)*(i%13)) 
    y=starty+((i//13)*(dist + Wbox * 2)) 
    letters.append([x,y,chr(A+i), True])
print(letters)

# function to update game and screen 
def updateScreen(turns,displayWord): 
    screen.fill(WHITE) 
    title=TitleFont.render("Hangman", 1, BLACK) 
    centerTitle=WIDTH/2-title.get_width()/2  #gets  the width of my screen/2 - width ofour text /2 
    screen.blit(title, (centerTitle,20)) 
    screen.blit(images[turns],(100,100)) 
    textW=WordFont.render(displayWord, 1, BLACK) 
    screen.blit(textW,(300, 150)) 
    for letter in letters: 
        x,y,ltr, see= letter 
        if see: 
            rect=pygame.Rect(x-Wbox/2,y-Wbox/2,Wbox,Wbox) 
            pygame.draw.rect(screen, BLACK, rect, width = 1) 
            text=LetterFont.render(ltr,1,BLACK) 
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2)) 
    pygame.display.update() 

 

 

def updateWord(word, guesses):  # function with a parameter to update word 
    displayWord = "" 
    for char in word: 
        if char in guesses: 
            displayWord += char+" " 
        else: 
            displayWord += "_ " 
    return displayWord 

play_again = "Y"
while play_again == "Y" or play_again == "y":
    print("Welcome to Hangman")
    print("Start guessing")

def dis_message(message): 
    screen.fill(WHITE) 
    text = TitleFont.render(message,1,BLACK) 
    screen.blit(text, (200, 200)) 
    pygame.display.update() 
    pygame.time.delay(2000) 
dis_message("Please choose letter you wish to use")
def main():
    word=random.choice(gameWords).upper()
    print(word)
    guesses=[]
    turns=0  # find better way to create turns
    check=True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check=False
            if event.type== pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                for letter in letters:
                    x,y,ltr,see = letter
                    if see:
                        rect=pygame.Rect(x-Wbox/2,y-Wbox/2,Wbox,Wbox)
                        if rect.collidepoint(mx,my):
                            letter[3]=False
                            guesses.append(ltr)
                            if ltr not in word:
                                turns +=1

#always have a way to close your screen 

        displayWord= updateWord(word, guesses) 
        updateScreen(turns,displayWord) 
        win=True 
        for letter in word: 
            if letter not in guesses: 
                win=False 
                break 
        if win: 
            dis_message("You Win!!!") 
            print("Play Again? (y/n)")
            break 
        if turns == 6: 
            dis_message("You lose")
            play_again = input("Play again? (Y/N)") 
            break

pygame.quit() 
sys.exit() 

 