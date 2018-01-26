class Enemy:
    name = 'Enemy'
    def __init__(self,h,k,i,x):
        self.hp = h
        self.knowledge = k
        self.immune = i
        self.xp = x
        
    def attacked(self,other_attack,other_power):
        self.hp -= other_power*other_attack/self.immune