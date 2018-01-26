class Enemy:
    name = 'Enemy'
    def __init__(self,h,k,i,x):
        self.hp = h
        self.knowledge = k
        self.immune = i
        self.xp = x
        
    def attacked(self,other_attack,other_power):
        damage = other_power*other_attack/self.immune
        self.hp -= damage
        return damage

class RickPerry(Enemy):
    name = 'Rick Perry'
    def __init__(self):
        Enemy.__init__(self,1000,100,100,1)