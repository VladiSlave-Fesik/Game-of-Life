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

    def __init__(self,position=1, status=0):
        self.stat = status
        self.pos = position
        self.symb = sq_null if self.stat is 0 else sq_full

    def __str__(self):
        return self.symb

    def change_stat(self):
        self.stat = 1 if self.stat == 0 else 0
        self.symb = sq_null if self.stat is 0 else sq_full

    def new_gen(self,d):
        self.ls = []

        try:
            self.up = True if d.get(str(self.pos-10)) else False
            if self.up is True:
                self.ls.append(self.up)
        except:
            pass
        try:
            self.down = True if d.get(str(self.pos + 10)) else False
            if self.down is True:
                self.ls.append(self.down)
        except:
            pass
        try:
            self.left = True if d.get(str(self.pos - 1)) else False
            if self.left is True:
                self.ls.append(self.left)
        except:
            pass
        try:
            self.right = True if d.get(str(self.pos + 1)) else False
            if self.right is True:
                self.ls.append(self.right)
        except:
            pass
        try:
            self.up_left = True if d.get(str(self.pos - 11)) else False
            if self.up_left is True:
                self.ls.append(self.up_left)
        except:
            pass
        try:
            self.down_left = True if d.get(str(self.pos + 9)) else False
            if self.down_left is True:
                self.ls.append(self.down_left)
        except:
            pass
        try:
            self.up_right = True if d.get(str(self.pos - 9)) else False
            if self.up_right is True:
                self.ls.append(self.up_right)
        except:
            pass
        try:
            self.down_right = True if d.get(str(self.pos + 11)) else False
            if self.down_right is True:
                self.ls.append(self.down_right)
        except:
            pass


        finally:
            if self.stat == 0:
                if len(self.ls) == 3:
                    self.change_stat()
                    print('da')

            elif self.stat == 1:
                if len(self.ls) in (2,3):
                    pass
                elif len(self.ls) > 3 or len(self.ls) < 2:
                    self.change_stat()
                    print('net')


def new_gen(d):
    for cell in cell_list:
        cell.new_gen(d)

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

def create_dict_num_cell():
    d = {}
    i = 1
    for cell in cell_list:
        d[str(i)] = cell
        i += 1
    return d

def main(d):
    global current_generation

    print(update_table())
    print_inf()
    print('')
    new_gen(d)
    current_generation += 1

# if __name__ == '__main__':
#     generate_initial_table(30)
#     d = create_dict_num_cell()
#     for i in range(1):
#         if table_inf().get('dead_cells') == 0:
#             break
#         main()
#         sleep(0.3)
#         clear()

generate_initial_table(50)
d = create_dict_num_cell()
main(d)

main(d)