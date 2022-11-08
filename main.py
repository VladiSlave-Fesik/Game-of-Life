import os
from time import sleep
import random as rnd
import pyfiglet as fg

# sq_n = 0 | null | dead
# sq_f = 1 | full | alive

sq_n1 = '□'
sq_f1 = '■'
sq_n2 = '░░'
sq_f2 = '██'
sq_n3 = ' 0'
sq_f3 = ' 1'
sq_n4 = '[□]'
sq_f4 = '[■]'
sq_null = sq_n2
sq_full = sq_f2

line_sep1 = '\n'
line_sep2 = '\n\n'
line_sep = line_sep2

cell_sep1 = ' '
cell_sep2 = '  '
cell_sep = cell_sep2

cell_list = []
current_generation = 0

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

glider = [36,46,56,55,44]

exit_code = None
exit_code_dict = {0:'The game is stopped due to the fact that the number of live cells = 0','∞':'Game paused because the table has not changed from the previous generation'}

settings_dict = {}

class Cell:

    def __init__(self,position=1, status=0):
        self.stat = status
        self.pos = position
        self.symb = sq_null if self.stat == 0 else sq_full
        self.next_stat = None

    def __str__(self):
        return self.symb

    def change_stat(self):
        if self.next_stat is not None:
            self.stat = self.next_stat
            self.next_stat = None
        self.symb = sq_null if self.stat == 0 else sq_full

    def new_gen(self,d):
        self.ls = []

        try:
            self.up = 'up' if d.get(str(self.pos - 10)).stat == 1 else False
            if self.up is not False:
                self.ls.append(self.up)
        except:
            pass
        try:
            self.down = 'down' if d.get(str(self.pos + 10)).stat == 1 else False
            if self.down is not False:
                self.ls.append(self.down)
        except:
            pass
        try:
            self.left = 'left' if d.get(str(self.pos - 1)).stat == 1 else False
            if self.left is not False:
                self.ls.append(self.left)
        except:
            pass
        try:
            self.right = 'right' if d.get(str(self.pos + 1)).stat == 1 else False
            if self.right is not False:
                self.ls.append(self.right)
        except:
            pass
        try:
            self.up_left = 'up_left' if d.get(str(self.pos - 11)).stat == 1 else False
            if self.up_left is not False:
                self.ls.append(self.up_left)
        except:
            pass
        try:
            self.down_left = 'down_left' if d.get(str(self.pos + 9)).stat == 1 else False
            if self.down_left is not False:
                self.ls.append(self.down_left)
        except:
            pass
        try:
            self.up_right = 'up_right' if d.get(str(self.pos - 9)).stat == 1 else False
            if self.up_right is not False:
                self.ls.append(self.up_right)
        except:
            pass
        try:
            self.down_right = 'down_right' if d.get(str(self.pos + 11)).stat == 1 else False
            if self.down_right is not False:
                self.ls.append(self.down_right)
        except:
            pass


        finally:
            if self.stat == 0 and len(self.ls) == 3:
                self.next_stat = 1

            elif self.stat == 1:
                if len(self.ls) in (2,3):
                    self.next_stat = 1

                elif len(self.ls) > 3 or len(self.ls) < 2:
                    self.next_stat = 0


def new_gen(d):
    for cell in cell_list:
        cell.new_gen(d)

def change_stats():
    for cell in cell_list:
        cell.change_stat()

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

def generate_prepared_table(pre):
    global cell_list
    cell_list = []
    for i in range(1,101):
        if i in pre:
            cell = Cell(position=i, status=1)
        else:
            cell = Cell(position=i, status= 0)
        cell_list.append(cell)

def update_table():
    i = 1
    string = ''''''
    for cell in cell_list:
        if i % 10 == 0:
            string += cell.__str__() + cell_sep
            string += line_sep
        else:
            string += cell.__str__() + cell_sep
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
    global table
    print(table:=update_table())
    print_inf()
    print('')
    current_generation += 1

