class Cas:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def vypis(self):
        print(f'{self.h}:{self.m:02}')

    def str(self):
        return str(f'{self.h}:{self.m:02}')

    def pridej(self, h, m):
        self.h += h
        self.m += m
        if self.m > 60:
            self.h += 1
            self.m -= 60


c = Cas(9, 1)
c.vypis()

print(c.str())
c.pridej(1, 45)
print(f'čas je: {c.str()}')
