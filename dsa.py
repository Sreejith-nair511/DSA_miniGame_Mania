import pygame
#the module that we using boiis
import sys
#imp for sys looping and display 

# Initialize Pygame
pygame.init()

# Screen dimensions,this will be our game window 
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DSA Minigame: Bubble Sort Visualization(Arrays)")

# Colors (feel free to change it)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font,again use anything you like 
font = pygame.font.SysFont(None, 36)

# Input box,for user input
input_box = pygame.Rect(100, 50, 140, 32)
input_text = ''
numbers = []

# Sorting variables,sort logic starts here 
sorting = False
i = 0
j = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def bubble_sort_step():#general bubb sort logic
    global i, j, numbers, sorting
    if i < len(numbers) - 1:
        if j < len(numbers) - 1 - i:
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            j += 1
        else:
            j = 0
            i += 1
    else:
        sorting = False

# Main loop
running = True
while running:#the main game loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text:
                    numbers = list(map(int, input_text.split()))
                    input_text = ''
                    sorting = True
                    i = 0
                    j = 0
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(WHITE)

    # Draw input box
    pygame.draw.rect(screen, BLACK, input_box, 2)
    draw_text(input_text, font, BLACK, screen, input_box.x + 5, input_box.y + 5)

    # Draw numbers
    for idx, num in enumerate(numbers):
        pygame.draw.rect(screen, GREEN if not sorting else RED, (100 + idx * 50, 200, 40, num * 5))

    if sorting:
        bubble_sort_step()

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
#addtional comments
"""1)Input Handling: Users can type numbers separated by spaces and press Enter to start sorting.
   2)Bubble Sort Visualization: The numbers are visualized as bars, and the sorting process is animated.
   3)Pygame Basics: The code uses basic Pygame functionalities like event handling, drawing shapes, and updating the display."""