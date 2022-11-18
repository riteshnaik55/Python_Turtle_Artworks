from turtle import *

def your_right(ang):                    #Interchanges right to left as per mirror value
    if(mirror):
        right(ang)
    else:
        left(ang)
        
def your_left(ang):                     #Interchanges left to right as per mirror value
    if(mirror):
        left(ang)
    else:
        right(ang)

def your_circle(rad,ang):             #Interchanges circle direction
    if(mirror):
        circle(rad,ang)
    else:
        circle(-rad,ang)

def person_side():                          #Half side of human
    seth(270)
    forward(10)
    your_right(60)
    forward(15)
    your_circle(40,40)
    your_right(8)
    forward(80)
    your_right(50)
    forward(25)
    your_circle(7,180)
    your_right(8)
    forward(30)
    your_circle(10,55)
    forward(70)
    seth(270)
    forward(50)
    your_right(40)
    your_circle(40,30)

def cat_side():                                 #Half side of cat
    your_right(60)
    your_circle(55,-70)
    your_left(70)
    your_circle(25,-50)
    your_left(50)
    your_circle(20,-50)
    your_right(80)
    your_circle(20,-50)
    your_right(117)
    forward(6)

screen = Screen()
screen.cv._rootwindow.resizable(False, False)
screen.setup(700, 600,  startx=300, starty=0)  

bgcolor(0.4,0,0.6)
pensize(3)
speed(2)
fillcolor('#000')
mirror=True

up()                                        #Go to out of page
goto(-400,-127)
down()

begin_fill()
forward(800)                            #Draw 700 unit surface line
speed(10)
right(90)
forward(200)
right(90)
forward(800)
right(90)
forward(200)
end_fill()

up()
goto(-110,0)                                      #Go to 0,0 to start from person neck
down()

begin_fill()                                        #Begin fill of person
mirror=True
person_side()                                                  # left side of human

up()
goto(-110,0)                                     #Go to 0,0 to start from person neck
down()

left(60)                                                   # human head
circle(40,-140)
circle(100,-10)
right(180)
forward(15)
right(140)
forward(10)
left(90)
circle(-60,20)
left(40)
forward(12)
right(120)
forward(10)
left(60)
circle(-70,26)

up()
goto(-67,0)                                          #Go to right neck
seth(0)
down()

mirror=False
person_side()                                             #right body of person
seth(180)
forward(93)
end_fill()                                              #End fill of person

up()                                                 #Go to 50, -127 surface of line
goto(105,-127)
down()
begin_fill()
goto(61,-127)

mirror=True
seth(0)
cat_side()                                              #Left side of cat

mirror=False
up()
goto(105,-127)
down()

seth(180)
cat_side()                                                  #Right side of cat
end_fill()

up()
goto(90,-128)                                           #Goto cat's bottom position
down()
pensize(8)

left(180)                                                   #Cat's tail
circle(40,60)
right(170)
circle(40,-70)

up()
goto(-40,150)
down()
pencolor(0.8,0.8,0.2)
write("''You'll never find the light.\nYou just have to find someone \nto walk through the darkness.''",font=('Arial',19,'bold'))

hideturtle()

done()