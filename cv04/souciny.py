from math import *

u = [5, 2, 3]
v = [4, 2, 1]

vekt_soucin = [u[1]*v[2]-v[1]*u[2], u[2]*v[0]-v[2]*u[0], u[0]*v[1]-v[0]*u[1]]
print(vekt_soucin)

skalar = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
print(skalar)

delka_w = sqrt(vekt_soucin[0]**2 + vekt_soucin[1]**2 + vekt_soucin[2]**2)
print(delka_w)

delka_u = sqrt(u[0]**2 + u[1]**2 + u[2]**2)
delka_v = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
if delka_u == 0 or delka_v == 0:
    mezivypocet = skalar / (delka_u * delka_v)
    if mezivypocet > -1 and mezivypocet < 1:
        rad = acos(mezivypocet)
        print(rad, "rad")
        deg = (180/pi)*rad
        print(deg, "deg")
        
        d2 = int(deg)
        m2 = int((deg - d2) * 60)
        s2 = ((deg - d2) * 60 - m2) * 60

        print(d2, "°", m2, "'", s2, "''")