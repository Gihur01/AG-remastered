#oh boy...
#■□◧
from modules import reads
timea=['■ □ □ □ □ □','□ ■ □ □ □ □','□ □ ■ □ □ □','□ □ □ ■ □ □','□ □ □ □ ■ □','□ □ □ □ □ ■']
timeb=['dawn','morning','noon','afternoon','evening','night']
mh=reads('max_hunger',)
mw=reads('max_water')
print(type(mh))
hunger_value=[(' ■'*i)+(' □'*(mh-i)) for i in range(0,(mh+1))]
water_value=[' ■'*i+' □'*(mw-i) for i in range(0,(mw+1))]

def mapsd(): #default map
    #general map
    maps=[['p','p','f','f','r'],
        ['p','p','f','r','p'],
        ['p','f','f','r','f'],
        ['f','f','f','f','r'],
        ['f','p','p','f','f']]
    #explored map
    emap=[[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
    return maps,emap