from turtle import *

speed('fastest')
pencolor('green')
pensize(2)

for i in range(8):
    fd(120)
    for i in range(5):
        fd(50)
        lt(360/5)
    lt(360/8)

hideturtle()
mainloop()

