from hut import Hut, create_unit
from functions import print_bold, print_dotted_line, show_health, \
    print_wave_line
from knight import Knight
from uniterror import HutNotNumberError, HutOutRangeError


class OrGame():
    """
    The Game Class , mainly
    """

    def __init__(self, hut_numbers=5):
        """get the game ready with scenario ready, default have 5huts.

        :param hut_numbers: in the game, how many huts
        :type hut_numbers: int
        """
        self.acquired_all_huts = False
        self.huts = []
        self.player = None
        self.hut_numbers = hut_numbers

    @property
    def get_occupants(self):
        """Show all huts with it's occupant

        :return: the message each hut with occupant
        :rtype: basestring
        """
        msg = "["
        for hut in self.huts:
            msg += str(hut.number) + ":" + hut.get_occupant_type + ", "
        msg += '\b\b]'
        return msg

    def _process_user_choice(self):
        verifying_choice = True
        idx = 0
        print_dotted_line()
        print("Current Occupants:\n\t%s" % self.get_occupants)
        print_dotted_line()
        while verifying_choice:
            user_choice = input(
                "Choose a hut number to enter(1~" + str(
                    self.hut_numbers) + "):")
            try:
                if not user_choice.isdigit():
                    raise HutNotNumberError(
                        "Your input '{}' is not number.".format(user_choice))

                idx = int(user_choice)
                if idx > self.hut_numbers or idx < 0:
                    raise HutOutRangeError(
                        "input not in range(1~" + str(self.hut_numbers) + ")")

            except HutNotNumberError as e:
                print_wave_line()
                print(e)
                print(e.error_message)
                print_wave_line()
                continue

            except HutOutRangeError as e:
                print_wave_line()
                print(e)
                print(e.error_message)
                print_wave_line()
                continue

            if self.huts[idx - 1].is_acquired:
                print(
                    "You have already acquired this hut. Try again",
                    "<Info:You can NOT get healed in already acquired hut.>"
                )
            else:
                verifying_choice = False

        return idx

    def play(self):
        """
        Workhorse method to play the game....
        Create a Knight instance, create huts and preoccupy them with a game
        Character instance (or leave empty)
        """
        self.setup_game_scenario()

        while not self.acquired_all_huts:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx - 1])

            if self.player.health_meter <= 0:
                print("You Lose :( Better luck next time")
                break

            for hut in self.huts:
                if not hut.is_acquired:
                    break
            else:
                self.acquired_all_huts = True

        if self.acquired_all_huts:
            print_bold("You Win!!! Congratulations!!!!!!")

    def setup_game_scenario(self):
        """
        Create player and huts and then randomly pre-occupy huts...
        """
        self.player = Knight("Sir Foo")
        for number in range(self.hut_numbers):
            self.huts.append(Hut(number + 1, create_unit()))
        self._show_mission()
        # print_bold("Current Occupants:", self.get_occupants)
        show_health(self.player, bold=True, end='\n')

    @staticmethod
    def _show_mission():
        print_dotted_line()
        print_bold("Welcome to Play the Knight Game!", end='\n')
        print_dotted_line()
        print_bold("Mission:")
        print("\t1. Defeat the enemy in any hut")
        print("\t2. Bring all huts in the village under your contral")
