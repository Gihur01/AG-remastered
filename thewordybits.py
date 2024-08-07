from modules import *
from sys import exit
p=print
def intro():
    p("backstory:\nyour plane crashed over a deserted patch of forest, in the middle of nowhere."\
        "\nbefore the impact you only heard that the captain call out mayday, with the vague numbers: 66,173...")
    s(3)
    p("you are the only survivor... now you must thrive in this wasteland and hold out before rescue comes!")
    save("firstboot",False)
def tut():
    s(2)
    p1("tutorial:")
    p2("this is a turn-based word survival game, where you control your character to explore, hunt, gather resources, and survive!")
    p2("each day you have certain amout of energy, determined by your stats, which you can use to do things.")
    p2("activities:\nfind food: f\ndrink: d (only in river tiles)\nexplore: e")
    p2("inventory: i\nview map: m\nsave game: s")
    p2("as your progress more activities will unlock...")
    p("now let your adventure start!")


def die(*causes):
    p2("unfortunatly, you didn't manage to survive...")
    for i in causes: 
        if type(i) == int: day=i
        if type(i) == str: death=i
    p2("survived until: day %s,\ncause of death: %s" % (day, death))
    _=input("press anything to end")
    exit()
    