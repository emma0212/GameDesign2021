#Emma Hoffman
#Creating a solitaire game using pygame
import os,random,time,sys,pygame
pygame.init()
os.system('cls')


#Things that need to be made:
# a menu
# a way to close the window succesfully
# create the sqaures to click the buttons with
#create a scoreboard
#find a way to darken square when clicked and light when not clicked

#Created window/screen


#Creating colors
BLACK=[0,0,0]
WHITE=[255,255,255]
YELLOW=[255,221,51]
BLUE=[0,77,230]
RED=[200,20,60]
GREEN=[34,139,34]
BG=[38,230,0]
BR=[255,25,25]
BB=[25,25,255]
BY=[255,255,0]
GREY=[132,132,130]

#Defining fonts
TitleFont= pygame.font.SysFont("comicsans", 45)  #set the type of font and the size 
CharacterFont=pygame.font.SysFont("arial", 40)
WordFont=pygame.font.SysFont("arial", 20)

Wbox=150
Hbox=60

def click():
    def __init__(self, color, pos):
     self.color = color
     self.pos = pos
     self.shape = pygame.Rect
     self.draw()

check=True
while check:
    #Creating title
    WIDTH=1000
    HEIGHT=900
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Simon Says")
    screen.fill(GREY)
    text = TitleFont.render("MENU", 1, BLACK)
    screen.blit(text, (440,15))
    text=CharacterFont.render("Level 1",1,WHITE)
    screen.blit(text,(422,60))
    rect1=pygame.Rect(420, 45, Wbox*2,Wbox)
    pygame.draw.rect(screen, WHITE, rect1, width=1)
    text = TitleFont.render("  ", 1, BLACK)
    screen.blit(text, (50, 5))
    text=CharacterFont.render("Level 2",1,WHITE)
    screen.blit(text,(422,160))
    text=CharacterFont.render("Level 3",1,WHITE)
    screen.blit(text,(422,260))
    text=CharacterFont.render("Scoreboard",1,WHITE)
    screen.blit(text,(422,360))
    text=CharacterFont.render("End Game",1,WHITE)
    screen.blit(text,(422,460))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.display.update()

#rectangle 1-- level 1
rect1=pygame.Rect(10, 100, Wbox*2,Wbox*2)
pygame.draw.rect(screen, WHITE, rect1, width=6)
text = TitleFont.render("  ", 1, BLACK)
screen.blit(text, (300 , 150))

#rectangle 2-- level 2
rect2=pygame.Rect(25, 10, Wbox*2,Wbox*2)
pygame.draw.rect(screen, WHITE, rect2, width=6)
text = TitleFont.render("  ", 1, BLACK)
screen.blit(text, (300 , 250))

#rectange 3-- level 3
rect3=pygame.Rect(50, 25, Wbox*2,Wbox*2)
pygame.draw.rect(screen, WHITE, rect3, width=6)
text = TitleFont.render("  ", 1, BLACK)
screen.blit(text, (300, 350))

#rectangle 4-- scoreboard
rect4=pygame.Rect(75, 50, Wbox*2,Wbox*2)
pygame.draw.rect(screen, WHITE, rect4, width=60)
text = TitleFont.render("  ", 1, BLACK)
screen.blit(text, (300, 450))

#rect 5-- leave the game
rect5=pygame.Rect(100, 75, Wbox*2,Wbox*2)
pygame.draw.rect(screen, WHITE, rect5, width=6)
text = TitleFont.render("  ", 1, BLACK)
screen.blit(text, (300 , 550))
pygame.display.update()

# r_square=click(RED,(255,25,25))
# g_square=click(GREEN,(38,230,0))
# b_square=click(BLUE,(25,25,255))
# y_square=click(YELLOW,(255,255,0))
# pygame.display.update()

    

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            print(mx," , ", my)
            if rect1.collidepoint(mx,my): 
                print()   
            if rect5.collidepoint(mx,my):
                print("Goodbye. Thank you for playing!")
                pygame.quit()
                sys.exit()
pygame.display.update()
