import pygame
import sys

# Initialize Pygame
pygame.init()#this can be considered as starting your pygame engine 

#the comment from the first program follows here 
# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DSA Minigame: Linked List Visualization")

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
linked_list = []

class Node:#since we know node is the main man in linked list 
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.next = None

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_linked_list():#enum helps us to link 
    for i, node in enumerate(linked_list):
        pygame.draw.circle(screen, GREEN, (node.x, node.y), 20)
        draw_text(str(node.value), font, BLACK, screen, node.x - 10, node.y - 10)
        if node.next:
            pygame.draw.line(screen, RED, (node.x, node.y), (node.next.x, node.next.y), 2)

# Main Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text:
                    value = int(input_text)
                    x = 100 + len(linked_list) * 100
                    y = height // 2
                    new_node = Node(value, x, y)
                    if linked_list:
                        linked_list[-1].next = new_node
                    linked_list.append(new_node)
                    input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(WHITE)

    # Draw input box
    pygame.draw.rect(screen, BLACK, input_box, 2)
    draw_text(input_text, font, BLACK, screen, input_box.x + 5, input_box.y + 5)

    # Draw linked list
    draw_linked_list()

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
"""1)Input Handling: Users can type a number and press Enter to add a node to the linked list.
   2)Linked List Visualization: Each node is represented as a circle with its value inside, and lines are drawn to show the connections between nodes.
   3)Pygame Basics: The code uses basic Pygame functionalities like event handling, drawing shapes, and updating the display."""