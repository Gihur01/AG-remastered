
itemslist=['berry','apple','pear','mushroom','raw meat','cooked meat','pebble','stick']
foods=['berry','apple','pear','mushroom','nothingf']
# places; abundance/100 (currently no use)
forest={'features':['wood',foods,'animals','mobs'],'abundance':10,'name':'forest'}
plain={'features':['berry','animals'],'abundance':6,'name':'plain'}
river={'features':['water','fish'],'abundance':1,'name':'river'}
#terrain list: for easy access
ttypes={'r':river,'f':forest,'p':plain}
evalues={'dawn':2,'morning':3,'noon':4,'afternoon':4,'evening':3,'night':2} #base energy values
ecost={'eat':1,'explore':6,'walk':2,'ff':2,'drink':1} #energy cost for every action
from modules import reads
class food():
    #hg=hunger, wt=water, pi=poison chance
    def __init__(self,hg, wt,pi,ab,name): 
        self.hg=hg
        self.wt=wt
        self.pi=pi
        self.ab=ab
        self.name=name
berry=food(1,1,2,4,'berry')
apple=food(2,1,0,2,'apple')
pear=food(2,1,0,2,'pear')
mushroom=food(1,1,4,3,'mushroom')
r_meat=food(3,-1,1,0,'r_meat')
c_meat=food(7,0,0,0,'c_meat')
nothingf=food(0,0,0,reads("food_abundance"),'nothingf')
#idk why
foodsobj=[berry,apple,pear,mushroom,nothingf]
#giving things names
foodsdict={'berry':berry,'apple':apple,'pear':pear,'mushroom':mushroom,'nothingf':nothingf,'raw meat':r_meat,'cooked meat':c_meat}
class animals():
    #agility(catch chance), abundance, food points
    def __init__(self,ag,ab,fd):
        self.ag=ag
        self.ab=ab

rabbit=animals(3,4,2)
mouse=animals(4,5,1)
bird=animals(7,3,2)
nothinga=animals(0,0,reads("animal_abundance"))

class mobs():
    # attack, health, abundance
    def __init__(self,at,hp,ab):
        self.at=at
        self.hp=hp

bear=mobs(6,10,1)
tiger=mobs(7,5,1)
nothingm=mobs(0,0,reads("mob_abundance"))

class items():
    def __init__(self):
        # no attributes for now
        pass

stick=items()
pebble=items()
