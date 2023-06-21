###run script1

os.chdir(path)
simdat = outreadin(path) ##all together, smoothed 
miles2=182.009609
path='/Users/ashley/Documents/Modeling/spanishcreek/calibration/outs/'
histor=('/Users/ashley/Documents/Modeling/spanishcreek/calibration/stream/calibstreamflow.csv')
histdattmp= readhist(histor)
histdat=convertflow(histdattmp,miles2)
len(histdat)
smth = smooth3d(histdat)
omean = histmean(smth)
simdat[4]
test= getcalcs(simdat,smth,omean)
print(test)
#pp.getallouts() 
somethinghe=getallouts(path,histor,miles2)    

parms=paramindx(test)

parmsss=parmreadin(os.getcwd())

grabbed=parmrange(parms,parmsss)


