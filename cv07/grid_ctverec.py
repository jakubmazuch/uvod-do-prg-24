import turtle

def ctverec(velikost):
    for i in range(4):
        turtle.forward(velikost)
        turtle.left(90)

def grid(velikost, pocet):
    for y in range(pocet-1):
        for x in range(pocet):
            ctverec(velikost)
            turtle.forward(velikost)
        turtle.backward(pocet * velikost)
        turtle.right(90)
        turtle.forward(velikost)
        turtle.left(90)

# Nastavení želvy
turtle.speed(10)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

grid(20, 5)

turtle.done()