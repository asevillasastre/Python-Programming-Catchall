import math
import random
from PIL import Image

nueva=Image.new("RGB",(100,100),(0,0,0))
         
def circulo_color(nueva, x_centro, y_centro, distacia_al_centro,color):
    for x in range(nueva.size[0]):
        for y in range(nueva.size[1]):
            if math.sqrt((x-x_centro)**2+(y-y_centro)**2)<=distacia_al_centro:
                nueva.putpixel((x,y),(color))
    return nueva

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def dianatowapa(lado,x_centro,y_centro,grosor):
    nueva=Image.new("RGB",(lado,lado),(0,0,0))
    i=int(math.sqrt(2*lado**2))
    while i>0:
        circulo_color(nueva, x_centro, y_centro, i,random_color())
        i-=grosor
        print(i)
    return nueva

def arte_moderno(circulos,xxx,yyy):
    nueva=Image.new("RGB",(xxx,yyy),(0,0,0))
    for i in range(circulos):
        print(i)
        circulo_color(nueva, random.randint(0,xxx), random.randint(0,yyy), random.randint(0,int(math.sqrt((xxx+yyy))//2)),random_color())
    return nueva

def carta_de_ajuste(lado):
    nueva=Image.new("RGB",(lado,lado),(0,0,0))
    for x in range(nueva.size[0]):
        for y in range(nueva.size[1]):
            nueva.putpixel((x,y),(random_color()))
    return nueva








