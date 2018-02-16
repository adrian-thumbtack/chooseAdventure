class Enemy:
    name = 'Scientist'
    attack = 'scientificate'
    def __init__(self,l):
        self.hp = 10*l
        self.knowledge = l**2
        self.immune = l**2
        self.xp = 10*l
        self.level = l
        self.power = 10
        
    def attacked(self,other_attack,other_power):
        damage = other_power*other_attack/self.immune
        self.hp -= damage
        return damage

class Physicist(Enemy):
    name = 'Physicist'
    attack = 'physicificate'
    def __init__(self,l):
        Enemy.__init__(l)

class Chemist(Enemy):
    name = 'Chemist'
    attack = 'chemistrificate'
    def __init__(self,l):
        Enemy.__init__(l)

class Biologist(Enemy):
    name = 'Biologist'
    attack = 'biologificate'
    def __init__(self,l):
        Enemy.__init__(l)

class Astronomer(Enemy):
    name = 'Astronomer'
    attack = 'astronomificate'
    def __init__(self,l):
        Enemy.__init__(l)

class Geologist(Enemy):
    name = 'Geologist'
    attack = 'rockificate'
    def __init__(self,l):
        Enemy.__init__(l)

class Mathematician(Enemy):
    name = 'Mathematician'
    attack = 'mathematificate'
    def __init__(self,l):
        Enemy.__init__(l)

class RickPerry(Enemy):
    name = 'Rick Perry'
    attack = 'frack'
    def __init__(self):
        Enemy.__init__(self,1000,100,100,1)

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