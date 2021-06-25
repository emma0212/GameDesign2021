#Emma Hoffman
#Creating a solitaire game using pygame
import os,random,time,sys,pygame
pygame.init()
os.system('cls')

file="FinalProjectScoreboard.txt"

 #Things that need to be made:
 #interactive menu
 #define mx and my
 # create the sqaures to click the buttons with
 #create a scoreboard
#find a way to darken square when clicked and light when not clicked

def printscore():
    FileRead=open(file,'r')
    print(FileRead.read())
    FileRead.close()


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

# #Created window/screen
Wbox=150
Hbox=60
dist=10
WIDTH=1000
HEIGHT=900
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#loop to keep window open
def menu():
    check=True
    while check:
        #Creating title
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Simon Says")
        screen.fill(GREY)
        text = TitleFont.render("MENU", 1, BLACK)
        screen.blit(text, (440,15))
        #level 1
        text=CharacterFont.render("Level 1",1,WHITE)
        screen.blit(text,(422,100))
        #rectangle 1=level 1
        rect1=pygame.Rect(340, 100, Wbox*2,Hbox)
        pygame.draw.rect(screen, WHITE, rect1, width=4)
        text = TitleFont.render("  ", 1, BLACK)
        screen.blit(text, (160, 350))
        #level 2
        text=CharacterFont.render("Level 2",1,WHITE)
        screen.blit(text,(422,200))
        #rectangle 2=level 2
        rect2=pygame.Rect(340, 200, Wbox*2,Hbox)
        pygame.draw.rect(screen, WHITE, rect2, width=4)
        text = TitleFont.render("  ", 1, BLACK)
        screen.blit(text, (160, 450))
        #level 3
        text=CharacterFont.render("Level 3",1,WHITE)
        screen.blit(text,(422,300))
        #rectangle 3=level 3
        rect3=pygame.Rect(340, 300, Wbox*2,Hbox)
        pygame.draw.rect(screen, WHITE, rect3, width=4)
        text = TitleFont.render("  ", 1, BLACK)
        screen.blit(text, (160, 450))
        #scoreboard
        text=CharacterFont.render("Scoreboard",1,WHITE)
        screen.blit(text,(390,400))
        #rectangle 4= scoreboard
        rect4=pygame.Rect(340, 400, Wbox*2,Hbox)
        pygame.draw.rect(screen, WHITE, rect4, width=4)
        text = TitleFont.render("  ", 1, BLACK)
        screen.blit(text, (160, 450))
        # Exit
        text=CharacterFont.render("Exit Game",1,WHITE)
        screen.blit(text,(400,500))
        #rectangle 5= exit game
        rect5=pygame.Rect(340, 500, Wbox*2,Hbox)
        pygame.draw.rect(screen, WHITE, rect5, width=4)
        text = TitleFont.render("  ", 1, BLACK)
        screen.blit(text, (160, 450))
        pygame.time.delay(2000)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                print(mx," , ", my)
            if rect1.collidepoint(mx,my):
                print("hello")
            elif rect2.collidepoint(mx,my):
                print("How are you?")
            elif rect3.collidepoint(mx,my):
                print("this is difficult")
            elif rect4.collidepoint(mx,my):
                printscore()
            if rect5.collidepoint(mx,my):
                print("Goodbye. Thank you for playing!") 
                pygame.quit()
                sys.exit()
pygame.display.update()

#defining what happens when buttons clicked

def Buttons():
    startx=round((WIDTH - (Wbox + dist) * 13) / 2)
    starty=400
    
class Button:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.shape = pygame.Rect
        self.draw()

def darken(self):
    index = 0
    for i in self.color:
        if i == 255:
            i -= 80
            self.color[index] = i
        index += 1
    self.draw()
    pygame.display.update()

def lighten(self):
    index = 0
    for i in self.color:
        if i == 160:
            i += 80
            self.color[index] = i
        index += 1
    self.draw()
    pygame.display.update()

def darken_then_lighten(self):
    self.darken()
    pygame.time.delay(1000)
    self.lighten()

#creating squares for game
r_square=Button(RED,(200,20,60))
g_square=Button(GREEN,(38,230,0))
b_square=Button(BLUE,(25,25,255))
y_square=Button(YELLOW,(255,255,0))
pygame.display.update()









