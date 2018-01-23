from pylab import *
import numpy as np
import time
import random

def line(n,m,pocz,kon,d):
    table=np.zeros((n,m,3))
    table.fill(1.0)
    if kon[0]<pocz[0]:
        temp=kon[0]
        kon[0]=pocz[0]
        pocz[0]=temp
    if kon[1]<pocz[1]:
        temp=kon[1]
        kon[1]=pocz[1]
        pocz[1]=temp
        
    while d/2>0:
        if pocz[0]==kon[0]:
            for i in xrange(int(pocz[1]),int(kon[1])):
                table[i,int(kon[0]),0]=1.0
                table[i,int(kon[0]),1]=0.0
                table[i,int(kon[0]),2]=0.0 
            pocz[0]-=0.1
            kon[0]-=0.1
        
        elif pocz[1]==kon[1]:
            for i in xrange(int(pocz[0]),int(kon[0])):
                table[int(pocz[1]),i,0]=1.0
                table[int(pocz[1]),i,1]=0.0
                table[int(pocz[1]),i,2]=0.0
            pocz[1]-=0.1
            kon[1]-=0.1

        else:
            a=(abs(pocz[0]-kon[0])/abs(pocz[1]-kon[1]))
            for i in xrange(int(pocz[0]),int(kon[1])):
                table[int(a*i),i,0]=1.0
                table[int(a*i),i,1]=0.0
                table[int(a*i),i,2]=0.0
            pocz[0]-=0.1
            kon[1]-=0.1
        d-=0.1
        
    while d/2>0:
        if pocz[0]==kon[0]:
            for i in xrange(int(pocz[1]),int(kon[1])):
                table[i,int(kon[0]),0]=1.0
                table[i,int(kon[0]),1]=0.0
                table[i,int(kon[0]),2]=0.0 
            pocz[0]+=0.1
            kon[0]+=0.1
        
        elif pocz[1]==kon[1]:
            for i in xrange(int(pocz[0]),int(kon[0])):
                table[int(pocz[1]),i,0]=1.0
                table[int(pocz[1]),i,1]=0.0
                table[int(pocz[1]),i,2]=0.0
            pocz[1]+=0.1
            kon[1]+=0.1

        else:
            a=(abs(pocz[0]-kon[0])/abs(pocz[1]-kon[1]))
            for i in xrange(int(pocz[0]),int(kon[1])):
                table[int(a*i),i,0]=1.0
                table[int(a*i),i,1]=0.0
                table[int(a*i),i,2]=0.0
            pocz[0]+=0.1
            kon[1]+=0.1
        d-=0.1
    plt.imshow(table, interpolation='nearest')
    axis([0,n,0,m])
    plt.show()
def test(n):
    czas=0
    for i in xrange(n):
        punkt_x=random.uniform(0,10)
        punkt_y=random.uniform(0,10)
        punkt1_x=random.uniform(0,10)
        punkt1_y=random.uniform(0,10)
        start=time.time()
        line(6000,6000,[punkt_x,punkt_y],[punkt1_x,punkt1_y],2)
        stop=time.time()
        czas+=stop-start
    return czas/n
        
        

print (line(500,500,[200.0,200.0],[300.0,100.0],2))    
#print "Sredni czas wykonania funkcji dla 50 wykonan: "
#print test(50)


