import tkinter as tk
import random


class Minesweeper:

    def __init__(self, n, mines):

        self.n = n
        self.mines = mines
        root = tk.Tk() 
        self.field = []
        self.open = []
        self.unopened = n

        for i in range(n):
            self.field.append([])
            self.open.append([])
            for j in range(n):
                self.field[i].append(0)
                self.open[i].append(False)
        
        temp = []
        for i in range(n*n):
            temp.append(i)
        random.shuffle(temp)
        for i in range(mines):
            i = temp[i]
            self.field[i//n][i%n] = -1
        self.count_neighbors()
        

        self.buttons = []
        for i in range(n):
            self.buttons.append([])
            for j in range(n):
                b = tk.Button(root,
                    width=2,
                    height=1,
                    command= lambda i=i, j=j: self.click(i, j))
                b.grid(row=i, column=j)
                self.buttons[i].append(b)

    
    def count_neighbors(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.field[i][j] != -1:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if i+x >= 0 and i+x < self.n and j+y >= 0 and j+y < self.n and self.field[i+x][j+y] == -1:
                                self.field[i][j] += 1


    def click(self, i, j):
        if not(i>= 0 and i< self.n and j >= 0 and j < self.n):
            return
        if self.open[i][j]:
            return
        if self.field[i][j] == -1:
            self.game_over()
            return

        self.open_cell(i, j)

        if self.field[i][j] == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    self.click(i+x, y+j)


    def open_cell(self, i, j):
        self.open[i][j] = True
        self.unopened -= 1
        self.buttons[i][j]['bg'] = 'white'
        self.buttons[i][j]['fg'] = 'green'
        
        if self.field[i][j] != 0:
            self.buttons[i][j]['text'] = str(self.field[i][j])
        if self.field[i][j] == -1:
            self.buttons[i][j]['bg'] = 'red'
            self.buttons[i][j]['fg'] = 'black'

    
    def game_over(self):
        for i in range(self.n):
            for j in range(self.n):
                self.open_cell(i, j)


    def run(self):
        tk.mainloop()


Minesweeper(10, 10).run()   