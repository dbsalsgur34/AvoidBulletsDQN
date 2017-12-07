from math import sqrt
from random import randint


class Bullet:
    def __init__(self, position, plain, width, height):
        self.position = position
        self.plain = plain
        self.width = width
        self.height = height
        self.vector = (0, 0)

        self.reset()

    def move(self):
        self.position = (self.position[0] + self.vector[0], self.position[1] + self.vector[1])
        if not (self.position[0] >= 0 and self.position[0] < 300) or not (self.position[1] >= 0 and self.position[1] < 300):
            self.reset()
        return self.collision()

    def reset(self):

        while True:
            x = randint(0, self.width)
            y = randint(0, self.height)

            if pow(x - self.plain.position[0], 2) + pow(y - self.plain.position[1], 2) >= 400:
                break

        self.position = (x, y)

        plain_position = self.plain.position
        v = (plain_position[0] - self.position[0], plain_position[1] - self.position[1])
        l = sqrt(pow(plain_position[0] - self.position[0], 2) + (pow(plain_position[1] - self.position[1], 2)))
        self.vector = (v[0] / l, v[1] / l)

    def collision(self):
        c = (self.plain.position[0] - self.position[0], self.plain.position[1] - self.position[1])

        if abs(c[0]) <= self.plain.width/2 and abs(c[1]) <= self.plain.height/2:
            return True
        else:
            return False
