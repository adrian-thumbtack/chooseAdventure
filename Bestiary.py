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
        Enemy.__init__(self,10)

class Player:
    def __init__(self):
        self.name = ''
        self.level = 1
        self.hp = 10
        self.glucose = 10
        self.adrenaline = 0
        self.knowledge = 10
        self.immune = 10
        self.atp = 0
        self.platelets = 0
        self.starch = 0
        self.xp = 0
    
    def addATP(self):
        self.atp += 1
    
    def addPlatelets(self):
        self.platelets += 1
    
    def addStarch(self):
        self.starch += 1
    
    def attacked(self,other_attack):
        damage = other_attack/self.immune
        self.hp -= damage
        return damage
    
    def giveXP(self,xp):
        self.xp += xp
        if xp >= 10*self.level**2:
            xp -= 10*self.level**2
            self.level += 1
            return 1
        return 0