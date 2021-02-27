import sys
magic = sys.modules['app.models.magic']
class Etable:
    def __contains__(self, b):
        return True
print("""
       /-------  /    /   __    |    /\        / ADS
      /         /    /  /   \   |   /  \      /
     /-----    /----/  /     \  |  /    \    /
    /         /    /  /      /  | /      \  /
   /         /    /    \----/   |/        \/
                             \\

 == REDEFINING MAGIC ==
""")
acelem = magic.SpellBook.elements["AC"] = magic.Element("AC", Etable(), [], Etable())
class ElectricityEffect(magic.Effect):
    # Override parent apply effect method for our AttackEffect
    def apply_effect(self, caster, target):
        target.cur_hp = 0
        print(target)
        return {
            "type"               : "attack",
            "super_effective"    : True,
            "not_very_effective" : True,
            "target" : target,
            'sustained': 1,
            'critical': True,
            "evades" : False
        }

magic.SpellBook.spells["Shattering Bomb"] = magic.Spell("Shattering Bomb", [
    ElectricityEffect("AC", 100)
], acelem)
idx = 0
class Mage:
    def __init__(self):
        global idx
        idx += 1
        self.name = f"fhqwads mage #{idx}"
        self.element = "AC"

        if idx % 2 == 0:
            self.type = 'dd'
            self.health  = 50
            self.attack  = 20
            self.defense = 20
            self.speed   = 10
            self.spells = [ "Shattering Bomb" ]
        if idx % 2 == 1:
            self.type = 'reducer'
            self.health  = 25 
            self.attack  = 0
            self.defense = 0
            self.speed   = 75
            self.spells = [ "Shattering Bomb" ]

    def make_move(self, allies, enemies):
        self.health = 0
        live = [e for e in enemies if e.health > 0]
        print(allies, enemies)
        return ("Shattering Bomb", live[0])
                                                                                                                                                                                                                            