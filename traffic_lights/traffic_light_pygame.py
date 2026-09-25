# Example file showing a circle moving on screen
import pygame
import time

# Class definitions
class Light:
    def __init__(self, colour, x_pos, y_pos, size):
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size

    def change(self, on_off):
        if on_off:
            new_colour = self.colour
        else:
            new_colour = "#333333"
        pygame.draw.circle(screen, new_colour, (self.x_pos,self.y_pos), self.size)

red_light = Light("#FF0000", 250, 150, 85)
amber_light = Light("#FFBF00", 250, 350, 85)
green_light = Light("#00FF00", 250, 550, 85)

light_States = (
    ((True,False,False),5),
    ((True,True,False),2),
    ((False,False,True),8),
    ((False,True,False),2)
    )

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
running = True
dt = 0

counter = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if counter >= len(light_States):
        counter = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for x in range(len(light_States[counter][0])):
        red_light.change(light_States[counter][0][0])
        amber_light.change(light_States[counter][0][1])
        green_light.change(light_States[counter][0][2])
    

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.time.delay(light_States[counter][1]*1000)

    counter += 1

pygame.quit()


