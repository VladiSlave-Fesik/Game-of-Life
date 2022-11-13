import pyfiglet as fg
from PIL import Image, ImageFont, ImageDraw
import os
import moviepy.video.io.ImageSequenceClip
import random as r
import string
import moviepy.editor as mp

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

coord_table2 ='''
░░ (1, 1)  ░░ (2, 1)  ░░ (3, 1)  ░░ (4, 1)  ██ (5, 1)  ██ (6, 1)  ░░ (7, 1)  ██ (8, 1)  ██ (9, 1)  ░░ (10, 1)  

░░ (1, 2)  ░░ (2, 2)  ░░ (3, 2)  ██ (4, 2)  ██ (5, 2)  ░░ (6, 2)  ░░ (7, 2)  ░░ (8, 2)  ██ (9, 2)  ██ (10, 2)  

░░ (1, 3)  ██ (2, 3)  ░░ (3, 3)  ░░ (4, 3)  ░░ (5, 3)  ██ (6, 3)  ░░ (7, 3)  ░░ (8, 3)  ██ (9, 3)  ░░ (10, 3)  

██ (1, 4)  ░░ (2, 4)  ██ (3, 4)  ░░ (4, 4)  ██ (5, 4)  ░░ (6, 4)  ██ (7, 4)  ██ (8, 4)  ░░ (9, 4)  ██ (10, 4)  

░░ (1, 5)  ██ (2, 5)  ██ (3, 5)  ░░ (4, 5)  ░░ (5, 5)  ░░ (6, 5)  ░░ (7, 5)  ░░ (8, 5)  ░░ (9, 5)  ░░ (10, 5)  

██ (1, 6)  ░░ (2, 6)  ██ (3, 6)  ██ (4, 6)  ░░ (5, 6)  ██ (6, 6)  ██ (7, 6)  ░░ (8, 6)  ██ (9, 6)  ░░ (10, 6)  

██ (1, 7)  ██ (2, 7)  ░░ (3, 7)  ██ (4, 7)  ░░ (5, 7)  ██ (6, 7)  ██ (7, 7)  ██ (8, 7)  ░░ (9, 7)  ██ (10, 7)  

░░ (1, 8)  ██ (2, 8)  ░░ (3, 8)  ░░ (4, 8)  ░░ (5, 8)  ░░ (6, 8)  ██ (7, 8)  ░░ (8, 8)  ██ (9, 8)  ░░ (10, 8)  

░░ (1, 9)  ░░ (2, 9)  ██ (3, 9)  ░░ (4, 9)  ██ (5, 9)  ██ (6, 9)  ░░ (7, 9)  ██ (8, 9)  ░░ (9, 9)  ██ (10, 9)  

░░ (1, 10) ░░ (2, 10) ░░ (3, 10) ██ (4, 10) ██ (5, 10) ░░ (6, 10) ██ (7, 10) ░░ (8, 10) ██ (9, 10) ██ (10, 10)  '''




class Cell:

    def __init__(self,position=(1,1), status=0):
        self.stat = status
        self.pos = position

        self.next_stat = None

    def __str__(self):
        return self.symb


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


# sq_n1 = '□'
# sq_f1 = '■'
# sq_n2 = '░░'
# sq_f2 = '██'
# sq_n3 = ' 0'
# sq_f3 = ' 1'
# sq_n4 = '[□]'
# sq_f4 = '[■]'

table ='''░░  ░░  ░░  ░░  ░░  ██  ██  ░░  ██  ██

░░  ░░  ░░  ░░  ░░  ██  ██  ░░  ██  ██

░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ██

░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ██  ░░

░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░

░░  ░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ██

░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░

░░  ░░  ░░  ░░  ░░  ██  ██  ░░  ██  ██

░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ██  ░░

░░  ░░  ░░  ░░  ░░  ██  ░░  ██  ░░  ░░'''

