from dataclasses import dataclass
from skills import *

@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=150,
    max_stamina=20,
    attack=1,
    stamina=0.9,
    armor=2,
    skill=FuryPunch()
)


TheifClass = UnitClass(
    name="Вор",
    max_health=100,
    max_stamina=15,
    attack=2,
    stamina=0.8,
    armor=0.5,
    skill=HardShot()
)


unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}