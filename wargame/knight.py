import random
from functions import print_bold, print_dotted_line, show_health
from rider import AbcRider
from hut import Hut


class Knight(AbcRider):
    def __init__(self, name, max_hp=40):
        self.name = name
        self.health_meter = max_hp
        self.max_hp = max_hp
        if self.name != 'Sir Foo':
            self.unit_type = "friend"
            self.self_heal = False
        elif self.name == 'Sir Foo':
            self.unit_type = 'player'
            self.self_heal = True

    def attack(self, combatant):
        if self.self_heal:
            self.heal()
        hit_list = ['player'] * 4 + ['enemy'] * 6
        injured_unit = random.choice(hit_list)
        injury = random.randint(10, 15)
        if injured_unit == 'player':
            self.health_meter = max(self.health_meter - injury, 0)
        elif injured_unit == 'enemy':
            combatant.health_meter = max(combatant.health_meter - injury, 0)
        show_health(self)
        show_health(combatant)

    def heal(self, by=2, full_heal=False):
        if self.health_meter == self.max_hp:
            return
        if full_heal:
            self.health_meter = self.max_hp
            print_bold("You are HEALED!", end=' ')
            show_health(self, bold=True)
            print()
        else:
            self.health_meter = min(self.max_hp, self.health_meter + by)

    def run_away(self):
        pass

    def acquire_hut(self, hut):
        print_bold("Entering hut %d..." % hut.number, end='')
        is_enemy = (isinstance(hut.occupant, AbcRider)
                    and hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'
        if is_enemy:
            print("Enemy sighted!")
            show_health(self, bold=True)
            show_health(hut.occupant, bold=True)
            while continue_attack:
                continue_attack = input("......Continue Attack?(y/n):")
                if continue_attack == 'n':
                    self.run_away()
                    break
                else:
                    continue_attack = 'y'

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break

                if self.health_meter <= 0:
                    print("")
                    break

        else:
            if hut.get_occupant_type == 'unoccupied':
                print_bold("Hut is unoccupied")
            else:
                print_bold("Friend sighted!")
            hut.acquire(self)
            self.heal(full_heal=True)
