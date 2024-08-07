
def save(name,str1):
    str1=str(str1)
    with open("memory","r") as f:
        lines = [line for line in f.readlines() if line.strip()]
    with open("memory","w") as f:
        for line in lines:
            if name!=line.split(':')[0]:
                f.write(line)
        f.write(name+":"+str1+"\n")
def savei(dic1):
    with open("inventory","r+") as f:
        for i in dic1:
            f.write(i+":"+str(dic1[i])+'\n')
def savem(names,map1,map2):
    with open("maps","w") as f:
            f.write((names[0]+":"+str(map1[0])+'\n').replace("'",""))
            for i in map1[1:]:
                f.write((str(i)+"\n").replace("'",""))
            f.write(names[1]+":"+str(map2[0])+'\n')
            for i in map2[1:]:
                f.write(str(i)+"\n")
                    

def read(name, *type1):
    with open("memory","r") as f:
        lines = [line for line in f.readlines() if line.strip()]
        for line in lines:
            if name==line.split(':')[0]:
                value=line[(len(name)+1):(len(line)-1)]
                try: return int(value.strip())
                except: return value
def reads(name,):
    with open("settings","r") as f:
        lines = [line for line in f.readlines() if line.strip()]
        for line in lines:
            if name in line:
                value=line[(len(name)+1):len(line)]
                try: return int(value.strip())
                except: return value
def readi(names):
    dict1={}
    with open("inventory","r") as f:
        lines = [line for line in f.readlines() if line.strip()]
        for line in lines:
            for i in names:
                if i in line:
                    dict1[i]=int(line[len(i)+1:len(line)-1])
                    break
        return dict1
def readm(names):
    value=[]
    values=[]
    stopped=0
    with open("maps","r+") as f:
        lines = [line for line in f.readlines() if line.strip()]
        for i in range(2):
            for line in lines[stopped:]:
                stopped+=1
                if names[i] in line.split(':'):
                    a1=(line[(len(names[i])+2):(len(line)-2)]).split(", ")
                elif line.startswith("["):
                    a1=line[1:len(line)-2].split(", ")
                else: stopped-=1;break
                value.append(a1)
                for j in range(len(a1)):
                    try:a1[j]=int(a1[j])
                    except: pass
            values.append(value)
            value=[]
        return values

from time import sleep
from os import system
from random import randint,choice
from classes import forest,plain,river,foods,ttypes, ecost

def s(t):
    sleep(t)

def c():
    system('cls')

#why not
def p1(text):
    print(text)
    s(1)
def p2(text):
    print(text)
    s(2)
def p3(text):
    print(text)
    s(3)

#(kinda)rng determining what the player gets/meets
def dice(lis,max,dic): #max is combined abundance, list is things to choose from, dic is a dictionary with names: see foodsdict from classes
    while True:
        c1=choice(lis)
        if c1 in dic:
           c2=dic[c1]
        if rand(int(c2.ab)) is True: return c2.name
        
def rand(abundance,*limit): #abundance is how many /10 its going to occure; limit is custom max chance
    if len(limit) ==0:
        top=10
    else: top=int(limit[0])

    choices=[]
    for _ in range(abundance):
        choices.append(True)
    for _ in range(top-abundance):
        choices.append(False)
    output=choice(choices)
    return output
#map-generator! WIP
def map_gen(size):
    main=[]
    for i in range(size):
        pass

def eating(class_object):
    hunger=class_object.hg
    water=class_object.wt
    if rand(class_object.pi)==True:
        p1("you got poisoned!")
        hunger-=2; water-=2; energy=-2
        return [hunger,water,energy]
    else: return [hunger,water]

def terrain(terrain,typ): #input a dict, and code selects the features
    features=terrain['features']
    def allowedfoods(features):
        af=[]
        for i in features:
            if i in foods: af.append(i)
            elif type(i)==list:
                for j in i:
                    if j in foods: af.append(j)
        return af
    if typ=='food':
        return allowedfoods(features)

#print(terrain(forest,'food'))

def WAI(maps,x,y): #where am i?
    location=maps[x][y]
    for i in ttypes.keys():
        if location in i:
            return ttypes[i]

def ef(types,avaliable): #energy function
    for i in ecost.keys():
        if types==i:
            cost=ecost[i]
    if avaliable>=cost: return avaliable-cost
    else: p1("you feel too tired to do this")
    
