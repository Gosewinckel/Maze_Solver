from cell import Cell
import time
from random import randrange

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
        self.break_walls_r(randrange(0, num_cols - 1), randrange(0, num_rows - 1))
        self.reset_cells_visited()

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
        time.sleep(0.001)

    def break_entrance_and_exit(self):
        self.matrix[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.matrix[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def break_walls_r(self, i, j):
        self.matrix[i][j].visited = True
        while True:
            temp = []
            if i > 0:
                if self.matrix[i - 1][j].visited == False:
                    temp.append([i - 1,j])
            if i < self.num_cols - 1:
                if self.matrix[i + 1][j].visited == False:
                    temp.append([i + 1, j])
            if j > 0:
                if self.matrix[i][j - 1].visited == False:
                    temp.append([i, j - 1])
            if j < self.num_rows - 1:
                if self.matrix[i][j + 1].visited == False:
                    temp.append([i, j + 1])
            if len(temp) == 0 or temp == None:
                self.draw_cell(i, j)
                return
            direc = randrange(0, len(temp))
            if i < temp[direc][0]:
                self.matrix[i][j].has_right_wall = False
                self.matrix[i + 1][j].has_left_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i + 1, j)
                self.break_walls_r(i + 1, j)
            elif i > temp[direc][0]:
                self.matrix[i][j].has_left_wall = False
                self.matrix[i - 1][j].has_right_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i - 1, j)
                self.break_walls_r(i - 1, j)
            elif j < temp[direc][1]:
                self.matrix[i][j].has_bottom_wall = False
                self.matrix[i][j + 1].has_top_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i, j + 1)
                self.break_walls_r(i, j + 1)
            elif j > temp[direc][1]:
                self.matrix[i][j].has_top_wall = False
                self.matrix[i][j - 1].has_bottom_wall = False
                self.draw_cell(i, j)
                self.draw_cell(i , j - 1)
                self.break_walls_r(i, j - 1)

    def reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.matrix[i][j].visited = False

    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate()
        self.matrix[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        directions = [[i - 1, j], [ i + 1, j], [i, j - 1], [i, j + 1]]
        walls = [self.matrix[i][j].has_left_wall, self.matrix[i][j].has_right_wall, self.matrix[i][j].has_top_wall, self.matrix[i][j].has_bottom_wall]
        for x in range(0, len(directions)):
            if (directions[x][0] >= 0 and directions[x][0] < self.num_cols) and (directions[x][1] >= 0 and directions[x][1] < self.num_rows):
                if walls[x] == False and self.matrix[directions[x][0]][directions[x][1]].visited == False:
                    self.matrix[i][j].draw_move(self.matrix[directions[x][0]][directions[x][1]])
                    path = self.solve_r(directions[x][0], directions[x][1])
                    if path == True:
                        return True
                    else:
                        self.matrix[i][j].draw_move(self.matrix[directions[x][0]][directions[x][1]], undo = True)
        return False
