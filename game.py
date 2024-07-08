import pygame
import random

pygame.init()
WIDTH, HEIGHT = 500, 500
BG_COLOR = (140,140,140)
ROWS, COLS = 4, 4
size = WIDTH // ROWS
NUM_FONT = pygame.font.SysFont('comicsans', 50)
NUM_COLOR = (0, 0, 0)
LOST_FONT= pygame.font.SysFont('comicsans',70)

IMAGE_1 = pygame.image.load('1.png')
IMAGE_1 = pygame.transform.scale(IMAGE_1, (int(size), int(size)))

IMAGE_2 = pygame.image.load('2.png')
IMAGE_2 = pygame.transform.scale(IMAGE_2, (int(size), int(size)))

IMAGE_3 = pygame.image.load('3.png')
IMAGE_3 = pygame.transform.scale(IMAGE_3, (int(size), int(size)))

IMAGE_4 = pygame.image.load('4.png')
IMAGE_4 = pygame.transform.scale(IMAGE_4, (int(size), int(size)))

IMAGE_5 = pygame.image.load('5.png')
IMAGE_5 = pygame.transform.scale(IMAGE_5, (int(size), int(size)))

IMAGE_6 = pygame.image.load('6.png')
IMAGE_6 = pygame.transform.scale(IMAGE_6, (int(size), int(size)))

IMAGE_7 = pygame.image.load('7.png')
IMAGE_7 = pygame.transform.scale(IMAGE_7, (int(size), int(size)))

IMAGE_8 = pygame.image.load('8.png')
IMAGE_8 = pygame.transform.scale(IMAGE_8, (int(size), int(size)))

IMAGE_9 = pygame.image.load('9.png')
IMAGE_9 = pygame.transform.scale(IMAGE_9, (int(size), int(size)))

IMAGE_10 = pygame.image.load('10.png')
IMAGE_10 = pygame.transform.scale(IMAGE_10, (int(size), int(size)))

IMAGE_11 = pygame.image.load('11.png')
IMAGE_11 = pygame.transform.scale(IMAGE_11, (int(size), int(size)))

IMAGE_12 = pygame.image.load('12.png')
IMAGE_12 = pygame.transform.scale(IMAGE_12, (int(size), int(size)))

IMAGE_13 = pygame.image.load('13.png')
IMAGE_13 = pygame.transform.scale(IMAGE_13, (int(size), int(size)))

IMAGE_14= pygame.image.load('14.png')
IMAGE_14 = pygame.transform.scale(IMAGE_14, (int(size), int(size)))

IMAGE_15= pygame.image.load('15.png')
IMAGE_15= pygame.transform.scale(IMAGE_15, (int(size), int(size)))


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("16 Puzzle Game")

def get_neighbours(rows, cols, row, col, field):
    neighbours = []
    if row > 0 and field[row-1][col] == 0: neighbours.append((row-1, col))
    if row < rows - 1 and field[row+1][col] == 0: neighbours.append((row+1, col))
    if col > 0 and field[row][col-1] == 0: neighbours.append((row, col-1))
    if col < cols - 1 and field[row][col+1] == 0: neighbours.append((row, col+1))
    return neighbours

def create_grid(rows, cols):
    numbers = list(range(1, rows * cols))
    numbers.append(0)
    random.shuffle(numbers)
    
    field = [numbers[i*cols:(i+1)*cols] for i in range(rows)]
    
    while not is_solvable(field):
        random.shuffle(numbers)
        field = [numbers[i*cols:(i+1)*cols] for i in range(rows)]
    
    return field

def is_solvable(field):
    one_d_list = sum(field, [])
    inversions = 0
    blank_row = 0

    for i in range(len(one_d_list)):
        if one_d_list[i] == 0:
            blank_row = i // COLS
            continue
        for j in range(i + 1, len(one_d_list)):
            if one_d_list[j] != 0 and one_d_list[i] > one_d_list[j]:
                inversions += 1

    if COLS % 2 != 0:  # Odd grid width
        return inversions % 2 == 0
    else:  # Even grid width
        if (ROWS - blank_row) % 2 == 0:  # Blank on even row from bottom
            return inversions % 2 != 0
        else:  # Blank on odd row from bottom
            return inversions % 2 == 0

def get_grid_pos(mouse_pos):
    mx, my = mouse_pos
    row = int(my // size)
    col = int(mx // size)
    return row, col

def win_condition(field):
    won = False
    if(field[0][0]==1 and field[0][1]==2 and field[0][2]==3 and field[0][3]==4 and
       field[1][0]==5 and field[1][1]==6 and field[1][2]==7 and field[1][3]==8 and
       field[2][0]==9 and field[2][1]==10 and field[2][2]==11 and field[2][3]==12 and
       field[3][0]==13 and field[3][1]==14 and field[3][2]==15 and field[3][3]==0 ):
        won = True
    return won

def draw_won(win,text):
    text = LOST_FONT.render(text,1,"green")
    win.blit(text,(WIDTH/2 - text.get_width()/2 , HEIGHT/2 - text.get_width()/2))
    pygame.display.update()

def draw(win, field):
    win.fill(BG_COLOR)
    for i in range(ROWS):
        y = size * i
        for j in range(COLS):
            x = size * j
            tile = field[i][j]

            if tile==1:
                win.blit(IMAGE_1, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==2:
                win.blit(IMAGE_2, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==3:
                win.blit(IMAGE_3, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==4:
                win.blit(IMAGE_4, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==5:
                win.blit(IMAGE_5, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==6:
                win.blit(IMAGE_6, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2) 
            if tile==7:
                win.blit(IMAGE_7, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==8:
                win.blit(IMAGE_8, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==9:
                win.blit(IMAGE_9, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==10:
                win.blit(IMAGE_10, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==11:
                win.blit(IMAGE_11, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==12:
                win.blit(IMAGE_12, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==13:
                win.blit(IMAGE_13, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==14:
                win.blit(IMAGE_14, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)
            if tile==15:
                win.blit(IMAGE_15, (x, y))
                pygame.draw.rect(win,"black",(x,y,size,size),2)  
            pygame.draw.rect(win, NUM_COLOR, (x, y, size, size), 2)  # Draw grid lines
    pygame.display.update()

def main():
    run = True
    field = create_grid(ROWS, COLS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_grid_pos(pygame.mouse.get_pos())
                if row >= ROWS or col >= COLS:
                    continue
                if event.button == 1 and field[row][col] != 0:
                    neighbours = get_neighbours(ROWS, COLS, row, col, field)
                    if neighbours:
                        row_empty, col_empty = neighbours[0]
                        field[row_empty][col_empty], field[row][col] = field[row][col], field[row_empty][col_empty]
                if(win_condition(field)):
                    draw(win, field)
                    draw_won(win, "YOU WIN")
                    pygame.time.delay(5000)
                    run = False
        draw(win, field)
        
                    
        

    pygame.quit()

if __name__ == "__main__":
    main()
