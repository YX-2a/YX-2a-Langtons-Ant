from tkinter import Canvas
from gameobjects import Floor, Ant, DIR, create_grid

class Game_Scene(Canvas):
    def __init__(self, master, height, width, bw, bh, speed, xant, yant) -> None:
        """         Initialises The Game_Scene and Accepts 8 Required Arguments 
        
        master  :   The Parent (Window, Frame etc...)
        height  :   The Height of The Game Scene
        width   :   The Width of The Game Scene
        bw      :   The Width of The Blocks
        bh      :   The Height of The Blocks
        speed   :   The Speed of The Simulation (The Lower The Faster)
        xant    :   The X Coordinate of The Ant
        yant    :   The Y Coordinate of The Ant"""

        super().__init__(master, height=height, width=width) # Initialises The Tkinter Canvas with the Master, Height and Width
        self.width, self.height, self.bw, self.bh, self.speed, self.xant, self.yant = width, height, bw, bh, speed, xant, yant
        self.grid_width, self.grid_height = 0, 0
        
        self.floor_grid = []
        grid = create_grid(self.width, self.height, self.bw, self.bh)
        self.create_floor_grid(*grid)
        self.ant = None
        self.create_ant()
        self.ant_loop()
    
    def create_floor_grid(self, grid, grid_width, grid_height) -> None:
        """Creates The Floor Grid In the Canavs with 3 required Arguments
        
        grid        :   The 2d Array of Coordinates and Dimensions
        grid_width  :   The Width of The Grid by its Units
        grid_height :   The Height of The Grid by its Units"""
        for row in grid:
            row_f = []
            for col in row:
                blk = Floor(*col)
                num = self.create_rectangle(col[0], col[1], col[0] + col[2], col[1] + col[3], fill=blk.color,outline=blk.color)
                blk.set_id(num)
                row_f.append(blk)
            self.floor_grid.append(row_f)
        self.grid_width, self.grid_height = grid_width, grid_height

    def create_ant(self):
        """Creates The Ant In The Coordinates Specified at Initiation of the class (self.xant, self.yant)"""
        self.ant = Ant(x=self.xant, y=self.yant, height=self.bh, width=self.bw, color="red")
        num = self.create_rectangle(self.ant.x, self.ant.y, self.ant.x + self.ant.height, self.ant.y + self.ant.height, fill=self.ant.color,outline=self.ant.color)
        self.ant.set_id(num)

    def ant_loop(self):
        """The Loop that applies Simulation Rules at an interval (self.speed)"""
        ant_grid_coords = [(self.ant.x//self.ant.width)     %   self.grid_width
                           ,(self.ant.y//self.ant.height)   %   self.grid_height
                           ] 
        ant_block = self.floor_grid[ant_grid_coords[1]][ant_grid_coords[0]]
        if ant_block.color == "white":
            self.ant.go_right()
        else:
            self.ant.go_left()

        ant_block.flip_color()
        self.itemconfig(ant_block.id, outline=ant_block.color, fill=ant_block.color)

        next_coords = [self.ant.x, self.ant.y]

        match self.ant.dir:
            case DIR.UP:    next_coords[1] = (next_coords[1] - self.ant.height) %   self.height
            case DIR.DOWN:  next_coords[1] = (next_coords[1] + self.ant.height) %   self.height
            case DIR.RIGHT: next_coords[0] = (next_coords[0] + self.ant.width)  %   self.width
            case DIR.LEFT:  next_coords[0] = (next_coords[0] - self.ant.width)  %   self.width
        
        self.coords (self.ant.id, next_coords[0], next_coords[1], next_coords[0] + self.ant.width, next_coords[1] + self.ant.height)
        self.ant.x = next_coords[0]
        self.ant.y = next_coords[1]

        self.after(self.speed,self.ant_loop)
