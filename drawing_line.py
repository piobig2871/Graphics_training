import matplotlib.pyplot as rys

def linia2(x1,y1,x2,y2):
    m = (float(y2) - float(y1)) / (float(x2) - float(x1))
    argumenty = [x1]
    wartosci = [y1]
    for y in range(y1,y2):
        x1 = x1 + (1 / m)
        argumenty.append(round(x1))
        y1 = y1 + 1
        wartosci.append(y1)
    print(m)
    print(argumenty, wartosci)
    odcinek = rys.plot(argumenty, wartosci,"s", markersize=12)
    rys.axis([0,20,0,20])
    rys.show(odcinek)
    rys.savefig(odcinek)

linia2(4,2,5,15)