table2 =\
'''
░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  

██  ░░  ░░  ░░  ██  ██  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ██  ██  

██  ░░  ░░  ░░  ░░  ██  ░░  ██  ░░  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  

██  ██  ░░  ░░  ░░  ██  ██  ██  ░░  ░░  ░░  ░░  ██  ██  ░░  ░░  ░░  ░░  ██  ██  

░░  ░░  ██  ██  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ██  ██  ██  ░░  ██  ░░  ░░  ░░  

░░  ░░  ░░  ░░  ██  ░░  ██  ██  ██  ░░  ░░  ░░  ░░  ░░  ░░  ██  ██  ██  ░░  ██  

░░  ░░  ░░  ██  ░░  ██  ██  ░░  ░░  ░░  ░░  ░░  ██  ░░  ██  ░░  ██  ░░  ██  ██  

░░  ░░  ░░  ░░  ██  ░░  ░░  ██  ██  ░░  ██  ██  ██  ██  ██  ░░  ██  ░░  ██  ██  

██  ██  ░░  ░░  ░░  ██  ██  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  

░░  ░░  ░░  ██  ██  ░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ██  ██  ██  ██  ██  

░░  ░░  ░░  ░░  ██  ██  ██  ██  ██  ██  ░░  ██  ██  ░░  ░░  ██  ██  ░░  ░░  ██  

░░  ░░  ░░  ░░  ██  ██  ██  ░░  ██  ░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  

██  ██  ██  ░░  ██  ██  ░░  ██  ░░  ██  ░░  ░░  ██  ░░  ░░  ██  ██  ░░  ██  ░░  

██  ██  ░░  ░░  ██  ░░  ██  ░░  ░░  ██  ██  ░░  ██  ░░  ██  ██  ██  ██  ██  ░░  

░░  ░░  ░░  ░░  ██  ██  ██  ░░  ░░  ██  ██  ██  ██  ██  ██  ██  ██  ░░  ░░  ░░  

░░  ░░  ██  ░░  ░░  ░░  ██  ░░  ██  ░░  ██  ░░  ██  ██  ░░  ░░  ░░  ░░  ██  ░░  

░░  ░░  ██  ██  ░░  ██  ██  ██  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ██  ██  ░░  ░░  

░░  ░░  ░░  ██  ░░  ░░  ██  ██  ░░  ░░  ░░  ██  ██  ░░  ░░  ░░  ░░  ██  ██  ░░  

██  ██  ░░  ░░  ██  ░░  ██  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ░░  ██  ░░  ██  

██  ██  ░░  ░░  ░░  ░░  ██  ██  ░░  ░░  ░░  ░░  ██  ██  ██  ░░  ██  ██  ██  ░░ '''

table3 = '''
██  ░░  ██  ██  ░░  ██  ██  ██  ░░  ██  ██  ██  ██  ░░  ░░  ░░  ░░  ░░  ░░  ░░

██  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ██  ██  ░░  ░░  ██  ░░  ░░  ░░

░░  ░░  ░░  ██  ░░  ░░  ░░  ██  ░░  ██  ██  ██  ░░  ██  ██  ██  ░░  ██  ░░  ░░

██  ██  ░░  ░░  ░░  ░░  ░░  ██  ██  ░░  ░░  ██  ██  ░░  ██  ░░  ██  ░░  ░░  ░░

░░  ░░  ░░  ██  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  ██  ██  ██  ░░  ░░  ░░  ██  ░░

██  ██  ██  ██  ░░  ██  ░░  ██  ██  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ░░

██  ██  ██  ░░  ██  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ██  ░░  ██  ██  ░░  ░░  ░░

░░  ░░  ██  ██  ██  ██  ██  ██  ░░  ██  ░░  ██  ░░  ██  ░░  ██  ██  ██  ░░  ██

░░  ░░  ██  ██  ██  ██  ██  ░░  ░░  ░░  ██  ██  ░░  ██  ░░  ██  ░░  ██  ██  ██

░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ██  ██  ██  ░░  ░░  ░░  ██  ░░
'''



x = 20
y = 10

# print(table)

# img = Image.new('RGB', (x*92,y*92), color = (0,0,0))
#
# title_font = ImageFont.truetype('arial.ttf', 45)
# image_editable = ImageDraw.Draw(img)
# image_editable.text((5,5), table2, (237, 230, 211), font=title_font)
#
# img.save('test2.png')


# image_folder='folder_with_images'
# fps=1
#
# image_files = [os.path.join(image_folder,img)
#                for img in os.listdir(image_folder)
#                if img.endswith(".png")]
# clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
# clip.write_videofile('my_video.mp4')

# import os
# import moviepy.video.io.ImageSequenceClip
# from PIL import Image, ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
#
# files = os.listdir('movie')
#
# new_f = sorted([int(i.replace('.png','')) for i in files])
# new_f = [str(i)+'.png' for i in new_f]
# print(new_f)

