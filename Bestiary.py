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