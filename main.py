from tkinter import Tk
from gamescene import Game_Scene

if __name__ == "__main__":
    w = Tk()                                # INITIALISATION of Tkinter Window
    w.title("Langton's Ant Simulation")     # SETTING THE TITLE of The Tkinter Window
    
    height  =   500     #   THE HEIGHT OF THE CANVAS
    width   =   500     #   THE WIDTH OF THE CANVAS
    blk_w   =   25      #   THE WIDTH OF BLOCKS (FLOORS and ANTS)
    blk_h   =   50      #   THE HEIGHT OF BLOCKS (FLOORS and ANTS)
    speed   =   50      #   THE SPEED OF THE SIMULATION
    x_ant   =   250     #   THE X COORDINATE OF THE ANT in THE CANVAS
    y_ant   =   250     #   THE Y COORDINATE OF THE ANT in THE CANVAS
    
    obj = Game_Scene(w, height, width, blk_w, blk_h, speed, x_ant, y_ant)   #           INITIALISING THE Game_Scene
    obj.pack()                                                              #   PACKING THE Game_Scene Into The Tkinter Window


    w.mainloop() # The Main Loop