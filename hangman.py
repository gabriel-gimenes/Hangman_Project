import pygame
import math
import random

# setup display
pygame.init() #Verifying if it has no errors in pygame library import
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT)) #Window size
pygame.display.set_caption("Hangman Game!") #Window title

# button variable
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(GAP+2*RADIUS)*13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP*2 + ((RADIUS*2+GAP) * (i%13))
    y = starty + ((i//13) * (GAP+RADIUS*2))
    letters.append([x,y,chr(A+i),True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('comicsans',70)

# load images
images = []
for i in range(7):
    image = pygame.image.load('hangman'+str(i)+'.png')
    images.append(image)

# game variables
hangman_status = 0
words = ['HELLO', 'DEVELOPER', 'PYTHON','SCIENCE','WEIRD']
word = words[random.randrange(len(words))]
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# setup loop game here
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE) #Display color
    
    text = TITLE_FONT.render('HANGMAN GAME',1,BLACK)
    win.blit(text,(HEIGHT/2-text.get_height()/2,20))


    # draw word
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ' '

        else:
            display_word += '_ '

    text = WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))

    # draw buttons
    for letter in letters:
        x,y,char,visible = letter
        
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3) #Ffunction(window,color_of_circle,center_pos,radius,thikiness)
            text = LETTER_FONT.render(char,1,BLACK) #format letters
            win.blit(text,(x-text.get_width()/2, y-text.get_height()/2)) #offset the position buttons

    win.blit(images[hangman_status],(150,100)) #Draw the image in specificated position
    pygame.display.update() #We need this to keep display in chosen color

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message,1,BLACK)
    win.blit(text,((WIDTH-text.get_width())/2,(HEIGHT-text.get_height())/2))        
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(FPS) #FPS limit is 60
    
    for event in pygame.event.get(): #Go through each event from pygame library
        if event.type == pygame.QUIT: #If the event is QUIT (close the window in the X), then, leave from loop
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos() #Get the xy position
            for letter in letters:
                x,y,char,visible = letter
                if visible:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(char)
                        if char not in word:
                            hangman_status += 1
    draw()
    
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
         
    if won:
        display_message('You WON!')        
        break

    if hangman_status == 6:
        display_message('You LOST!')
        break
pygame.quit()
