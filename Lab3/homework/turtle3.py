from turtle import *

def draw_square(length,color):
   pencolor(color)
   for _ in range(4):
       forward(length)
       left(length)


draw_square(90,"magenta")