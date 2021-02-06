import numpy as np
import pygame
import sys
import math
totalRow=6
totalColumn=7
circleColor=(0,0,0)#black
rectcolor=(0,0,255)#blue
player1color=(255,0,0)#red
player2color=(255,255,0)#yellow
def createBoard():
    board = np.zeros((totalRow,totalColumn))
    return board
def dropPeace(board,row,column,peace):
    board[row][column]=peace
def checkLocations(board,column):
    return board[totalRow-1][column]==0
def nextRow(board,column):
    for i in range(totalRow):
        if board[i][column]==0:
            return i
def flipBoard(board):
    print(np.flip(board,0))
def wincheck(board,peace):
    #Check horizontal locations
    for i in range(totalColumn-3):
        for j in range(totalRow):
            if board[j][i]==peace and board[j][i+i]==peace and board[j][i+2]==peace and board[j][i+3]==peace:
                return True
    #Check vertical locations
    for i in range(totalColumn):
        for j in range(totalRow-3):
            if board[j][i]==peace and board[j+1][i]==peace and board[j+2][i]==peace and board[j+3][i]==peace:
                return True
    #Check positive diagonal
    for i in range(totalColumn-3):
        for j in range(totalRow-3):
            if board[j][i]==peace and board[j+1][i+1]==peace and board[j+2][i+2]==peace and board[j+3][i+3]==peace:
                return True
    #Check negative diagonal
    for i in range(totalColumn-3):
        for j in range(3,totalRow):
            if board[j][i]==peace and board[j-1][i+1]==peace and board[j-2][i+2]==peace and board[j-3][i+3]==peace:
                return True
def drawBoard(board):
    for i in range(totalColumn):
        for j in range(totalRow):
            pygame.draw.rect(screen,rectcolor,(i*squaresize,j*squaresize+squaresize,squaresize,squaresize))
            pygame.draw.circle(screen,circleColor,(int(i*squaresize+squaresize/2),int(j*squaresize+squaresize+squaresize/2)),radius)
    for i in range(totalColumn):
        for j in range(totalRow):
            if board[j][i] == 1:
                pygame.draw.circle(screen,player1color,(int(i*squaresize+squaresize/2),height-int(j*squaresize+squaresize/2)),radius)
            elif board[j][i] == 2:
                pygame.draw.circle(screen,player2color,(int(i*squaresize+squaresize/2),height-int(j*squaresize+squaresize/2)),radius)
    pygame.display.update()

gameOver = False
board = createBoard()
turn = 1
pygame.init()
squaresize = 100
width = totalColumn * squaresize
height = totalRow * squaresize
size = (width, height)
radius = int(squaresize / 2 - 5)
screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75)
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,circleColor,(0,0,width,squaresize))
            posx=event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen,player1color,(posx,int(squaresize/2)),radius)
            else:
                pygame.draw.circle(screen,player2color,(posx,int(squaresize/2)),radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:

    #Player1 imput
            if turn==1:
                posx = event.pos[0]
                column = int(math.floor(posx/squaresize))
                turn += 1;
                if checkLocations(board,column):
                    row = nextRow(board,column)
                    dropPeace(board, row, column, 1)
                    if wincheck(board, 1):
                        label=myfont.render("Player1 win!",1,(2),player1color)
                        screen.blit(label,(40,10))
                        gameOver=True
                flipBoard(board)
                # drawBoard(board)
            else:
                posx=event.pos[0]
                column=int(math.floor(posx/squaresize))
                turn-=1;
                if checkLocations(board,column):
                    row=nextRow(board,column)
                    dropPeace(board,row,column,2)
                    if wincheck(board,2):
                        label=myfont.render("Player2 win!",1,(2),player2color)
                        screen.blit(label,(40,10))
                        gameOver=True
                flipBoard(board)
            drawBoard(board)
            if gameOver:
                    pygame.time.wait(3000)
