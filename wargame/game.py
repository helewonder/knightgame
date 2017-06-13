import random
from functions import print_bold, print_dotted_line, show_health
from knight import Knight
from orcrider import OrcRider
from hut import Hut
from uniterror import HutNotNumberError, HutOutRangeError


class OrGame():
    def __init__(self, hut_numbers=5):
        self.huts = []
        self.player = None
        self.hut_numbers = hut_numbers

    @property
    def get_occupants(self):
        msg = "["
        for hut in self.huts:
            msg += str(hut.number) + ":" + hut.get_occupant_type + ", "
        msg += '\b]'
        return msg

    def _process_user_choice(self):
        verifying_choice = True
        idx = 0
        print("Current occupants: %s" % self.get_occupants)
        while verifying_choice:
            user_choice = input(
                "Choose a hut number to enter(1~" + str(self.hut_numbers) + "):")
            try:
                if not user_choice.isnumber():
                    raise HutNotNumberError(
                        "Your input {} is not number.".format(user_choice))

                idx = int(user_choice)
                if idx > self.hut_numbers or idx < 0:
                    raise HutOutRangeError(
                        "input not in range(1~" + str(self.hut_numbers))

            except HutNotNumberError:
                break

            except HutOutRangeError:
                break

            if self.huts[idx - 1].is_acquired:
                print(
                    "You have already acquired this hut. Try again",
                    "<Info:You can NOT get healed in already acquired hut.>"
                )
            else:
                verifying_choice = False

        return idx

    def _occupy_huts(self):
        occupants = [None, 'friend', 'enemy']
        for i in range(self.hut_numbers):
            occupant = random.choice(occupants)
            if occupant == 'enemy':
                self.huts.append(Hut(i + 1, OrcRider('enemy' + str(i + 1))))
            elif occupant == 'friend':
                self.huts.append(Hut(i + 1, Knight('knight' + str(i + 1))))
            else:
                self.huts.append(Hut(i + 1, None))

    def play(self):
        self.player = Knight("Sir Foo")
        self._occupy_huts()
        acquired_all_huts = False

        self._show_mission()
        print_bold("Current Occupants:", self.get_occupants)
        show_health(self.player, bold=True, end='\n')

        while not acquired_all_huts:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx - 1])

            if self.player.health_meter <= 0:
                print("You Lose :( Better luck next time")
                break

            for hut in self.huts:
                if not hut.is_acquired:
                    break
            else:
                acquired_all_huts = True

        if acquired_all_huts:
            print_bold("You Win!!! Congratulations!!!!!!")

    @staticmethod
    def _show_mission():
        print_dotted_line()
        print_bold("Welcome to Play the Knight Game!", end='\n')
        print_dotted_line()
        print_bold("Mission:")
        print("\t1. Defeat the enemy in any hut")
        print("\t2. Bring all huts in the village under your contral")