def settings_menu():
    global settings_dict
    global random_ch
    print('Input the settings, you can also skip to not change or select an already preset\n')
    print('''
        Enter dead and alive cell symbol through a space:
        □
        ■

        ░░ - standard
        ██ - standard

        0
        1

        [□]
        [■]''')

    alive_cell = input('\tAlive cell: ')
    dead_cell = input('\tDead cell: ')

    cell_separator = input('''
    Cell separator:
    cell_sep1 = ' ' 
    cell_sep2 = '  ' - standard
    >>> ''')

    line_separator = input('''
    Line separator: 
    line_sep1 = '\\n'
    line_sep2 = '\\n\\n' - standard
    >>> ''')

    mode = input('''
    Game mode:
    Random - standard
    Glider
    Input
    >>> ''')

    if mode.lower() == 'random':
        random_ch = int(input('Print chance of alive cell: '))

    tbs = input('''
    Table per second | tbs  3 - standard
    max - no limit
    0 - after each generation, input is expected
    your int
    >>> ''')

    clear_or_not = input('''
    Whether to clear the console from the table? [y/n]
    >>> ''')

    settings_dict = {'sq_null':dead_cell,'sq_full':alive_cell,'line_sep':line_separator,'cell_sep':cell_separator,'mode':mode,'tbs':tbs,'cln':clear_or_not}


if __name__ == '__main__':

    print(fg.Figlet(font='slant',width=300).renderText('Game of Life'))
    ans = input('''
    This is a console version of the game of life written in Python.
    Would you like to change settings?
    [start/settings] >>> ''')

    while ans.lower() not in ['settings','start']:
        ans = input('[start/settings] >>> ')
        print()

    if ans.lower() == 'start':
        if ans == 'start':
            generate_initial_table(40)
            # generate_prepared_table(pre_table)
            d = create_dict_num_cell()
            main(d)
            clear()
            while True:

                last_table = table

                new_gen(d)
                change_stats()
                main(d)

                if table_inf().get('alive_cells') == 0:
                    exit_code = 0
                    break

                if last_table == table:
                    exit_code = '∞'
                    break

                sleep(round(1 / 3, 5))

                clear()

    elif ans.lower() == 'settings':
        settings_menu()

        sq_null = settings_dict['sq_null'] if settings_dict['sq_null'] else sq_n2
        sq_full = settings_dict['sq_full'] if settings_dict['sq_full'] else sq_f2

        if len(settings_dict['line_sep']) == 0:
            line_sep = '\n\n'
        else:
            line_sep = settings_dict['line_sep'].replace(r'\n','\n')

        cell_sep = settings_dict['cell_sep'] if settings_dict['cell_sep'] else '  '


        if settings_dict['mode'].lower() == 'glider':
            generate_prepared_table(glider)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            while True:

                last_table = table

                new_gen(d)
                change_stats()
                main(d)

                if table_inf().get('alive_cells') == 0:
                    exit_code = 0
                    break

                if last_table == table:
                    exit_code = '∞'
                    break

                if len(settings_dict['tbs']) == 0:
                    sleep(round(1 / 3, 5))

                elif settings_dict['tbs'].lower() == 'max':
                    pass

                elif settings_dict['tbs'] == '0':
                    input('enter >>> ')

                else:
                    sleep(round(1 / int(settings_dict['tbs']), 5))

                if settings_dict['cln'].lower() == 'y':
                    clear()

        elif settings_dict['mode'].lower() == 'random':
            generate_initial_table(random_ch)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            while True:

                last_table = table

                new_gen(d)
                change_stats()
                main(d)

                if table_inf().get('alive_cells') == 0:
                    exit_code = 0
                    break

                if last_table == table:
                    exit_code = '∞'
                    break

                if len(settings_dict['tbs']) == 0:
                    sleep(round(1 / 3, 5))

                elif settings_dict['tbs'].lower() == 'max':
                    pass

                elif settings_dict['tbs'] == '0':
                    input('enter >>> ')

                else:
                    sleep(round(1 / int(settings_dict['tbs']), 5))

                if settings_dict['cln'].lower() == 'y':
                    clear()

        elif settings_dict['mode'].lower() == 'input':
            print('Enter, separated by a space, the coordinates of those cells that must be filled')
            print(coord_table)

            pre_table = (map(int,input('>>> ').split()))

            generate_prepared_table(pre_table)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            while True:

                last_table = table

                if table_inf().get('alive_cells') == 0:
                    exit_code = 0
                    break

                new_gen(d)
                change_stats()
                main(d)

                if last_table == table:
                    exit_code = '∞'
                    break

                if len(settings_dict['tbs']) == 0:
                    sleep(round(1 / 3, 5))

                elif settings_dict['tbs'].lower() == 'max':
                    pass

                elif settings_dict['tbs'] == '0':
                    input('enter >>> ')

                else:
                    sleep(round(1 / int(settings_dict['tbs']), 5))

                if settings_dict['cln'].lower() == 'y':
                    clear()

print(exit_code_dict[exit_code])

input('>>>')