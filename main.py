import os
from time import sleep as sl

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
0  1  2  3  4 5 6 7 8 9 10
11 12 13 14 ....








'''

cell_list = []

class Cell:

    def __init__(self,position=0,status = 0):
        self.stat = status
        self.pos = position
        self.symb = sq_null if self.stat is False else sq_full

    def change_stat(self,new_status):
        self.stat = new_status
        self.symb = sq_null if self.stat is False else sq_full

    def gen(self):
        pass

for i in range(100):
    cell = Cell(position=i)
    cell_list.append(cell)

print(cell_list)

# for i in range(10):
#     for cell in cell_list[i:i*10]:
#         print(cell.symb,end=' ')
#     print('')