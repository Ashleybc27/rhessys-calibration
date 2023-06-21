####get params### 
#from rhsprocess import PostProc as pp
import os
import hydroeval as he
import matplotlib.pyplot as plt

#path='/Users/ashley/Documents/Modeling/spanishcreek/calibration/outs/'
#histor='/Users/ashley/Documents/Modeling/spanishcreek/calibration/stream/calibstreamflow.csv'
#pp.getallouts(path,histor)

#print(test)
#test.sort(key=lambda x: x[0], reverse=True)
#est
##plotly <- plot


def paramindx(outs):
    outs.sort(key=lambda x: x[1], reverse=True) #sort based on nnse
    set1=list()
    for i in outs[0:10]:
        print(i)
        if i[0] <= 1:
            set1.append(i)
        else:
            pass
    return(set1)

parms=paramindx(test)
#print(parms)

def plotgood (simdat,histdat,paramindx): ##use smoothed data here 
    plotdata = []
    for i in simdat:
        for j in paramindx:
            num = j[4]
            print(num)
            if i[1][5] == num:  
                plotdata.append(i)
            else:
                pass
    return(plotdata)

ptest = plotgood(simdat,smth,parms)  

def getdata (plotdata): ##I loose the indexing this way but that's okay for now
    datavals = []
    for k in plotdata:
        listvals=[]
        for h in k:
            listvals.append(h[3])
        datavals.append([listvals])  
    return(datavals)

plt.plot(dattest[1])
plt.plot(dattest[2])
plt.show()
dattest = getdata(ptest)
dattest[1]
len(dattest)
plt.show()
    #plt.plot(histdat[1])
    



def parmreadin(_path_): # function using these indices
    parsable = os.listdir(_path_)
    tmp=list()
    #simout=list()
    for i in parsable:
        with open(i, 'r') as _i_:
            all=list()
            name= i.split('_')
            for line in _i_:
                line = line.strip('\n')
                line = line.split(' ') 
                all.append(line)
            #del all[0] 
        tmp.append(all) 
    return(tmp)

#parmsss=parmreadin(os.getcwd())
#print(parmsss[1])

def fixind(parms):
    right=list()
    for i in parms:
        t1=(int(i[0])-1)
        t2=(int(i[1])-1)
        right.append([t1,t2])
    return(right)

def parmrange(parms,parmsss):
    litall=list()
    for i in parms:
        ind1=(i[0]-1)
	#print(ind1)
        ind2=(i[1]-1)
	#print(ind2)
        litall.append(parmsss[ind1][ind2])
    v1=list()
    v2=list()
    v3=list()
    v4=list()
    v5=list()
    v6=list()
    for j in litall:
        print(j)
        v1.append(j[0])
        v2.append(j[1])
        v3.append(j[2])
        v4.append(j[3])
        v5.append(j[4])
        v6.append(j[5])
    allrange=list()
    allrange.append([min(v1),max(v1)])
    allrange.append([min(v2),max(v2)])
    allrange.append([min(v3),max(v3)])
    allrange.append([min(v4),max(v4)])
    allrange.append([min(v5),max(v5)])
    allrange.append([min(v6),max(v6)])
    return(allrange)

#grabbed=parmrange(parms,parmsss)
#len(grabbed)
