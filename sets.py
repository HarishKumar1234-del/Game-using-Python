mutex,db,rc=(1,1,0)
Dict={}
Qlist=[]
def wait(param):
    param-=1  

    if param<0:
        #Put process PCB in suspended state
        Qlist.push(index)
        return param,False

    else:
        return param,True

def signal(param):
    param+=1
    if param<=0:
        Qindex=Qlist.pop(0)
        return param,Qindex

def read(index,burst):
    while(True):
        mutex=wait(mutex,index)
        rc+=1

        if rc==1:
            db=wait(db,index)

        mutex=signal(mutex)

        #

        mutex=wait(mutex,index)

        rc-=1

        if rc==0:
            db=signal(db)

        mutex=signal(mutex)

def write(index):
    while True:
        db=wait(db,index)

        #

        db=signal(db)


print('Enter r/w , burst, arrival')
for _ in range(10):
    rw,burst,aT=input().split()
    Dict[aT]=(rw,burst)


maxTime=max([Dict.keys])

t,i=0,0
while t<=maxTime:
    try:
        if Dict[t][0]=='R':
            read(i,Dict[t][1])
        else:
            write(i,Dict[t][1])

        i+=1
    except:
        pass

