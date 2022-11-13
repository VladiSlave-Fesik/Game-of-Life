import pyfiglet as fg
from PIL import Image, ImageFont, ImageDraw
import os
import moviepy.video.io.ImageSequenceClip
import random as r
import string
import moviepy.editor as mp
import cv2
import numpy
from record import *

tabl = '''
░░  ░░  ██  ██  ░░  ░░  ░░  ░░  ░░  ░░  

░░  ██  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  

░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  

░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  

░░  ░░  ██  ██  ░░  ░░  ██  ░░  ░░  ░░  

░░  ░░  ░░  ██  ░░  ░░  ░░  ██  ░░  ░░  

░░  ░░  ░░  ░░  ██  ░░  ██  ░░  ░░  ░░  

░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  ░░  

░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  

░░  ░░  ░░  ░░  ░░  ██  ░░  ░░  ░░  ░░  '''

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

# from record import *
# create_video()
# print(42)

# img = cv2.imread('359.png')
# img = cv2.resize(img,(1000,1000))
# cv2.imwrite('nice.png',img)

