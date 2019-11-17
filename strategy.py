from army import Army
from army import Squad
from units import Soldier
from random import Random


class Strategy:
    @staticmethod
    def rand(enemy: Army, rand_=Random()):
        squad = rand_.choice(enemy.squads)
        return rand_.choice(squad.units)

    @staticmethod
    def weakest(enemy: Army):
        squad_hp = 10000
        squad = None
        for s in enemy.squads:
            sum = 0
            for unit in s.units:
                sum += unit.hp
            if squad_hp > sum:
                squad = s
                squad_hp = sum

        unit = squad.units[0]
        for u in squad.units:
            if u.hp < unit.hp:
                unit = u
        return unit

    @staticmethod
    def strongest(enemy: Army):
        squad_hp = 0
        squad = None
        for s in enemy.squads:
            sum = 0
            for unit in s.units:
                sum += unit.hp
            if squad_hp < sum:
                squad = s
                squad_hp = sum

        unit = squad.units[0]
        for u in squad.units:
            if u.hp > unit.hp:
                unit = u
        return unit


strategy = {
    'random': Strategy.rand,
    'weakest': Strategy.weakest,
    'strongest': Strategy.strongest
}


