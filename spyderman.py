from turtle import *

speed(13)
bgcolor("#990000")
pensize(10)
penup()
goto(0,50)
pendown()
circle(-120)
penup()
circle(-120,-60)
pendown()
pensize(5)
right(50)
circle(70,55)
right(85)
circle(75,58)
right(90)
circle(70,55)
right(90)
circle(70,58)

#body
penup()
pensize(10)
goto(80,15)
pendown()
seth(92)
fd(135)
seth(125)
circle(30,135)
seth(190)
fd(50)
seth(125)
circle(30,135)
seth(275)
fd(90)

#Arm 1
penup()
pensize(10)
goto(92,-150)
seth(240)
pendown()
fd(80)
left(10)
circle(-28,185)

#Arm 2
penup()
goto(0,50)
seth(0)
pensize(10)
circle(-120,-60)
seth(200)
pendown()
fd(72)
left(20)
circle(30,150)
left(20)
fd(20)
right(15)
fd(10)
pensize(5)
fillcolor('#3366cc')
begin_fill()
seth(92)
circle(-120,31)
seth(200)
fd(45)
left(90)
fd(52)
end_fill()
fd(-12)
right(90)
fd(40)
penup()
right(90)
fd(18)
pendown()
right(86)
fd(40)
penup()
goto(-152,-86)
pendown()
left(40)
circle(35,90)
#Body Coloring
penup()
goto(-80,116)
seth(10)
pensize(5)
pendown()
begin_fill()
fillcolor('#3366cc')
fd(155)
seth(-88)
fd(37)
seth(195)
fd(156)
end_fill()


