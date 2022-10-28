import os
from time import sleep
import random as rnd

# sq_n = 0 | null | dead
# sq_f = 1 | full | alive

sq_n1 = '□'
sq_f1 = '■'

sq_n2 = '░░'
sq_f2 = '██'

sq_n3 = ' 0'
sq_f3 = ' 1'

sq_null = sq_n2
sq_full = sq_f2

cell_list = []

current_generation = 0

game_field = 10,10
x_field = game_field[0]
y_field = game_field[1]

clear = lambda: os.system('cls')
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

class Cell:

    def __init__(self,position=0, status=0):
        self.stat = status
        self.pos = position
        self.symb = sq_null if self.stat is 0 else sq_full

    def __str__(self):
        return self.symb

    def change_stat(self,new_status):
        self.stat = new_status
        self.symb = sq_null if self.stat is 0 else sq_full

    def new_gen(self):
        pass

def new_gen():
    for cell in cell_list:
        cell.new_gen()

def generate_status(percent:int):
    '''The percentage argument means the chance that the cell will be 'alive' '''

    st, = rnd.choices((0, 1), (100 - percent, percent))
    return st

def generate_initial_table(percent_of_alive:int):
    global cell_list
    cell_list = []
    for i in range(1,101):
        cell = Cell(position=i, status=generate_status(percent_of_alive))
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

def table_inf():
    l = []
    for i in cell_list:
        l.append(i.stat)

    alive_cells = sum(l)
    dead_cells = 100-alive_cells
    inf_dict = {'alive_cells': alive_cells, 'dead_cells': dead_cells, 'current_generation': current_generation}

    return inf_dict

def print_inf():
    for i in table_inf():
        print(f'{i} - {table_inf().get(i)}')


def main():
    global current_generation

    print(update_table())
    print_inf()
    new_gen()
    current_generation += 1

if __name__ == '__main__':
    generate_initial_table(30)
    for i in range(10):
        main()
        sleep(0.3)
        clear()
        print()
