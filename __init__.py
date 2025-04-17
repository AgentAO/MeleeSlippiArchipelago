import random
from typing import List
from BaseClasses import MultiWorld
from .Regions import create_regions
from .Locations import MeleeSlippiLocation, location_table
from ..AutoWorld import World, WebWorld
from .Items import MeleeSlippiItem, item_data, item_data_table
from .Options import MeleeSlippiOptions
from .names.Characters import getCharacterList
from .Rules import set_rules

class MeleeSlippiWeb(WebWorld):
    game: str = "Melee Slippi"

class MeleeSlippiWorld(World):
    """For playing Melee on Slippi"""
    
    game: str = "Melee Slippi"
    web = MeleeSlippiWeb()
    options_dataclass = MeleeSlippiOptions  
    options: MeleeSlippiOptions
    item_name_to_id = item_data
    location_name_to_id = location_table
    topology_present = True  # show path to required location checks in spoiler
    starting_character = None

    # area_connections: Dict[int, int]
    # area_cost_map: Dict[int,int]

    def generate_early(self):
        seenNumbers = set()
        for number in self.options.wins_needed.value:
            if number < 1 or number > 10:
                raise Exception("Wins Needed can only be from 1 to 10")
            elif number in seenNumbers:
                raise Exception("Wins Needed can not have duplicate numbers")
            else:
                seenNumbers.add(number)

    def create_item(self, name: str) -> MeleeSlippiItem:
        return MeleeSlippiItem(name, item_data_table[name].type, item_data_table[name].id, self.player)

    def create_items(self) -> None:
        #randomly determine starting character
        self.starting_character = random.choice(getCharacterList())

        item_pool: List[MeleeSlippiItem] = []
        for name, item in item_data_table.items():
            if item.id and name != "Trophy" and name != self.starting_character["name"]:
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

        # We have extra slots to fill - for each win per player, there will be an extra spot. Take our starting character out of the pool as well
        fill_count = (len(getCharacterList()) * len(self.options.wins_needed.value) - len(getCharacterList())) + 1

        self.multiworld.itempool += [self.create_item("Trophy") for i in range(0,fill_count)]
    
    def get_filler_item_name(self) -> str:
        return "Trophy"
    
    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)

    def pre_fill(self):
        self.multiworld.push_precollected(self.create_item(self.starting_character["name"]))