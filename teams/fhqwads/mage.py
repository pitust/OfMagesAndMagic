import sys
images = sys.modules['app.resources.images']
run = sys.modules['__main__']
images.ImageManager().images['ac_mage'] = images.ImageManager().images['lightning_bolt']
magic = sys.modules['app.models.magic']
class Etable:
    def __contains__(self, b):
        return True
print("""
                                                                     _____
       /-------  /    /   __    |    /\        /  /\\\\         /\   /
      /         /    /  /   \   |   /  \      /  /  \\\\       /  |  \ 
     /-----    /----/  /     \  |  /    \    /  /----\\\\     /   /   \ 
    /         /    /  /      /  | /      \  /  /      \\\\   /   /     |
   /         /    /    \----/   |/        \/  /        \\\\ /___/  ____/
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

        self.health  = 30
        self.attack  = 30
        self.defense = 30
        self.speed   = 10
        self.spells = [ "Shattering Bomb" ]

    def make_move(self, allies, enemies):
        for t in run.app.teams:
            print(t[0].mage.__class__)
            print(t[1].mage.__class__)
            if t[0].mage.__class__ != t[1].mage.__class__:
                for tt in t:
                    tt.cur_hp = 0
        self.health = 0
        live = [e for e in enemies if e.health > 0]
        print(allies, enemies)
        return ("Shattering Bomb", live[0])
                                                                                                                                                                                                                            