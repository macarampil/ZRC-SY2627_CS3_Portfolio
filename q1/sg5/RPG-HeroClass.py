# ============================================================
#  RPG Hero — complete the class below.
#  The class name and method names are already set for you;
#  just fill in the bodies marked with TODO.
# ============================================================

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
#---code for taking damage from an attack---#
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
 #--bouns section---#
    def heal(self, amount):
        self.hp += amount

# ------------------------------------------------------------
#  Step 3 — Instantiate two heroes and try them out.
#  Uncomment and complete the lines below once your class works.
# ------------------------------------------------------------
#-----Arthur and Morgana's max health before any damage or healing----#
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)
morgana.take_damage(0)  # Morgana doesn't take any damage
#---result of damage taken by Arthur and Morgana's health after blocking the attack---#
print(f"Arthur was bitten! ({arthur.hp} hp remaining)")    # Expected: 90
print(f"Morgana blocked the attack! ({morgana.hp} hp remaining)")     # Expected: 100
#----result of healing potion used by Arthur and Morgana's health after healing---#
arthur.heal(5)
print(f"Arthur used a healing potion! ({arthur.hp} hp remaining)")         # Expected: 95 
