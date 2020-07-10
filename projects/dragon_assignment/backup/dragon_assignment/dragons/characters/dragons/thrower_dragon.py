from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        # 1.3 starts here
        if len(self.place.terminators) == 0:
            current=self.place.entrance
            while current.entrance != None:
                if len(current.terminators) != 0:
                    return random_or_none(current.terminators)
                else:
                    current = current.entrance
            return None
        else:
            return random_or_none(self.place.terminators)
            # 1.3 ens here
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
