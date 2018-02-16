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