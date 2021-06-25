#Emma Hoffman
#Final Project
#Making a 3 level soltaire game
#It will have an easy,medium, and hard level

import sys,os,random,math,pygame
pygame.init()
os.system('cls')
#Defining fonts
TitleFont= pygame.font.SysFont("couriernew", 100)  #set the type of font and the size 
CharacterFont=pygame.font.SysFont("comicsans", 75)
WordFont=pygame.font.SysFont("comicsans", 50)
#a while loop to keep the screen open until red button clicked
file="FinalProjectScoreboard.txt"

def printScore():
    FileRead=open(file, 'r')
    print(FileRead.read())
    FileRead.close()

check=True
while check:
    #screen parameters
    WIDTH=1200
    HEIGHT=1200
    #Defining colors
    BLACK=[0,0,0]
    WHITE=[255,255,255]
    RED=[200,20,60]
    GREEN=[34,139,34]
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    #Creating title
    pygame.display.set_caption("Solitaire")
    screen.fill(GREEN)
    Wbox=80
    pygame.display.update()

images=[]
for image in file:
    image=pygame.image.load("Images/solitiare"+image+".jpg")
    images.append(image)

def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WordFont.render(message, 1, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    print("hello")

click=False
def game_Init(message): 
    test=True
    while test:
    #Print message
        text = TitleFont.render(message, 1, BLACK)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/3)))
        #rectangle 1-- level 1
        rect1=pygame.Rect(150, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect1, width=1)
        text = TitleFont.render("Level 1", 1, RED)
        screen.blit(text, (500 , 500))
        #rectangle 2-- level 2
        rect2=pygame.Rect(150, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect2, width=1)
        text = TitleFont.render("Level 2", 1, RED)
        screen.blit(text, (500 , 500))
        #rectange 3-- level 3
        rect3=pygame.Rect(150, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect3, width=1)
        text = TitleFont.render("Level 3", 1, RED)
        screen.blit(text, (500 , 500))
        #rectangle 4-- scoreboard
        rect4=pygame.Rect(150, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect4, width=1)
        text = TitleFont.render("Scoreboard", 1, RED)
        screen.blit(text, (500 , 500))
        #rect 5-- leave the game
        rect5=pygame.Rect(150, 350, Wbox*2,Wbox*2)
        pygame.draw.rect(screen, BLACK, rect5, width=1)
        text = TitleFont.render("Exit Game", 1, RED)
        screen.blit(text, (500 , 500))
        pygame.display.update()
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
                display_message("Goodbye. Thank you for playing!")
                pygame.quit()
                sys.exit()
    pygame.display.update()

def updateScreen(displayWord):
    screen.fill(WHITE)
    #Display Title
    title=TitleFont.render("Hangman",1, BLACK)
    centerTitle= WIDTH/2-title.get_width()/2
    screen.blit(title, (centerTitle,20))
    #Display Word
    textW=WordFont.render(displayWord,1, BLACK)
    screen.blit(textW, (300,150))







