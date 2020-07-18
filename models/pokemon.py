class Pokemon:

    def __init__(self, name, pkmnType, level, attacks, aka = None,):
        self.name = name
        self.aka = aka if aka != None else name 
        self.type = pkmnType
        self.level = level
        self.attacks = attacks

    def describePokemon(self):
        print('I chose the {} type, {}, with level {}.'.format(self.type.name , self.name, self.level))

    def printAttacks(self):        
        stringAttacks = ''
        for currentAttack in self.attacks:
            stringAttacks += currentAttack + ', '
        
        lenght = len(stringAttacks)

        stringAttacks = stringAttacks[:lenght-2]
        return stringAttacks