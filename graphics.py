import pygame as p
import conway as c
import sys
#example board with glider below
#if board is not passed into Game() instance then it will create a 60x60 2d Array as a board, initialized with a Gosper's Glider Gun
#space or right click = Pause or unpause game


board = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    ]
#by default, no board is passing into conway.Game(), thus a 60x60 board with a glider gun will be created
gs = c.Game()
p.font.init
WIDTH = LENGTH = len(gs.board) * 15
SQ_SIZE = WIDTH / len(gs.board)
numRow = numCol = len(gs.board)
MAX_FPS = 10

def main():
    p.init()
    p.display.set_caption("Conway's Game of Life")

    clock = p.time.Clock()
    screen = p.display.set_mode((WIDTH,LENGTH))

    screen.fill(p.Color("white"))
    running = True
    draw_board(screen,gs)
    paused = False
    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN and e.button == 1:
                location = p.mouse.get_pos() #gives x and y
                col = int(location[0]//SQ_SIZE)
                row = int(location[1]//SQ_SIZE)
                print(row,col)
                if gs.board[col][row] == '1':
                    gs.delete_cell(row,col)
                else:
                    gs.board[col][row] = '1'
            elif e.type  == p.MOUSEBUTTONDOWN and e.button == 3 or (e.type == p.KEYDOWN and e.key == p.K_SPACE):
                pause(paused,running,screen,gs,clock)
            else:
                pass

        draw_game_state(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def test_main(): ## call instead if you just want a picture of the board being passed in
    p.init()
    p.display.set_caption("Conway's Game of Life")

    clock = p.time.Clock()
    screen = p.display.set_mode((WIDTH,LENGTH))

    screen.fill(p.Color("white"))
    running = True
    draw_board(screen,gs)
    paused = False

    while running: 
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            else:
                continue
        draw_board(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
            

def pause(paused,running,screen,gs,clock):
    paused = True
    event = p.event.poll()

    while paused:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                paused = False
                return running
            elif e.type == p.MOUSEBUTTONDOWN and e.button == 3 or (e.type == p.KEYDOWN and e.key == p.K_SPACE):
                paused = False
                return paused
            elif e.type == p.MOUSEBUTTONDOWN and e.button == 1:
                location = p.mouse.get_pos() #gives x and y
                row = int(location[0]//SQ_SIZE)
                col = int(location[1]//SQ_SIZE)
                print(row,col)
                if gs.board[row][col] == '1':
                    gs.delete_cell(row,col)
                else:
                    gs.board[row][col] = '1'
        draw_board(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
            

def draw_board(screen, gs):
    black = (0,0,0)
    white = (255, 255, 255)
    grey = (128,128,128)
    for numRow_ in range(numRow):
        for numCol_ in range(numCol):
            if gs.board[numRow_][numCol_] == '1':
                p.draw.rect(screen,grey,p.Rect(numRow_*SQ_SIZE,numCol_*SQ_SIZE,SQ_SIZE,SQ_SIZE))
                p.draw.rect(screen,black,p.Rect(numRow_*SQ_SIZE+2,numCol_*SQ_SIZE+2,SQ_SIZE-2,SQ_SIZE-2))

            else:
                p.draw.rect(screen,grey,p.Rect(numRow_*SQ_SIZE,numCol_*SQ_SIZE,SQ_SIZE,SQ_SIZE))
                p.draw.rect(screen,white,p.Rect(numRow_*SQ_SIZE+2,numCol_*SQ_SIZE+2,SQ_SIZE-2,SQ_SIZE-2))


def draw_game_state(screen, gs):
    draw_board(screen,gs)
    gs.next_frame()



main()
