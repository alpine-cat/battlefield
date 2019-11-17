from units import Unit


class Squad:
    def __init__(self, unit_list):
        self._units = unit_list

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        self._units = units

    def get_active_units(self):
        return [
            op
            for op in self.units
            if op.is_active()
        ]


class Army:
    def __init__(self, srtat, squads):
        self._squads = squads
        self._strategy = srtat

    @property
    def squads(self):
        return self._squads

    @squads.setter
    def squads(self, squads):
        self._squads = squads

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy
