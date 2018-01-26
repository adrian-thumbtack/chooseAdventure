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
    
    def pickup(self,item):
        self.inventory.append(item)
    
    def use(self,index):
        pass
    
    def attacked(self,other_attack,other_power):
        self.hp -= other_power*other_attack/self.immune

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

