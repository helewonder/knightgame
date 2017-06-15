import random

from functions import print_bold
from knight import Knight
from orcrider import OrcRider


class Hut():
    """Class to create hut object in the game Attack of the Orcs.

    :arg int number: Hut number to be assigned.
    :arg `AbstractRider` occupant: The new occupant of the Hut.

    :ivar int number: A number assigned to this hut.
    :ivar boolean is_acquired: A boolean flag to indicate if the hut is
    acquired. In the current implementation this is viewed from the players
    perspective.
    :ivar AbstractRider occupant: The occupant of this hut. Needs to be an
    instance of a subclass of `AbstractRider`.

    .. seealso:: Where it is used --
        :py:meth: `game.OrGame.setup_game_scenario()`

    """

    def __init__(self, number, occupant=None):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
        """The player take control the target hut

        :param new_occupant:the game player indeed
        :type new_occupant: `knight.Knight`
        """
        self.occupant = new_occupant
        self.is_acquired = True
        print_bold("Good Job! Hut %d acquired" % self.number)

    @property
    def get_occupant_type(self):
        if self.is_acquired:
            occupant_type = 'ACQUIRED'
        elif self.occupant is None:
            occupant_type = 'unoccupied'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type


def create_unit():
    """According to chance in dictionary, choice a unit_type"""
    # a dictionary include the occupant type of friend or enemy
    # maybe better stored in a Json file.
    friend = {
        'friend': 4
    }
    enemy = {
        'enemy': 5
    }
    unoccupied = {
        None: 1
    }
    occupant_class = {
        'friend': Knight,
        'enemy': OrcRider,
        # None: None
    }
    # occupant_type = {
    #     "enemy": enemy,
    #     "friend": friend,
    #     "unoccupied": unoccupied
    # }

    occupant_list = []
    # occupant = random.choice(occupant_type)
    for occupant in (friend, enemy, unoccupied):
        for k, v in occupant.items():
            for i in range(v):
                occupant_list.append(k)

    # occupant_list += [list(k) * v
    #                   for occupant in [friend, enemy, unoccupied]
    #                   for k, v in occupant.items()]
    choice = random.choice(occupant_list)
    if choice is not None:
        return occupant_class[choice](choice)
    else:
        return None
