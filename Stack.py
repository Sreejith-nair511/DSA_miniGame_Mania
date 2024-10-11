import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DSA Minigame: Stack Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Input box
input_box = pygame.Rect(100, 50, 140, 32)
input_text = ''
stack = []

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_stack():
    for i, value in enumerate(stack):
        pygame.draw.rect(screen, GREEN, (350, 500 - i * 50, 100, 40))
        draw_text(str(value), font, BLACK, screen, 375, 510 - i * 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text:
                    stack.append(int(input_text))
                    input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_p:
                if stack:
                    stack.pop()
            else:
                input_text += event.unicode

    screen.fill(WHITE)

    # Draw input box
    pygame.draw.rect(screen, BLACK, input_box, 2)
    draw_text(input_text, font, BLACK, screen, input_box.x + 5, input_box.y + 5)

    # Draw stack
    draw_stack()

    pygame.display.flip()
    pygame.time.Clock().tick(30)#this is for your error outdation timing and loop timings 

pygame.quit()
sys.exit()
"""input Handling: Users can type a number and press Enter to push it onto the stack. Pressing ‘p’ will pop the top element from the stack.
Stack Visualization: Each element in the stack is represented as a rectangle, and the stack grows upwards as elements are added.
Pygame Basics: The code uses basic Pygame functionalities like event handling, drawing shapes, and updating the display."""