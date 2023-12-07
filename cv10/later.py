from cas import Cas


def later(cas, hodiny, minuty):
    novy = Cas(cas.hodiny, cas.minuty)
    novy.pridej(hodiny, minuty)
    return novy


c = Cas(17, 40)
d = later(c, 2, 55)
print(c.str())
print(d.str())
