from army import Army
from army import Squad
from units import Soldier
from units import Vehicle
from strategy import strategy

class Game:
    def create_vehicle(self, count_of_operators):
        operators = list()
        for _ in range(count_of_operators):
            operators.append(Soldier())
        return Vehicle(operators)

    def create_squad(self, unit_type, count_of_units, count_of_operators=None):
        unit = list()
        for _ in range(count_of_units):
            if unit_type is Soldier:
                unit.append(unit_type())
            else:
                if count_of_operators is None:
                    print('ERROR! count_of_operators must be a number(1-3)')
                    return None
                if count_of_operators < 1 or count_of_operators > 3:
                    print('ERROR! count_of_operators must be a number 1-3!')
                    return None
                unit.append(self.create_vehicle(count_of_operators))

        return Squad(unit)

    def create_army(self, strat: str,  count_of_soldiers_squads, count_of_vehicle_squads):
        squads = list()
        for _ in range(count_of_soldiers_squads):
            squads.append(self.create_squad(Soldier, 8))
        for _ in range(count_of_vehicle_squads):
            squads.append(self.create_squad(Vehicle, 5, 3))

        return Army(strategy[strat], squads)

    def play(self):
        pass