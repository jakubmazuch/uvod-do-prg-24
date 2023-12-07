class Zlomek:
    def __init__(self, c, j):
        self.c = c
        self.j = j

    def vypis(self):
        print(f'zlomek je {self.c}/{self.j}')


if __name__ == '__main__':
    z1 = Zlomek(3, 8)
    z2 = Zlomek(2, 4)
    z1.vypis()
    z2.vypis()
