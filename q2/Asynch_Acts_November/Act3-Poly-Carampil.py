class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

Odysseus = Warrior()
Robin_Hoos = Archer()
Qi = Mage()

Heroes = [Odysseus, Robin_Hoos, Qi]

for hero in Heroes:
    perform_move(hero)
    
