from math import sqrt

class Plain:
    def __init__(self, width, height, pwidth, pheight):
        self.position = (width/2, height/2)
        self.width = pwidth
        self.height = pheight

    def move(self):
        x = self.position[0] - 0.1
        y = self.position[1] - 0.1
        self.position = (x, y)