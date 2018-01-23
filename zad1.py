from pylab import *
import numpy as np
def rysujOkrag(n,m,srodek,r):
    macierz=np.zeros((n,m,3))
    kat = np.arange(0, 2*np.pi,0.01)
    for i in kat:
        x = srodek[0] + r * np.cos(i)
        y = srodek[1] + r * np.sin(i)
        macierz[int(x),int(y),0]=1.0
        macierz[int(x),int(y),1]=0.0
        macierz[int(x),int(y),2]=0.0
    plt.imshow(macierz)
    plt.show()
print rysujOkrag(200,200,[95.0,95.0],50)    

