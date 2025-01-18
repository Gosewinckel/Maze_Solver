from Window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, x1, x2, y1, y2, win = None , visited = False, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
        self.visited = visited
        self.top_left = Point(x1, y1)
        self.top_right = Point(x2, y1)
        self.bottom_left = Point(x1, y2)
        self.bottom_right = Point(x2, y2)

    def draw(self):
        if self.has_left_wall == True:
            left_wall = Line(self.top_left, self.bottom_left)
            left_wall.draw(self.win.canvas, "black")
        elif self.has_left_wall == False:
            left_wall = Line(self.top_left, self.bottom_left)
            left_wall.draw(self.win.canvas, "white")
        if self.has_right_wall == True:
            right_wall = Line(self.top_right, self.bottom_right)
            right_wall.draw(self.win.canvas, "black")
        elif self.has_right_wall == False:
            right_wall = Line(self.top_right, self.bottom_right)
            right_wall.draw(self.win.canvas, "white")
        if self.has_top_wall == True:
            top_wall = Line(self.top_left, self.top_right)
            top_wall.draw(self.win.canvas, "black")
        elif self.has_top_wall == False:
            top_wall = Line(self.top_left, self.top_right)
            top_wall.draw(self.win.canvas, "white")
        if self.has_bottom_wall == True:
            bottom_wall = Line(self.bottom_left, self.bottom_right)
            bottom_wall.draw(self.win.canvas, "black")
        elif self.has_bottom_wall == False:
            bottom_wall = Line(self.bottom_left, self.bottom_right)
            bottom_wall.draw(self.win.canvas, "white")

    def draw_move(self, to_cell, undo = False):
        center1 = Point(self.x1 + (self.x2 - self.x1)/2, self.y1 + (self.y2 - self.y1)/2)
        center2 = Point(to_cell.x1 + (to_cell.x2 - to_cell.x1)/2, to_cell.y1 + (to_cell.y2 - to_cell.y1)/2)
        if undo == False:
            move = Line(center1, center2)
            move.draw(self.win.canvas, "red")
        else:
            move = Line(center1, center2)
            move.draw(self.win.canvas, "grey")