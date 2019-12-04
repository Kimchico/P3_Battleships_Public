class ship:
    def __init__(self, health, positions,type): #type is the same as health in the beggining
        self.health = health
        self.positions = positions
        self.isDestroyed = False
        self.type = type
    def check_health(self):
        if self.health==0:
            self.isDestroyed=True
    def get_Type(self):
        if self.type==1:
            return 'Decoy'
        if self.type==2:
            return 'Destroyer'
        if self.type==3:
            return 'Battleship'
        if self.type==4:
            return 'Carrier'
    def get_Positions(self):
        return self.positions