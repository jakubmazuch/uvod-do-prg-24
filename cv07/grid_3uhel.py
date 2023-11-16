import turtle

def kresli_trojuhelnik(strana):
    """Funkce pro kreslení jednoho rovnostranného trojúhelníka."""
    for _ in range(3):
        turtle.forward(strana)
        turtle.left(120)

def kresli_grid(strana, pocet_v_radku):
    """Funkce pro kreslení gridu trojúhelníků."""
    for y in range(pocet_v_radku):
        for x in range(y + 1):
            kresli_trojuhelnik(strana)
            turtle.forward(strana)
        turtle.backward(strana * (y + 1))
        turtle.right(60)
        turtle.forward(strana)
        turtle.left(60)

# Nastavení Turtle
turtle.speed(1)
turtle.penup()
turtle.goto(-100, 100)  # Startovní pozice
turtle.pendown()

# Kreslení gridu
kresli_grid(50, 5)  # Velikost strany trojúhelníka a počet trojúhelníků v prvním řádku

# Ukončení Turtle
turtle.done()
