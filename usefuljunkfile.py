###useful junk file###



#########junkyard#########
def compare_dates(date1, date2):
    def dosplit(date):
        if isinstance(date, str):
            date = date.split('-')
            date = [int(e) for e in date]
            return date
        elif isinstance(date, list):
            date = [int(e) for e in date]
            return date
    date1 = dosplit(date1)
    date2 = dosplit(date2)
    if_all = list()
    for N in range(0,2):
        if date1[N] == date2[N]:
            if_all.append(True)      
        else: if_all.append(False)
    if all(if_all):
        return True
    elif not all(if_all):
        return False   
print(simdat[0][1])   
print(histdat[1]) 
def combinedata (simdat,histdat):
    mergedat=list()
    for a in simdat:
        smldat = list()
        for b in a:
            for c in histdat:
                if compare_dates(b[0:2],c[1]) == True:
                    row= [b[0],b[1],b[2],b[3],c[2]]
                    smldat.append(row)
                else:
                    pass
        print('yay')
        mergedat.append(smldat)
    return(mergedat)

mergedat= combinedata(simdat,histdat)

    wantout = list()
    for i in parsable:
        with open(i, 'r') as _i_:
            all=list()
            for line in _i_:
                line = line.strip('\n')
                line = line.split(' ') 
                all.append(list([line[2]+"-"+line[1]+"-"+line[0], line[18]]))
            del all[0]     
        wantout.append(all)
    return wantout


print(dataout[0])

j = 3
obs [j][2]

def calcnse(minilit,omean):
    tp1= 0
    bm1 = 0
    for i in minilit: 
        tp1.add((i[3] - i[4])**2)
        bm1.add((i[3]-omean)**2)
        nse = 1 - (tp1/bm1)
    print(nse)
    return(nse)



# def _embedded_foo_(_want_, compare_to_me2):
        
       # for j in minilit:
           # t2 = (j[3]-j[4])
           # b2= j[4]
           # tp2.add(t2)
           # bm2.add(b2)
            #return()
      #  pbias= 100 * (tp2/bm2)
       # out.append(list(i,nse,pbias))
    #
for j in all:
                if int(j[2]) == 1979 and int(j[1]) >= 10:
                    want.append(j)
                if int(j[2]) >=1980:
                    want.append(j)
                else:
                    pass
        for t in want:
            histsim = list()
            for h in obs:
                if t[0:2] == h[0:2]:
                    nrow= t + h[2]
                    histsim.append(nrow)

def compare_dates(date1, date2):
    date1 = date1.split('-')
    date2 = date2.split('-')
    if_all = list()
    for N in range(0,2):
        if date1[N] == date2[N]:
            if_all.append(True)
        else: if_all.append(False)
    if all(if_all):
        return True
    elif not all(if_all):
        return False

def single_read(a_string,_ash_criteria, delimiter = ' '):
    if _ash_criteria in str(a_string):
        with open(a_string, 'r') as readfile:
            to_env = list()
            for line in readfile:
                line = line.strip('\n')
                line = line.split(delimiter)
                to_env.append(line)
            return to_env
    else:
        pass

def open_reading(directory, _ash_criteria):
    contents = os.listdir(directory) 
    for _ in contents:
        tmp = (single_read(_, _ash_criteria))
        print(tmp[0:10])
        lofl.append(tmp)
   

open_reading(os.getcwd(),'basin.daily')
lofl = list()
lofl[1][0:1]

data = list()
for i in os.listdir():
    l = single_read(i, 'basin.daily')
    print(l[0:10])
    data.append(l)

data[1][0:10]
os.chdir('/Users/ashley/Documents/Modeling/spanishcreek/calibration/outs') 

test = lofl[1][0:2,18]
print(test)

