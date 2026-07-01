from tkinter import Tk
from gamescene import Game_Scene

if __name__ == "__main__":
    w = Tk()
    obj = Game_Scene(w, 750, 500, 5, 5, 5)
    obj.pack()
    w.mainloop()