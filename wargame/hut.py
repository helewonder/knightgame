from functions import print_bold


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

    def __init__(self, number, occupant):
        self.occupant = occupant
        self.number = number
        self.is_acquired = False

    def acquire(self, new_occupant):
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
