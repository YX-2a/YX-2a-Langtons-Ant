def create_grid(w, h, bw, bh) -> tuple:
    """         create_grid is a helper function, returns a tuple with a 2d Array, Number of Columns and Number of Rows
                                            and accepts 4 required arguments
                                            
    w   :   Real Width
    h   :   Real Height
    bw  :   Width of Grid Cells 
    bh  :   Height of Grid Cells"""
    grid = []
    for i in range(0,h,bh):
        row = []
        for j in range(0,w,bw):
            row.append((j, i, bw, bh))
        grid.append(row)
    
    return (grid, len(grid[0]), len(grid))

class DIR:
    """Direction Enum"""
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Block:
    def __init__(self, x, y, width, height, color):
        """     Initialises The Block with 5 required argumets
        
        x       :   X Coordinate
        y       :   Y Coordinate
        width   :   Width
        height  :   Height
        color   :   Color"""
        self.x, self.y, self.width, self.height, self.color =  x, y, width, height, color
        self.id = -1 # Unique Integer ID
    
    def set_id(self, num) -> None:
        """Sets The ID of The Block"""
        self.id = num

class Floor(Block):
    def __init__(self, x, y, width, height):
        """     Initialises The Floor with 4 required argumets
        
        x       :   X Coordinate
        y       :   Y Coordinate
        width   :   Width
        height  :   Height"""
        super().__init__(x, y, width, height, "white")

    def flip_color(self) -> None:
        """Flips The Color From White to Black and Black to White"""
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

class Ant(Block):
    def __init__(self, x, y, width, height, color):
        """     Initialises The Ant with 5 required argumets
        
        x       :   X Coordinate
        y       :   Y Coordinate
        width   :   Width
        height  :   Height
        color   :   Color"""
        super().__init__(x, y, width, height, color)
        self.dir = DIR.RIGHT # Direction Variable
    
    def go_right(self) -> None:
        """Turns Right"""
        self.dir = (self.dir + 1)%4
    
    def go_left(self) -> None:
        """Turns Left"""
        self.dir = (self.dir - 1)%4
