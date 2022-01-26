# Iron Man Logo Program
from turtle import *

bgcolor('#00ccff')
title('Turtle test')
speed(15)
pensize(3)
color('black')

#Mask
fillcolor('red')
goto(-5,-20)
begin_fill()
circle(115)
end_fill()

up()
goto(-120,90)
seth(60)
fd(60)
pendown()

#Inner Mask Design
begin_fill()
fillcolor('yellow')
for i in range(45):
    rt(1)
    fd(2)

seth(270)
fd(60)
seth(0)
fd(30)
seth(90)
fd(60)
seth(0)

for i in range(50):
    rt(1.5)
    fd(2)

for i in range(60):
    rt(0.8)
    fd(2)

for i in range(5):
    rt(3)
    fd(2)

seth(120)
fd(20)
seth(180)
fd(90)
seth(240)
fd(20)

seth(140)
for i in range(70):
    rt(1)
    fd(2)

end_fill()

up()
goto(20,100)
down()

#Eyes
begin_fill()
fillcolor('white')
seth(30)
fd(60)
seth(300)
fd(20)
seth(210)
fd(60)
seth(120)
fd(20)
end_fill()

up()
goto(-20,100)
down()

begin_fill()

seth(140)
fd(60)
seth(225)
fd(20)
seth(319)
fd(60)
seth(40)
fd(20)
end_fill()

up()
goto(-20,-120)
down()

speed(1)
write('Feels like something raining down hellfire,',align='center',font=('Arial', 25,'normal'))
up()
goto(-20,-155)
down()
write('and here I am without an umbrella.',align='center',font=('Arial', 25,'normal'))
up()
goto(200,-190)
write(' - RDJ',align='center',font=('Arial', 25,'normal'))

done()
