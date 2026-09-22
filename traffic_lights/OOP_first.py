import time
class Light_States:
    def __init__(self, colour, time):
        self.colour = colour
        self.time = time

lights = (
    Light_States("Red", 5),
    Light_States("Red + Amber", 2),
    Light_States("Green", 8),
    Light_States("Amber", 2),
)
counter = 0

while True:
    print(lights[counter].colour)
    time.sleep(lights[counter].time)
    counter += 1
    if counter >= len(lights):
        counter = 0
