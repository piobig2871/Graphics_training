import matplotlib.pyplot as plt
import numpy as np
import math

# linia

def rysowanie(sx, sy, ex, ey):
    x = sx
    y = sy
    a = (ey - sy) / (ex - sx)

    punkty = []

    for x in range(sx, ex+1):
        punkty.append((x, int(round(y))))
        x += 1
        y += a
    return punkty

lista = rysowanie(1,2,15,7)

print(lista)

x_list = [x for [x,y] in lista]
y_list = [y for [x,y] in lista]
#
# plt.plot(x_list, y_list, 'bs')
# plt.ylabel('param1')
# plt.axis([0,10,0,10])
# plt.scatter(x_list,y_list)
# plt.show()

r = 7
ax = plt.gca()
ax.add_patch(plt.Circle((0,0),radius=r,facecolor=(.7,.7,.7),edgecolor='blue'))
plt.xlim([-r-2,r+2])
plt.ylim([-r-2,r+2])
plt.axes().set_aspect('equal')
plt.savefig('kolo.pdf')
plt.show()
