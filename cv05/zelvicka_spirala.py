import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(10)
t.color("blue")

for i in range(150):
    t.forward(i)
    t.left(45)

turtle.done()
