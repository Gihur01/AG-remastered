
if __name__ == '__main__':
    from random import randint
    from modules import *
    from thewordybits import *
    from art import *
    from classes import *

    
    #initialisation
    energy=int(reads("bonus energy"))
    if read("firstboot")!="True" and input("save detected. load?")!='no': 
        mapls=readm(['maps','emap']); maps=mapls[0]; emap=mapls[1]
        hunger=read('hunger'); water=read('water'); esum=read('energy'); gtime=read('global_time'); time=read('time'); day=read('day')
        x=read('x'); y=read('y')
        inv=readi(itemslist)
    else:
        if read("firstboot")=="True":
            intro(); tut()
        mapls=mapsd(); maps=mapls[0]; emap=mapls[1]; savem(['maps','emap'],maps,emap)
        day=1; time=0; gtime=0; hunger=6; water=5
        tenergy=evalues[timeb[time]]
        esum=int((energy+tenergy)*(1+(0.1*hunger))//1)-(2*(5-water))
        x=2;y=2
        inv={}
        save('hunger',hunger); save('water',water);save('energy',esum);save('global_time',gtime);save('day',day);save('time',time);save('x',x)
        save('y',y);savem(['maps','emap'],maps,emap);savei(inv)

    #actual game
    c()
    IAH=WAI(maps,x,y) #i am here!
    def timep(): #time pass function, for conviniency
        global time, day, hunger, water, esum, gtime
        gtime +=1
        if time !=4:
            time+=1
        else: 
            slip=input("sleep?")
            if slip!='no':
                day+=1;time=0
            else: 
                time+=1
        if hunger!=0 and water!=0:
            if esum >1: hunger-=1; water-=1
            elif hunger-2>=0 and water-2>=0: hunger-=2; water-=2
            else: 
                if hunger>water: water=0
                else: hunger=0
        else: #athetic purposes
            if hunger==0: reason='starvation'
            else: reason='thirst'
            die(reason, day)
        tenergy=evalues[timeb[time]]
        esum=int(((energy+tenergy)*(1+(0.1*hunger))//1)-(4-water))

    def ea(): #energy assignment
        global esum
        try: int(ee)
        except: return False
        esum=ee

        

    while True:
        #main game loop
        c()
        print(' day:',day,'\n',timea[time],"\n",timeb[time])
        if hunger > mh: hunger=mh
        if water > mw: water=mw
        print('hunger:%s\nwater:%s\nenergy: %s' % (hunger_value[hunger],water_value[water],esum))
        a=input()
        #actions
        if a=='i': #inventory
            for i in inv:
                p(i,":",inv[i])
            b=input("action?")
            kwords=b.split()
            for j in kwords:
                try: num=int(j)
                except: pass

            for j in kwords:  
                if j in ['use','consume','absorb','swallow','eat']:
                    ee=ef('eat',esum) 
                    if ea()!=False:
                        for i in foodsdict.keys():
                            if i in b:
                                try: int(num)
                                except: num=1
                                try: temp=inv[i]
                                except: p1('you dont have that!'); break
                                if num<=inv[i]: inv[i]-=num
                                else: num=inv[i]; p1("thats too much! i assume you mean eat all :)"); inv[i]-=num
                                if inv[i]==0: inv.pop(i)
                                for _ in range(num):
                                    temp=eating((foodsdict[i]))
                                    hunger=hunger+temp[0]; water=water+temp[1]
                                break
                if j in ['back','quit','exit','close','']: break
                
        if a=='m':
            vmap=[] #visual map
            
            for i in range(len(maps)):
                line=[' ']*len(maps)
                for j in range((len(maps[i]))):
                    try:
                        if emap[i][j]==1:
                            line[j]=(maps[i][j])
                    except: break
                vmap.append(line)
            for i in vmap:
                p(i)
            b=input()      

        if a=='f': #find food funtion
            ee=ef('ff',esum) 
            if ea()!=False:
                localfoods=terrain(IAH,'food')
                ff=dice(localfoods,11+int(reads("food_abundance")),foodsdict)
                for i in range(len(localfoods)): 
                    if ff==localfoods[i]: break
                if ff!='nothingf': 
                    b=input("you found a %s, eat now?" % (ff))
                    if b=='yes': 
                        temp=eating((foodsobj[i]))
                        hunger=hunger+temp[0]; water=water+temp[1]; 
                        try:energy=energy-temp[2]
                        except: pass
                    else: 
                        try: inv[ff]+=1
                        except: inv[ff]=1
                else: p1("you got nothing.")
        
        if a=='d':
            if IAH["name"]!='river':
                p1("there is no water nearby!")
            else:
                ee=ef('drink',esum) 
                if ea()!=False:
                    water+=5


        if a=='e': #explore
            while True:
                y1=y; x1=x
                b=input("which direction do you want to explore?")
                if b=='w':
                    y1-=1
                if b=='e':
                    y1+=1
                if b=='n':
                    x1-=1
                if b=='s':
                    x1+=1
                try: tile=maps[x1][y1]; break
                except:p1("you shouldn't go too far from the crash site!"); break
                
            if emap[x1][y1]==1:
                ee=ef('walk',esum)
            else: ee=ef('explore',esum)
            if ea()!=False:
                x=x1; y=y1
                for i in ttypes.keys():
                    if maps[x][y]==i:
                        IAH=ttypes[i]; break
                p1("you entered a %s!" %(IAH['name']))
                emap[x][y]=1
        
        if a in [' ','pass','p','rest','r','next','n'] or (esum<=1 and inv.keys()==0):
            timep()
        
        if gtime%12==0 and gtime!=0 or a in ['s','save']:
            save('hunger',hunger)
            save('water',water)
            save('energy',esum)
            save('global_time',gtime)
            save('day',day)
            save('time',time)
            save('x',x)
            save('y',y)
            savem(['maps','emap'],maps,emap)
            savei(inv)
            p1("save success!")
