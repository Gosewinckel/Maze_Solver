from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_y, cell_size_x, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.matrix = [] 
        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        self.matrix = []
        for i in range(0, self.num_cols):
            ytemp = self.y1
            col = []
            for j in range(0, self.num_rows):
                col.append(Cell(self.x1, self.x1 + self.cell_size_x, ytemp, ytemp + self.cell_size_y, self.win))
                ytemp += self.cell_size_y
            self.matrix.append(col)
            self.x1 += self.cell_size_x
        
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        if self.win != None:
            self.matrix[i][j].draw()
        self.animate()

    def animate(self):
        if self.win != None:
            self.win.redraw()
        time.sleep(0.02)

    def break_entrance_and_exit(self):
        self.matrix[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.matrix[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
