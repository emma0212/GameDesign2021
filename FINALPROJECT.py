#Emma Hoffman
#Creating a simon says game

import pygame,sys,os,random
from random import randint
from time import sleep

pygame.init()
(width, height) = (450, 450)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simon')
pygame.display.flip()
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
TitleFont= pygame.font.SysFont("comicsans", 45)  #set the type of font and the size 
CharacterFont=pygame.font.SysFont("arial", 40)
WordFont=pygame.font.SysFont("arial", 20)
Wbox=150
Hbox=60
dist=10
WIDTH=1000
HEIGHT=900

file="FinalProjectScoreboard.txt"

def printscore():
    FileRead=open(file,'r')
    print(FileRead.read())
    FileRead.close()

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
                text=WordFont.render("Level 1",1,WHITE)
                screen.blit(text,(WIDTH/2-text.get_WIDTH()/2,HEIGHT/2))
                pygame.display.update()
                pygame.time.delay(2000)
            elif rect2.collidepoint(mx,my):
                text=WordFont.render("Level 2",1,WHITE)
                screen.blit(text,(WIDTH/2-text.get_WIDTH()/2,HEIGHT/2))
                pygame.display.update()
                pygame.time.delay(2000)
            elif rect3.collidepoint(mx,my):
                text=WordFont.render("Level 3",1,WHITE)
                screen.blit(text,(WIDTH/2-text.get_WIDTH()/2,HEIGHT/2))
                pygame.display.update()
                pygame.time.delay(2000)
            elif rect4.collidepoint(mx,my):
                printscore()
                pygame.display.update()
                pygame.time.delay(2000)
            if rect5.collidepoint(mx,my):
                text=WordFont.render("Exit",1,WHITE)
                screen.blit(text,(WIDTH/2-text.get_WIDTH()/2,HEIGHT/2))
                pygame.quit()
                sys.exit()
            pygame.display.update()
            pygame.time.delay(2000)


class Button:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.shape = pygame.Rect
        self.draw()

    def draw(self):
        self.shape = pygame.draw.rect(screen, self.color, self.pos)

    def darken(self):
        index = 0
        for i in self.color:
            if i == 255:
                i -= 95
                self.color[index] = i
            index += 1
        self.draw()
        pygame.display.update()

    def lighten(self):
        index = 0
        for i in self.color:
            if i == 160:
                i += 95
                self.color[index] = i
            index += 1
        self.draw()
        pygame.display.update()

    def dark_then_light(self):
        self.darken()
        sleep(.5)
        self.lighten()


red_square = Button(RED, (25, 25, 200, 200))
green_square = Button(GREEN, (225, 25, 200, 200))
blue_square = Button(BLUE, (25, 225, 200, 200))
yellow_square = Button(YELLOW, (225, 225, 200, 200))
pygame.display.update()

def click():
    global player_list
    pos = pygame.mouse.get_pos()
    if (25 < pos[0] < 225) and (25 < pos[1] < 225):
        press(0)
        player_list.append(0)
    elif (225 < pos[0] < 425) and (25 < pos[1] < 225):
        press(1)
        player_list.append(1)
    elif (25 < pos[0] < 225) and (225 < pos[1] < 425):
        press(2)
        player_list.append(2)
    elif (225 < pos[0] < 425) and (225 < pos[1] < 425):
        press(3)
        player_list.append(3)


def press(index):
    if index == 0:
        red_square.dark_then_light()
    elif index == 1:
        green_square.dark_then_light()
    elif index == 2:
        blue_square.dark_then_light()
    elif index == 3:
        yellow_square.dark_then_light()


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def erase_text():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 450, 25))


correct_list = []
player_list = []


def ai_turn():
    global AI_turn, player_turn, correct_list
    index = randint(0, 3)
    correct_list.append(index)
    for i in correct_list:
        press(i)
        sleep(.15)
    AI_turn = False
    player_turn = True


def check():
    global correct_list, player_list, DEFEAT
    if len(correct_list) == len(player_list):
        if correct_list == player_list:
            return True
        else:
            DEFEAT = True
    return False


END_SCREEN = True
running = True
AI_turn = True
player_turn = False
DEFEAT = False
score = 0

while running:
    if AI_turn:
        erase_text()
        draw_text(screen, 'SIMON\'S TURN', 20, 225, 2, )
        pygame.display.update()
        sleep(.5)
        ai_turn()
    if player_turn:
        erase_text()
        draw_text(screen, 'PLAYER\'S TURN', 20, 225, 2, )
        pygame.display.update()
        for event in pygame.event.get():
            if not DEFEAT:
                if event.type == pygame.QUIT:
                    running = False
                    END_SCREEN = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click()
                    if check():
                        AI_turn = True
                        player_turn = False
                        player_list = []
                        score += 1
                        break
            else:
                break
    if DEFEAT:
            break

screen.fill((0, 0, 0))
draw_text(screen, 'YOU LOSE!!!', 50, 225, 200)
draw_text(screen, 'SCORE:', 50, 225, 255)
draw_text(screen, str(score), 50, 225, 305)
pygame.display.update()

while END_SCREEN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            END_SCREEN = False

