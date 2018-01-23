from pylab import *
import numpy as np

def okrag(n,m,pocz,r,fill):
    table=np.zeros((n,m,3))
    table.fill(1.0)
    dokladnosc = 0.01
    kat = np.arange(0, 2*np.pi, dokladnosc)
    if fill==1:
        pom=r
    else:
        pom=1
    for z in range(pom):
        for i in kat:
            x = pocz[0] + r * np.cos(i)
            y = pocz[1] + r * np.sin(i)
    
            table[int(x),int(y),0]=1.0
            table[int(x),int(y),1]=0.0
            table[int(x),int(y),2]=0.0
        r=r-1
    plt.imshow(table)
    plt.show()
print okrag(500,500,[200.0,200.0],50,0)    
