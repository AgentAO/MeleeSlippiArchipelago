from typing import Dict, NamedTuple
from BaseClasses import Location
from .names.Characters import getCharacterList
from ..AutoWorld import World

class MeleeSlippiLocation(Location):
    game: str = "Melee Slippi"

melee_slippi_base_id: int = 253761962

location_table: Dict[str, int] = {}
for character in getCharacterList():
    for number in range(1, 10):
        location_table[f"{character["name"]} {number} Wins"] = melee_slippi_base_id
        melee_slippi_base_id += 1