from Bestiary import *
import random

class Item:
    def __init__(self,name,t):
        self.name = ''
        self.item_type = t

class Consumable(Item):
    def __init__(self,name,h,g):
        Item.__init__(self,name,0)
        self.hp = h
        self.glucose = g

class Equipment(Item):
    def __init__(self,name,a,d):
        Item.__init__(self,name,1)
        self.knowledge = a
        self.immune = d

class Player:
    def __init__(self):
        self.name = ''
        self.level = 1
        self.hp = 10
        self.glucose = 10
        self.adrenaline = 0
        self.knowledge = 10
        self.immune = 10
        self.inventory = []
        self.equipment = []
        self.xp = 0
    
    def pickup(self,item):
        self.inventory.append(item)
    
    def use(self,index):
        pass
    
    def attacked(self,other_attack):
        damage = other_attack/self.immune
        self.hp -= damage
        return damage
    
    def getXP(self,xp):
        self.xp += xp
        if xp >= 5*self.level**2:
            xp -= 5*self.level**2
            self.level += 1
            return 1
        return 0

player = Player()

print 'Hello there! Welcome to the world of SciBowl!\n\
My name is Tracey! People call me the SciBowl Prof!\n\
This world is inhabited by creatures called Scibowlers!\n\
For some people, SciBowlers are students. Others use them for fights.\n\
Myself...I study SciBowl as a profession.\n'
print 'First, what is your name?'

raw_input('')

print '\nI don\'t care, your name is Linnaeus.'

player.name = 'Linnaeus'

rick_perry = RickPerry()

print 'Now fight Rick Perry.'
while player.hp > 0:
    raw_input('Action: ')
    print rick_perry.name,'took',rick_perry.attacked(player.knowledge,10),'damage'
    if random.randint(0,1) == 1:
        print rick_perry.name,'dealt',player.attacked(rick_perry.knowledge),'damage'
    else:
        print rick_perry.name,'missed'

print 'You lose!'