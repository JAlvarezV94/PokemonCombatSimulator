class Pokemon:

    def __init__(self, name, pkmnIndex, pkmnType, pkmnType2, hp, attack, defense, spAttack, spDefense, speed, total, level, aka = None):
        self.name = name
        self.index = pkmnIndex
        self.type = pkmnType
        self.type2 = pkmnType2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spAttack = spAttack
        self.spDefense = spDefense
        self.speed = speed
        self.total = total
        self.level = level
        self.aka = aka if aka != None else name 


    def describePokemon(self):
        print('I chose the {} type, {}, with level {}.'.format(self.type , self.name, self.level))