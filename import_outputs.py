#bulk processing of rhessys output files###
import os
##############################################################
def outreadin(_path_): # function using these indices
    parsable = os.listdir(_path_)
    tmp=list()
    simout=list()
    for i in parsable:
        with open(i, 'r') as _i_:
            all=list()
            name= i.split('_')
            print(name)
            for line in _i_:
                line = line.strip('\n')
                line = line.split(' ') 
                all.append([line[2],line[1],line[0],line[18],name[3],name[4]])
            del all[0] 
        tmp.append(all) 
        tmpp=list()
        for j in all:
            if int(j[0]) == 1979 and int(j[1]) >= 10:
                tmpp.append([j[2],j[1],j[0],j[3],j[4],j[5]])
            if int(j[0]) >=1980:
                tmpp.append([j[2],j[1],j[0],j[3],j[4],j[5]])
            else:
                pass
        simout.append(tmpp) 
    return(simout)

#simdat = outreadin(path)

def readhist (file):
    histor=file
    with open(histor,'r') as _j_:
        tmp=list()
        for lin in _j_:
            lin = lin.strip('\n')
            lin = lin.split(',')
            tmp.append(lin)
        del tmp[0]
    print(tmp[0])
    return(tmp)

#miles2=182.009609
def convertflow(tmp,miles2):
    obs=list()
    for ech in tmp:
        lix = float(ech[2])/(miles2*27878400)*304.8*60*60*24 #convert to mm/day
        obs.append([ech[1],lix])
    print(obs[4])
    return(obs)

#histor=('/Users/ashley/Documents/Modeling/spanishcreek/calibration/stream/calibstreamflow.csv')
#histdattmp= readhist(histor)
#histdat=convertflow(histdattmp,miles2)

def histmean(obs):
    osum=0
    for i in obs:
        osum += float(i[1])
    print(osum)
    omean=osum/len(obs)
    print(len(obs))
    print(omean)
    return(omean)

#omean = histmean(histdat)
#print(omean)

##instead of doing this ^^^^ can I just check the indicies and then loop through each list iterativley?
##print(simdat[0][-1])
##print(histdat[-1])
##indexes line up :) 

def getcalcs (simdat,histdat,omean):
    outs=list()
    for k in simdat:
        nsx = nse(k,histdat,omean)
        pbs = pbias(k,histdat)
        #rsq = rsqu(k,histdat,omean)
        outs.append([nsx,pbs,k[0][4],k[0][5]])
    return(outs)

#test= getcalcs(simdat,histdat,omean)
#print(test)

def nse (simdat,histdat, omean):
    tp1= 0
    bm1 = 0
    for i in simdat: 
        tp1 += ((histdat[simdat.index(i)][1] - float((i[3])))**2)
        bm1 += ((histdat[simdat.index(i)][1]- float(omean))**2)
    nse = 1 - (tp1/bm1)
    return(nse)

def rsqu (simdat,histdat,omean):
    t=0
    b=0
    for p in simdat:
        t += ((float((p[3])) - histdat[simdat.index(p)][1])**2)
        b += ((histdat[simdat.index(p)][1] - float(omean))**2)
    rsq = 1 - (t/b)
    return(rsq)

def pbias (simdat,histdat):    #####check equation
    t =0
    b =0
    for j in simdat:
        t += (float(j[3])-histdat[simdat.index(j)][1])
        b += float(j[3])
        pbias= 100 * (t/b) 
    return(pbias)

def writeouts (outs):
    with open('output.txt', 'w') as output:
        for line in outs:
            for element in line:
                output.write(f'{element},')
            output.write('\n')

def getallouts (_path_,histor):
    simdat = outreadin(_path_)
    print('yay')
    histdattmp = readhist(histor)
    print('yay2')
    histdat = convertflow(histdattmp)
    print('yay3')
    omean = histmean(histdat)
    print('yay4')
    outs = getcalcs (simdat, histdat, omean)
    print('sheworks :)')
    writeouts(outs)
    return(outs)


#from rhsprocess import PostProc as pp

#pp.getallouts()