import turtle


def kresli_sestiuhelnik(strana):
    """Funkce pro kreslení jednoho šestiúhelníka."""
    for _ in range(6):
        turtle.forward(strana)
        turtle.left(60)


def posun_pro_dalsi_sestiuhelnik(strana, radek, sloupec):
    """Funkce pro posunutí želvy na pozici pro kreslení dalšího šestiúhelníka."""
    x = strana * 1.5 * sloupec
    y = strana * 1.73 * (radek - sloupec / 2)
    turtle.penup()
    turtle.goto(x, -y)
    turtle.pendown()


def kresli_sestiuhelnikovy_grid(strana, radky, sloupce):
    """Funkce pro kreslení gridu šestiúhelníků."""
    for r in range(radky):
        for s in range(sloupce - (r // 2)):
            posun_pro_dalsi_sestiuhelnik(strana, r, s)
            kresli_sestiuhelnik(strana)


# Nastavení Turtle
turtle.speed('fastest')
turtle.penup()
turtle.goto(0, 0)  # Startovní pozice
turtle.pendown()

# Kreslení šestiúhelníkového gridu
# Velikost strany šestiúhelníka, počet řádků, počet sloupců
kresli_sestiuhelnikovy_grid(30, 5, 4)

# Ukončení Turtle
turtle.hideturtle()
turtle.done()
