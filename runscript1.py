###run script1

simdat = outreadin(path)
miles2=182.009609
path='/Users/ashley/Documents/Modeling/spanishcreek/calibration/outs/'
histor=('/Users/ashley/Documents/Modeling/spanishcreek/calibration/stream/calibstreamflow.csv')
histdattmp= readhist(histor)
histdat=convertflow(histdattmp,miles2)

omean = histmean(histdat)

test= getcalcs(simdat,histdat,omean)

#pp.getallouts() 
something=getallout(path,histor)    

parms=paramindx(test)

parmsss=parmreadin(os.getcwd())

grabbed=parmrange(parms,parmsss)