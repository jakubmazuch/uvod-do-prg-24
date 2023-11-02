import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(10)
t.color("blue")

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
