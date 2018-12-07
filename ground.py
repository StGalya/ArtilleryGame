import random


class Ground:
    def __init__(self, canv):
        self.canvas = canv
        self.coords = []
        self.coord = 0

    def draw(self):
        h = random.randint(250, 650)
        for x in range(1200):
            self.coord = (x, h)
            self.coords.append(self.coord)
            self.canvas.create_line(x, 700, x, h, width=7, fill='green')
            if h > 670:
                i = random.randint(-25, 0)
            elif 100 <= h <= 670:
                i = random.randint(-5, 5)
            elif h < 80:
                i = random.randint(0, 25)
            h = h + i
