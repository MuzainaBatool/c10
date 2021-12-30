import turtle
import random

list1=[10,20,30,40,50,60,70,80,90,110,120,130]
colors=['red','blue','green','cyan','white','pink','grey']

def draw_lines(l,c):
    for value in l:
        turtle.forward(value)
        turtle.pencolor(random.choice(c))
        turtle.stamp()
        turtle.backward(value)
        turtle.right(30)
        l.append(value+20)
        l.remove(value)               
draw_lines(list1,colors)    
        
   
