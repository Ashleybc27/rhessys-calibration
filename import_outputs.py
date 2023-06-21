#bulk processing of rhessys output files###
import os
import numpy as np
import hydroeval as he

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
                tmpp.append([int(j[2]),int(j[1]),int(j[0]),float(j[3]),int(j[4]),int(j[5])])
            if int(j[0]) >=1980:
                tmpp.append([int(j[2]),int(j[1]),int(j[0]),float(j[3]),int(j[4]),int(j[5])])
            else:
                pass
        sssmmmoootttthhh = smooth3dsim(tmpp)###adding smoothing 
        print(sssmmmoootttthhh[0])
        simout.append(sssmmmoootttthhh) 
    return(simout)

def smooth3dsim(input):
    back=input
    smoothed=list()
    #back.insert(0,input[0])
    #print(back[0:2])
    #back.append(input[-1])
    lst=len(back)-1
    print(lst)
    print
    for j in back:
        if back.index(j)==0 or back.index(j)==lst:
            pass
            print(back.index(j))
            print(j)
        else:
           #print(j)
            idx = back.index(j)
            #print(idx)
            bf=idx+1
            aft=idx-1
            avg=(float(back[bf][3])+ float(back[idx][3])+ float(back[aft][3]))/3
        ##need to index across a few lists, how to do that?
            smoothed.append([int(j[2]),int(j[1]),int(j[0]),float(avg),int(j[4]),int(j[5])])
    fnt=(float(input[0][3]) + float(input[0][3]) + float(input[1][3]))/3
    ed = (float(input[-1][3]) + float(input[-1][3]) + float(input[-2][3]))/3
    print(fnt)
    print(ed)
    smoothed.insert(0,[input[0][0],input[0][1],input[0][2],fnt,input[0][4],input[0][5]]) 
    smoothed.append([input[-1][0],input[-1][1],input[-1][2],ed,input[-1][4],input[-1][5]])
    return(smoothed)
simdat = outreadin(path)
simdat[1][4][5]

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

miles2=182.009609 
def convertflow(tmp,miles2):  #convert to mm/day
    obs=list()
    milesconv= miles2*2589988110000
    for ech in tmp:
        lix = (float(ech[2])*28316846.37) ##cubic ft to cubic mm per second
        lix2 = lix * 86400 ##cubic mm per day
        lix3= lix2/milesconv ##over basin area to mm/day
        obs.append([ech[1],lix3])
    print(obs[4])
    return(obs)

def smooth3d(input):
    back=input
    smoothed=list()
    #back.insert(0,input[0])
    #print(back[0:2])
    #back.append(input[-1])
    lst=len(back)-1
    print(lst)
    print
    for j in back:
        if back.index(j)==0 or back.index(j)==lst:
            pass
            print(back.index(j))
            print(j)
        else:
           #print(j)
            idx = back.index(j)
            #print(idx)
            bf=idx+1
            aft=idx-1
            avg=(back[bf][1]+back[idx][1]+back[aft][1])/3
        ##need to index across a few lists, how to do that?
            smoothed.append([j[0],avg])
    fnt=(input[0][1] + input[0][1] + input[2][1])/3
    ed = (input[-1][1] + input[-1][1] + input[-2][1])/3
    print(fnt)
    print(ed)
    smoothed.insert(0,[input[0][0],fnt]) 
    smoothed.append([input[-1][0],ed])
    return(smoothed)

print(histdat[3652:3655])
test=smooth3d(histdat)
len(histdat)
len(test)
print(test[-1])
print(test[0:3])
print(histdat[1])
print(histdat[-2])

len(simdat[17])


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
smlsim= simdat[3]
onesim=[]
for o in smlsim:
    smlsimval=float(o[3])
    onesim.append(smlsimval)
print(onesim)
print(smlsim)
histvals=[]
for p in histdat:
    valls=float(p[1])
    histvals.append(valls)
print(histvals)

tst=he.nse(np.array(onesim),np.array(histvals))
print(tst)

print(something)

def getcalcs (simdat,histdat,omean):
    outs=list()
    histvals=[]
    for p in histdat:
        valls=float(p[1])
        histvals.append(valls)
    for k in simdat:
        singlesim = k
        onesim=[]
        for o in singlesim:
            smlsimvals=float(o[3])
            onesim.append(smlsimvals)
        nsx = he.nse(np.array(onesim),np.array(histvals))
        nnsx = nnse(nsx)
        pbs = pbias(k,histdat)
        #rsq = rsqu(k,histdat,omean)
        outs.append([nsx,nnsx, pbs,k[0][4],k[0][5]])
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

def nnse(nse):
    nnse = 1/(2-nse)
    return(nnse)

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

def getallouts (_path_,histor,miles):
    simdat = outreadin(_path_)
    print('yay')
    histdattmp = readhist(histor)
    print('yay2')
    histdat = convertflow(histdattmp,miles)
    print('yay3')
    smoothin = smooth3d(histdat)
    print('yay3.5')
    omean = histmean(smoothin)
    print('yay4')
    outs = getcalcs (simdat, histdat, omean)
    print('sheworks :)')
    #writeouts(outs)
    return(outs)


#from rhsprocess import PostProc as pp

#pp.getallouts()
