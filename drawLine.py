import matplotlib.pyplot as graf
def drawLine(x1,y1,x2,y2):
    m=float((y2-y1))/((x2-x1))
    args=[x1]
    value=[y1]
    if(m>1):
        z=1
    else:
        z=-1
    for y in range(y1,y2,z):
        x1=x1+(1/m)*z
        args.append(round(x1))
        y1=y1+z
        value.append(y1)
    print "args:",args
    print "value :",value
    odcinek=graf.plot(args,value)
    graf.axis([0,10,0,10])
    graf.show(odcinek)    
drawLine(4,1,5,10)


