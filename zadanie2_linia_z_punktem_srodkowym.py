import matplotlib.pyplot as plt

def antyaliasing(xp, yp, xk, yk):
    xlist = []
    ylist = []
    dx = xk - xp
    dy = yk - yp
    dydx = (254*dy)/dx
    y = 0
    for x in range(dx):
        c = y & 255
        i = y >> 8
        xlist.append(xp+x)
        xlist.append(xp+x)
        ylist.append(yp+i)
        ylist.append(yp+i+1)
        y += dydx


def rysowanie(xp, yp, xk, yk):
    x_list = []
    y_list = []
    colors = []

    dx = xk - xp
    dy = yk - yp
    print('dy', dy)
    print('dx', dx)

    dydx = (256*dy)/dx
    y = 0
    for x in range(dx):
        c = y & 255
        i = y >> 8
        x_list.append(xp+x)
        y_list.append(yp+i)
        colors.append(c)

        x_list.append(xp+x)
        y_list.append(yp+i+2)
        colors.append(254-c)
        y += dydx

    if xp > xk and yp > xk:
        xp, xk = xk, xp
        yp, yk = yk, yp

    if float(yk-yp) != 0 and float(xk-xp) != 0:
        a = float(yk-yp) / (xk-xp)

        if a >= 1 or a <= -1:
            for i in range(abs(yp-yk)):
                y_list.append(yp)
                if a >= 1:
                    yp += 1
                    xp += 1/a
                else:
                    yp -= 1
                    xp -= 1/a
                x_list.append(round(xp))
                colors.append(0)
        if -1 < a < 1:
            for i in range(abs(xp-xk)):
                x_list.append(xp)
                xp += 1
                yp += a
                y_list.append(round(yp))
                colors.append(0)
    else:
        if float(yk-yp) == 0:
            for x in range(xp, xk):
                x_list.append(x)
                y_list.append(yp)
                colors.append(0)
        else:
            if float(yk-yp) < 0:
                for y in range(yk, yp):
                    y_list.append(y)
                    x_list.append(xp)
                    colors.append(0)
            else:
                for y in range(yp, yk):
                    y_list.append(y)
                    x_list.append(xp)
                    colors.append(0)

    print(colors)
    plt.axis([0, 20, 0, 20])
    for i in range(len(x_list)):
        plt.plot(x_list[i], y_list[i], 's', markersize=12, color=str(colors[i]))
    plt.show()


##print '1', rysowanie(10,10,10,20)
##print '2', rysowanie(10,10,14,19)
##print '3', rysowanie(10,10,18,18)
##print '4', rysowanie(2,2,19,14)
##print '5', rysowanie(10,10,20,10)
##print '6', rysowanie(10,10,19,6)
print('7', rysowanie(10,10,18,2))
# print '8', rysowanie(10,10,14,1)
# print '9', rysowanie(10,10,10,0)
# print '10', rysowanie(10,10,6,1)
# print '11', rysowanie(10,10,2,2)
# print '12', rysowanie(10,10,1,6)
# print '13', rysowanie(10,10,0,10)
# print '14', rysowanie(10,10,1,14)
# print '15', rysowanie(10,10,2,18)
# print '16', rysowanie(10,10,6,19)
