import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
xy = 300
tiles = {}
spaceBtwn = 100
turn = 2

win = pygame.display.set_mode((xy, xy))
pygame.display.set_caption("Tic Tac Toe")
win.fill(WHITE)


def numberBlocks():
    tilecount = 0
    rowx = 0
    y = 0
    while y <= xy - spaceBtwn:
        for r in range(rowx, xy, spaceBtwn):
            tiles[tilecount] = Tile(rowx, y)
            rowx += spaceBtwn
            tilecount += 1
        y += spaceBtwn
        rowx = 0


def drawGrid(xy, win):
    pygame.draw.line(win, BLACK, ((1 / 3) * xy, 0), ((1 / 3) * xy, xy))
    pygame.draw.line(win, BLACK, ((2 / 3) * xy, 0), ((2 / 3) * xy, xy))
    pygame.draw.line(win, BLACK, (0, (1 / 3) * xy), (xy, (1 / 3) * xy))
    pygame.draw.line(win, BLACK, (0, (2 / 3) * xy), (xy, (2 / 3) * xy))


class Tile():
    def __init__(self, x, y):
        self.occupied = False
        self.XO = ""
        self.x = x
        self.y = y

    def draw(self):
        if self.XO == 'O':
            self.occupied = 1
            drawO(self.x, self.y, win)
        elif self.XO == "X":
            self.occupied = 2
            drawX(self.x, self.y, win)
            self.occupied = True
        else:
            pass


numberBlocks()


def yn(a, c):
    # decide if something, whether float or int is the same number
    b = a // c
    bb = a / c
    if b - bb == 0:
        return True
    else:
        return False


def askPlayerPos():
    global turn
    pos = 0
    while not 1 <= pos <= 9:
        pos = input('Your next move (1-9) : ')
        pos = int(pos)
        # translate the numbers according to my keyboard
        if pos == 7:
            pos = 1
        elif pos == 8:
            pos = 2
        elif pos == 9:
            pos = 3
        elif pos == 4:
            pos = 4
        elif pos == 5:
            pos = 5
        elif pos == 6:
            pos = 6
        elif pos == 1:
            pos = 7
        elif pos == 2:
            pos = 8
        elif pos == 3:
            pos = 9

        if tiles[pos - 1].occupied:
            continue
        else:
            if yn(turn, 2):
                tiles[pos - 1].XO = "X"
            else:
                tiles[pos - 1].XO = "O"
            turn += 1
            tiles[pos - 1].occupied = True


def drawX(x, y, win):
    pygame.draw.line(win, BLACK, (x+5, y+5), (x+95, y+95))
    pygame.draw.line(win, BLACK, (x+95, y+5), (x+5, y+95))


def drawO(x, y, win):
    pygame.draw.circle(win, BLACK, (x+50, y+50), 45, 1)


def redrawWin():
    win.fill(WHITE)
    drawGrid(xy, win)
    askPlayerPos()
    for t in tiles:
        tiles[t].draw()
        print(tiles[t].occupied)
    pygame.display.update()


def main():
    run = True
    win.fill(WHITE)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        try:
            redrawWin()
        except:
            pass


main()

