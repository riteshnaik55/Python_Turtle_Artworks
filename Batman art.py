
#Batman Art Logo
from turtle import *

def run():
    forward(10)
    your_left(90)
    forward(30)
    your_right(150)
    forward(35)
    your_left(40)
    for i in range(70):
        your_left(1)
        forward(3)
    your_right(70)
    forward(100)
    your_right(140)
    forward(100)
    your_left(40)
    forward(30)
    your_right(55)
    forward(130)
    your_left(40)
    forward(103)

def your_right(num):
    if(mirror):
        right(num)
    else:
        left(num)

def your_left(num):
    if(mirror):
        left(num)
    else:
        right(num)

bgcolor(0.99,0.035,0.04)
mirror=True
pencolor('#000')
pensize(3)
fillcolor('#000')
begin_fill()
up()
goto(0,100)
down()
run()
up()
goto(0,100)
down()
mirror=False
right(45)
run()
goto(0,-20)
end_fill()

up()
goto(-200,-150)

write("''When that light hits the sky,\nit's not just a call it's a warning.''\n\t\tThe BatMan(2022)",font=('Arial',18,'bold'))
goto(-500,-500)
done()