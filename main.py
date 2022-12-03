try:
    from time import sleep, time, process_time
    import pyfiglet as fg
    from record import *
    import os
    import clr
    clr.AddReference(os.getcwd()+'\\next_gen.dll')

except ImportError as error:
    print('Import error. It ended earlier than it should have...')
    print(error)
    input()

# sq_n = 0 | null | dead
# sq_f = 1 | full | alive

end_1 = 'Everything ends . Sooner or later.'
end_2 = 'Everything begins and ends.'

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
1  *  *  *  *  *  *  *  *  *  *
2  *  *  *  *  *  *  *  *  *  *
3  *  *  *  *  *  *  *  *  *  *
4  *  *  *  *  *  *  *  *  *  *
5  *  *  *  *  *  *  *  *  *  *
6  *  *  *  *  *  *  *  *  *  *
7  *  *  *  *  *  *  *  *  *  *
8  *  *  *  *  *  *  *  *  *  *
9  *  *  *  *  *  *  *  *  *  *
10 *  *  *  *  *  *  *  *  *  *
'''

num_x = 10
num_y = 10

glider = ['6;3', '6;4', '6;5', '5;5', '4;4']

exit_code = None
exit_code_dict = {0: 'The game is stopped due to the fact that the number of live cells = 0',
                  '∞': 'Game paused because the table has not changed from the previous generation',
                  'loop': 'The game has stopped due to being caught in a loop'}

settings_dict = {}


class Cell:

    def __init__(self, position='1;1', status=0):
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

    def new_gen(self, d: dict):
        self.ls = []
        self.n_pos = self.pos.split(';')
        self.n_pos = list(map(int, self.n_pos))
        try:
            self.up = 'up' if d.get(f'{self.n_pos[0]};{self.n_pos[1] - 1}').stat == 1 else False
            if self.up is not False:
                self.ls.append(self.up)
        except:
            pass
        try:
            self.down = 'down' if d.get(f'{self.n_pos[0]};{self.n_pos[1] + 1}').stat == 1 else False
            if self.down is not False:
                self.ls.append(self.down)
        except:
            pass
        try:
            self.left = 'left' if d.get(f'{self.n_pos[0] - 1};{self.n_pos[1]}').stat == 1 else False
            if self.left is not False:
                self.ls.append(self.left)
        except:
            pass
        try:
            self.right = 'right' if d.get(f'{self.n_pos[0] + 1};{self.n_pos[1]}').stat == 1 else False
            if self.right is not False:
                self.ls.append(self.right)
        except:
            pass
        try:
            self.up_left = 'up_left' if d.get(f'{self.n_pos[0] - 1};{self.n_pos[1] - 1}').stat == 1 else False
            if self.up_left is not False:
                self.ls.append(self.up_left)
        except:
            pass
        try:
            self.down_left = 'down_left' if d.get(f'{self.n_pos[0] - 1};{self.n_pos[1] + 1}').stat == 1 else False
            if self.down_left is not False:
                self.ls.append(self.down_left)
        except:
            pass
        try:
            self.up_right = 'up_right' if d.get(f'{self.n_pos[0] + 1};{self.n_pos[1] - 1}').stat == 1 else False
            if self.up_right is not False:
                self.ls.append(self.up_right)
        except:
            pass
        try:
            self.down_right = 'down_right' if d.get(f'{self.n_pos[0] + 1};{self.n_pos[1] + 1}').stat == 1 else False
            if self.down_right is not False:
                self.ls.append(self.down_right)
        except:
            pass


        finally:

            if self.stat == 0 and len(self.ls) == 3:
                self.next_stat = 1

            elif self.stat == 1:
                if len(self.ls) in (2, 3):
                    self.next_stat = 1

                elif len(self.ls) > 3 or len(self.ls) < 2:
                    self.next_stat = 0


def new_gen(d):
    for cell in cell_list:
        cell.new_gen(d)


def change_stats():
    for cell in cell_list:
        cell.change_stat()


def generate_status(percent: int):
    '''The percentage argument means the chance that the cell will be 'alive' '''

    st, = rnd.choices((0, 1), (100 - percent, percent))
    return st


def generate_initial_table(percent_of_alive: int):
    global cell_list
    cell_list = []
    for y in range(1, num_y + 1):
        for x in range(1, num_x + 1):
            cell = Cell(position=f'{x};{y}', status=generate_status(percent_of_alive))
            cell_list.append(cell)


def generate_prepared_table(pre):
    global cell_list
    cell_list = []
    for y in range(1, num_y + 1):
        for x in range(1, num_x + 1):
            if f'{x};{y}' in pre:
                cell = Cell(position=f'{x};{y}', status=1)
            else:
                cell = Cell(position=f'{x};{y}', status=0)
            cell_list.append(cell)


def update_table():
    global col1, col2

    i = 0
    string = ''''''
    for y in range(1, num_y + 1):
        for x in range(1, num_x + 1):
            cell = cell_list[i]
            string += cell.__str__() + cell_sep
            i += 1
        string += line_sep
    return string


def table_inf():
    l = []
    for i in cell_list:
        l.append(i.stat)

    alive_cells = sum(l)
    dead_cells = num_x * num_y - alive_cells
    inf_dict = {'alive_cells': alive_cells, 'dead_cells': dead_cells, 'current_generation': current_generation}

    return inf_dict


def print_inf():
    for i in table_inf():
        print(f'{i} - {table_inf().get(i)}')


def create_dict_num_cell():
    d = {}
    i = 0
    for y in range(1, num_y + 1):
        for x in range(1, num_x + 1):
            d[f'{x};{y}'] = cell_list[i]
            i += 1
    return d


def main(d):
    global current_generation
    global table
    print(table := update_table())
    print_inf()
    current_generation += 1


def life():
    global table, last_table, exit_code, mean_tps

    while True:

        generation_time = process_time()

        try:
            second_table = last_table
        except:
            pass
        last_table = table

        new_gen(d)
        change_stats()
        main(d)
        try:
            print(f'tps:{round(1 / (time() - start), 2)}\n')
        except:
            pass

        if table_inf().get('alive_cells') == 0:
            exit_code = 0
            if settings_dict['rec'] == 'y':
                resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)
            break

        if last_table == table:
            exit_code = '∞'
            if settings_dict['rec'] == 'y':
                resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)
            break
        try:
            if second_table == table:
                exit_code = 'loop'
                if settings_dict['rec'] == 'y':
                    resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width,
                                 height=height)
                break
        except:
            pass

        start = time()

        if len(settings_dict['tps']) == 0:
            if float(process_time()-generation_time) >= 0.3:
                pass
            else:
                sleep(1/int(settings_dict['tps']))


        elif settings_dict['tps'].lower() == 'max':
            pass

        elif settings_dict['tps'] == '0':
            input('enter >>> ')

        else:
            if float(process_time()-generation_time) >= (1 / int(settings_dict['tps'])):
                pass
            else:
                sleep(1/int(settings_dict['tps']))

        if settings_dict['cln'].lower() == 'y':
            clear()

        if settings_dict['rec'] == 'y':
            resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)

    mean_tps = current_generation / (time() - gen_start)


def settings_menu():
    global settings_dict
    global random_ch
    global num_x, num_y
    global width, height
    global col1, col2

    print(
        'Input the settings, you can also skip to not change or copy and input an already preset\nFor correct recording, do not change: cell signs, cell separator, line separator')
    print('Standard - 10,10. Skip not to change.')
    num_x_inp = input('Cells in a row (x):')
    num_y_inp = input('Cells in a column (y):')

    num_x = 10 if not num_x_inp else int(num_x_inp)
    num_y = 10 if not num_y_inp else int(num_y_inp)

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
        random_ch = int(input('Input a chance of alive cell: '))

    tps = input('''
    Table per second | tps  3 - standard
    max - no limit
    0 - after each generation, input is expected
    your int
    >>> ''')

    clear_or_not = input('''
    Whether to clear the console from the table? [y/n]
    >>> ''')

    rec = input('''
    Record game? [y/n]
    >>> ''')

    if rec == 'y':
        width = int(input('Width of frame:'))
        height = int(input('Height of frame:'))

    settings_dict = {'sq_null': dead_cell, 'sq_full': alive_cell, 'line_sep': line_separator,
                     'cell_sep': cell_separator, 'mode': mode, 'tps': tps, 'cln': clear_or_not, 'rec': rec}


if __name__ == '__main__':

    if 'frames' not in os.listdir(os.getcwd()):
        os.mkdir('frames')

    if 'movie' not in os.listdir(os.getcwd()):
        os.mkdir('movie')

    print(fg.Figlet(font='slant', width=300).renderText('Game of Life'))
    ans = input('''
    This is a console version of the game of life written in Python.
    Would you like to change settings?
    [start/settings] >>> ''')

    while ans.lower() not in ['settings', 'start']:
        ans = input('[start/settings] >>> ')
        print()

    if ans.lower() == 'start':
        gen_start = time()

        generate_initial_table(40)
        d = create_dict_num_cell()
        main(d)
        while True:
            clear()
            eng_start = time()
            try:
                second_table = last_table
            except:
                pass
            last_table = table

            new_gen(d)
            change_stats()
            main(d)
            try:
                print(f'tps:{round(1 / (time() - start), 2)}\n')
            except:
                pass
            start = time()
            if table_inf().get('alive_cells') == 0:
                exit_code = 0
                break

            if last_table == table:
                exit_code = '∞'
                break

            try:
                if second_table == table:
                    exit_code = 'loop'
                    break
            except:
                pass
            eng_end = time()
            sleep((1 / 3) - (eng_end - eng_start))

        mean_tps = current_generation / (time() - gen_start)


    elif ans.lower() == 'settings':
        settings_menu()

        sq_null = settings_dict['sq_null'] if settings_dict['sq_null'] else sq_n2
        sq_full = settings_dict['sq_full'] if settings_dict['sq_full'] else sq_f2

        if len(settings_dict['line_sep']) == 0:
            line_sep = '\n\n'
        else:
            line_sep = settings_dict['line_sep'].replace(r'\n', '\n')

        cell_sep = settings_dict['cell_sep'] if settings_dict['cell_sep'] else '  '

        if settings_dict['mode'].lower() == 'glider':
            gen_start = time()
            generate_prepared_table(glider)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            if settings_dict['rec'] == 'y':
                resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)

            life()

        elif settings_dict['mode'].lower() == 'random':
            gen_start = time()
            generate_initial_table(random_ch)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            if settings_dict['rec'] == 'y':
                resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)

            life()

        elif settings_dict['mode'].lower() == 'input':
            print(
                'Enter, separated by a space, the coordinates of those cells that must be filled, example - 1;1 10;5 7;3')
            print(coord_table)

            pre_table = input('>>> ').split()
            gen_start = time()
            generate_prepared_table(pre_table)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            if settings_dict['rec'] == 'y':
                resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)

            life()

        else:
            gen_start = time()
            generate_initial_table(40)
            d = create_dict_num_cell()
            main(d)
            if settings_dict['cln'].lower() == 'y':
                clear()
            if settings_dict['rec'] == 'y':
                resize_image(create_img(table, x=num_x, y=num_y), str(current_generation), width=width, height=height)

            life()

print(exit_code_dict[exit_code], '\n')
print(f'Mean tps: {round(mean_tps, 2)}')
try:
    if settings_dict['rec'] == 'y':
        fps = int(input('Enter the frame rate for the video: '))
        create_video(fps=fps)
        from record import name

        print(f'Name of record - {name}.mp4')
        delete_images()
except:
    pass
sleep(0.5)
print(fg.Figlet(font='slant', width=300).renderText(end_1))

input('Press Enter to pay respects to dead cells...')
