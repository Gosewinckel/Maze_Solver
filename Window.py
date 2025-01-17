from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close())

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        running = True
        while running == True:
            self.redraw()

    def close(self):
        self.running == False 
    
    def draw_line(self, Line, fill_colour):
        Line.draw(self.canvas, fill_colour)