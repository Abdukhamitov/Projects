import pygame
import sys
import time
#initialization
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((1000,680))



#class1
class TextBox():
    def __init__(self,main = ""):
        self.main=main
        self.temp=[]
        for i in self.main:
            if i == " ":
                self.temp.append(" ")
            else:
                self.temp.append("_")
    #text template
        self.font = pygame.font.SysFont('Gill Sans', 80)
        self.text = self.font.render(' '.join(self.temp), True, black, white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (500, 600)
    #draw word
    def drawer(self):
        screen.blit(text.text,text.textRect)
#submit function
def submit(keyname,text):
    global attempt
    if keyname in text.main:
        for i in range(len(text.main)):
            if keyname==text.main[i]:
                text.temp[i]=keyname
        text.text = text.font.render(' '.join(text.temp), True, black, white)
    else:
        attempt -= 1
    if text.main == text.temp:
        return True
    else: return False



#class2
class Front(TextBox):
    def __init__(self):
        super().__init__()
        self.textRect.center = (5, 260)
    #draw letter
    def drawer(self,keyname):
        self.main=keyname
        self.text = self.font.render(self.main, True, black, white)
        screen.blit(front.text, front.textRect)

#main
#colors
white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)
#win image
win=pygame.image.load('source/win.png')
#background image
bc = pygame.image.load('source/background.jpg')
#inserting game over picture
over=pygame.image.load('source/gover.png')
#inserting hangman image
hangman = [pygame.image.load('source/0.jpg'),
    pygame.image.load('source/1.jpg'),
    pygame.image.load('source/2.jpg'),
    pygame.image.load('source/3.jpg'),
    pygame.image.load('source/4.jpg'),
    pygame.image.load('source/5.jpg'),
    pygame.image.load('source/6.jpg')
    ]
#chanse
attempt=6

#input word from user
while True:
    main = list(input("which text: ").upper())
    if len(main)<15 or len(main)<1:
        break
    else:
        print("This word is too long . Please try again: ")
#classes
text=TextBox(main)
front=Front()

keyname=''
#start game
while True:

    #background image
    screen.blit(bc, (0,0))
    text.drawer()
    for event in pygame.event.get():
        #get pressed key name
        if event.type == pygame.KEYDOWN and len(pygame.key.name(event.key))==1 and pygame.key.name(event.key).isalpha():
            keyname=pygame.key.name(event.key).upper()
        #exit when click close
        elif event.type == pygame.QUIT:
            sys.exit()
    #submit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        enter=submit(keyname,text)
        time.sleep(0.3)
        if enter==True:
            text.drawer()
            pygame.display.update()
            time.sleep(0.5)
            screen.blit(win,(75,-50))
            pygame.display.update()
            time.sleep(2)
            sys.exit()

    #picture update
    screen.blit(hangman[attempt],(475,20))
    if(attempt == 0):
        pygame.display.update()
        time.sleep(1)
        #game over image
        screen.blit(over,(100,100))
        pygame.display.update()
        time.sleep(2)
        sys.exit()

    #display letter
    screen.blit(front.font.render("qq", True, white, white),front.textRect)
    front.drawer(keyname)

    #updating screen
    pygame.display.update()
