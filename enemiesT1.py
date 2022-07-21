class Commoner:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 2
        self.goldgain = 10
rank1=Commoner("Commoner Bob")

class Squire:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 20
rank2=Squire("Squire Edon")

class Baron:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 60
        self.health = self.maxhealth
        self.attack = 12
        self.goldgain = 30
rank3=Baron("Baron Rolph")