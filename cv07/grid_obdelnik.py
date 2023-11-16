import turtle

def obdelnik(sirka, vyska):
    for i in range(2):
        turtle.forward(sirka)
        turtle.left(90)
        turtle.forward(vyska)
        turtle.left(90)

def grid(sirka, vyska, pocet):
    for y in range(pocet):
        for x in range(pocet):
            obdelnik(sirka, vyska)
            turtle.forward(sirka)
        turtle.backward(pocet * sirka)
        turtle.right(90)
        turtle.forward(vyska)
        turtle.left(90)

# Nastavení želvy
turtle.speed(10)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

grid(20, 10, 5)

turtle.done()