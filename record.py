import cv2
import os
import random as rnd
import string
from PIL import Image, ImageFont, ImageDraw

def create_video(pathIn='frames\\',pathOut='movie\\',fps=3):
    global name
    name = ''.join(rnd.choice(string.ascii_letters + string.digits) for i in range(5))
    while name in os.listdir('movie'):
        name = ''.join(rnd.choice(string.ascii_letters + string.digits) for i in range(5))
    pathOut = pathOut + name + '.mp4'
    files = os.listdir(pathIn)
    files = sorted([int(i.replace('.png','')) for i in files])
    files = [str(i)+'.png' for i in files]
    frame_array = []
    for i in range(len(files)):
        filename=pathIn + files[i]
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

def create_img(tbl,name_img,x=10,y=10):
    folder = 'frames\\'
    img = Image.new('RGB', (x * 92, y * 92), color=(0, 0, 0))

    title_font = ImageFont.truetype('arial.ttf', 45)
    image_editable = ImageDraw.Draw(img)
    image_editable.text((5, 5), tbl, (237, 230, 211), font=title_font)

    img.save(folder+name_img+'.png')

def delete_images():
    files = os.listdir('frames')
    for file in files:
        if file.endswith('.png'):
            os.remove('frames\\'+file)