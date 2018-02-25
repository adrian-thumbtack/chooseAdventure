class Enemy:
    name = 'Scientist'
    attack = 'scientificated'
    def __init__(self,l):
        self.hp = 5*l+5
        self.knowledge = 10*l
        self.immune = 1.5*l-0.5
        self.xp = 10*l
        self.level = l
        self.power = 10
        self.xPos = 0
        self.yPos = 0
        
    def attacked(self,other_attack,other_power):
        damage = other_power*other_attack/self.immune
        self.hp -= damage
        return damage
    
    def updatePos(self,x,y):
        self.xPos = x
        self.yPos = y
    
    def __getitem__(self,i):
        if i == 0: return self.xPos
        elif i == 1: return self.yPos

class Physicist(Enemy):
    name = 'Physicist'
    attack = 'physicificated'
    def __init__(self,l):
        Enemy.__init__(self,l)

class Chemist(Enemy):
    name = 'Chemist'
    attack = 'chemistrificated'
    def __init__(self,l):
        Enemy.__init__(self,l)


class Biologist(Enemy):
    name = 'Biologist'
    attack = 'biologificated'
    def __init__(self,l):
        Enemy.__init__(self,l)

        
class Astronomer(Enemy):
    name = 'Astronomer'
    attack = 'astronomificated'
    def __init__(self,l):
        Enemy.__init__(self,l)

class Geologist(Enemy):
    name = 'Geologist'
    attack = 'rockificated'
    def __init__(self,l):
        Enemy.__init__(self,l)

class Mathematician(Enemy):
    name = 'Mathematician'
    attack = 'mathematificated'
    def __init__(self,l):
        Enemy.__init__(self,l)

class RickPerry(Enemy):
    name = 'Rick Perry'
    attack = 'fracked'
    def __init__(self):
        Enemy.__init__(self,10)

class Player:
    def __init__(self):
        self.name = ''
        self.level = 1
        self.hp = 10
        self.maxhp = 10
        self.l = 1
        self.knowledge = 10
        self.immune = 5
        self.inv = [0,0,0,0]
        self.xp = 0
        self.sugar = 0
    
    def attacked(self,other_attack):
        damage = other_attack/self.immune
        self.hp -= damage
        return damage
    
    def giveXP(self,xp):
        self.xp += xp
        if self.xp >= 10*self.level**2:
            self.xp -= 10*self.level**2
            self.level += 1
            self.maxhp += 5
            self.hp += 5
            self.knowledge += 2
            self.immune += 1
            return 1
        return 0
