class Enemy:
    name = 'Enemy'
    def __init__(self,l):
        self.hp = 10*l
        self.knowledge = l**2
        self.immune = l**2
        self.xp = 10*l
        self.level = l
        
    def attacked(self,other_attack,other_power):
        damage = other_power*other_attack/self.immune
        self.hp -= damage
        return damage

class RickPerry(Enemy):
    name = 'Rick Perry'
    def __init__(self):
        Enemy.__init__(self,1000,100,100,1)