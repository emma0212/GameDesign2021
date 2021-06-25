#Emma Hoffman
#06/21/2021
#Creating a hangman version of game:
#Using images in list, use fonts, and render them
import os, pygame, sys, time, random, math
from pygame.mouse import get_pos

os.system('cls')
pygame.init() 
#Create display screen

WIDTH=800   #uppercase because it behaves as a constant
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman")
#Define colors
WHITE=[255,255,255]
BLACK=[0,0,0]
RED=[200,50,0]

#Word Lists
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
images=[]
for i in range(7):
    image=pygame.image.load("Images/hangman"+str(i)+".png")
    images.append(image)
    # screen.blit(images[i],(100,100))
    # pygame.display.update()
    # pygame.time.delay(300)
#always have a way to close the window/screen
#Define font objects
def init_game(message):
    #display message
    screen.fill(WHITE)
    text=TitleFont.render(message,1,BLACK)
    screen.blit(text, (25, 300))
    #create yes rectangle
    rect1=pygame.Rect(150,350,Wbox*2,Wbox*2)
    pygame.draw.rect(screen,BLACK,rect1,width=1)
    text=LetterFont.render("yes", 1, BLACK)
    screen.blit(text,(160,365))
    #create the No rectangle
    rect2=pygame.Rect(150,350,Wbox*2,Wbox*2)
    pygame.draw.rect(screen,BLACK,rect2,width=1)
    text=LetterFont.render("no", 1, BLACK)
    screen.blit(text,(320,365))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                print(mx," , ", my)
                if rect1.collidepoint(mx,my):
                    main()
                if rect2.collidepoint(mx,my):
                    dis_message("Goodbye. Thank you for playing!")
                    pygame.quit()
                    sys.exit()
    pygame.display.update()
    pygame.time.delay(2000)



TitleFont=pygame.font.SysFont("comicsans", 60)  #to  set type of font and size
WordFont=pygame.font.SysFont("comicsans", 35)
LetterFont=pygame.font.SysFont("comicsans", 40)

#Define Letters for rectangular buttons
A=65
Wbox=30
dist=10
letters = [] #array of arrays
startx=round((WIDTH-(Wbox+dist)*13)/2) #round converts to an integer
starty=350
#loading the letters double array [[x,y,ltr,boolean]]
for i in range (26):
    x= startx+dist*2+((Wbox+dist)*(i%13))
    y=starty+((i//13)*(dist+Wbox*2))
    letters.append([x,y,chr(A+i),True])
print(letters)

def updateScreen(turns,displayWord):
    screen.fill(WHITE)
    #print title
    title= TitleFont.render("HANGMAN", 1, BLACK)
    centerTitle=WIDTH/2-title.get_width()/2
    screen.blit(title,(centerTitle,20))
    #print image
    screen.blit(images[turns],(100,100))
    #print word
    textW=WordFont.render(displayWord, 1, BLACK)
    screen.blit(textW, (300,150))
    #print letters
    for letter in letters:
        x,y,ltr,see = letter
        if see:
            rect=pygame.Rect(x-Wbox/2,y-Wbox/2,Wbox,Wbox)
            pygame.draw.rect(screen, BLACK,rect,width=1)
            text=LetterFont.render(ltr,1,BLACK)
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    pygame.display.update()

def updateWord(word, guesses): # function with a parameter to update word
    displayWord=" "
    for char in word:
        if char in guesses:
            displayWord += char+" "
        else:
            displayWord +="_ "
    return displayWord
#load images to list

def dis_message(message):
    screen.fill(WHITE)
    text=TitleFont.render(message,1,BLACK)
    screen.blit(text, (0, 250))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    dis_message("Please choose the letter you wish to use")
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

        displayWord=updateWord(word, guesses)
        updateScreen(turns, displayWord)
        win=True
        for letter in word:
            if letter not in guesses:
                win=False
        if win:
            dis_message("You win!")
            break
        if turns == 6:
            dis_message("You Lose")
            break
def option():
    print("I'm here")
while True:
    init_game("Would you like to play?")
    


