def create_grid(w, h, bw, bh):
    grid = []
    for i in range(0,h,bh):
        row = []
        for j in range(0,w,bw):
            row.append((j, i, bw, bh))
        grid.append(row)
    
    return (grid, len(grid[0]), len(grid))

class DIR:
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Block:
    def __init__(self, x, y, width, height, color):
        self.x, self.y, self.width, self.height, self.color =  x, y, width, height, color
        self.id = -1
    
    def set_id(self, num):
        self.id = num

class Floor(Block):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "white")
    
    def flip_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

class Ant(Block):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.dir = DIR.RIGHT
    
    def go_right(self):
        self.dir = (self.dir + 1)%4
    
    def go_left(self):
        self.dir = (self.dir - 1)%4
