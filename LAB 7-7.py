import turtle
t = turtle.Turtle()
t.shape('turtle')
for i in range(3):
    t.forward(100)
    t.left(120)
for i in range(3):
    t.forward(200)
    t.left(120)
turtle.done()

import turtle
t = turtle.Turtle()
t.shape('turtle')
lengths = [100, 200, 300]
for length in lengths:   
    for i in range(3):   
        t.forward(length)
        t.left(120)
turtle.done()

import turtle
t = turtle.Turtle()
t.shape('turtle')
for i in range(4):
    t.forward(100)
    t.left(90)
turtle.done()
