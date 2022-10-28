import os
from time import sleep as sl
import random as rnd

clear = lambda: os.system('cls')

sq_null1 = '□'
sq_full1 = '■'

sq_null = '░░'
sq_full = '██'

# sq_n = 0
# sq_f = 1

game_field = 10,10
x_field = game_field[0]
y_field = game_field[1]

table = '''

'''
game_table = '''

'''

coord_table = '''
1  2  3  4  5  6  7  8  9  10 
11 12 13 14 15 16 17 18 19 20 
21 22 23 24 25 26 27 28 29 30 
31 32 33 34 35 36 37 38 39 40 
41 42 43 44 45 46 47 48 49 50 
51 52 53 54 55 56 57 58 59 60 
61 62 63 64 65 66 67 68 69 70 
71 72 73 74 75 76 77 78 79 80 
81 82 83 84 85 86 87 88 89 90 
91 92 93 94 95 96 97 98 99 100 
'''

cell_list = []

class Cell:

    def __init__(self,position=0,status = 0):
        self.stat = status
        self.pos = position
        self.symb = sq_null if self.stat is False else sq_full

    def __str__(self):
        return self.symb

    def change_stat(self,new_status):
        self.stat = new_status
        self.symb = sq_null if self.stat is False else sq_full

    def new_gen(self):
        pass

def generate_initial_table():
    for i in range(1,101):
        cell = Cell(position=i)
        cell_list.append(cell)


def update_table():
    i = 1
    string = ''''''
    for cell in cell_list:
        if i % 10 == 0:
            string += cell.__str__() + ' '
            string += '\n'
        else:
            string += cell.__str__() + ' '
        i += 1
    return string

