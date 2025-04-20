import random
from typing import List
from BaseClasses import MultiWorld
from .Regions import create_regions
from .Locations import MeleeSlippiLocation, location_table
from ..AutoWorld import World, WebWorld
from .Items import MeleeSlippiItem, item_data, item_data_table
from .Options import MeleeSlippiOptions, RunDifficulty
from .names.Characters import getCharacterList, Character
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
    starting_characters = {}
    valid_characters = set()

    # area_connections: Dict[int, int]
    # area_cost_map: Dict[int,int]

    # Pre generation checks - mostly sanity checks
    def generate_early(self):
        seenNumbers = set()
        
        # Check if wins needed is empty
        if len(self.options.wins_needed.value) == 0:
            raise Exception("Wins Needed can not be empty")
        
        # Ensure wins needed has no dupes
        # (we're using a list because the set option doesn't take numbers)
        for number in self.options.wins_needed.value:
            if number < 1 or number > 10:
                raise Exception("Wins Needed can only be from 1 to 10")
            elif number in seenNumbers:
                raise Exception("Wins Needed can not have duplicate numbers")
            else:
                seenNumbers.add(number)

        # Check valid difficulty setting
        if self.options.run_difficulty > RunDifficulty.option_impossible or self.options.run_difficulty < RunDifficulty.option_default:
            raise Exception(f"Run difficulty must be from {RunDifficulty.option_default} to {RunDifficulty.option_impossible}")
        
        # Check we're not including an excluded character
        for character in self.options.excluded_characters.value:
            if character in self.options.included_characters.value:
                raise Exception("You can not include and exclude the same character")
            if character in self.options.starting_characters.value:
                raise Exception("You can not start on an excluded character")
        
        # Determine our valid characters for this run based on whether or not they're in the difficulty setting
        self.valid_characters = [character for character in getCharacterList() if character.is_valid_for_run(self.options) is True]

        if len(self.valid_characters) == 0:
            raise Exception("No characters are valid under current settings")

    # Func to create one item
    def create_item(self, name: str) -> MeleeSlippiItem:
        return MeleeSlippiItem(name, item_data_table[name].type, item_data_table[name].id, self.player)

    # Fills the pool with items - checking options, character validtity, and adding fillers.
    def create_items(self) -> None:
        # Get Names for valid characters
        valid_character_names = [character.name for character in self.valid_characters]

        if len(self.options.starting_characters.value) > 0:
            self.starting_characters = self.options.starting_characters.value
        else:
            # else, randomly determine starting character from our legal character pool
            randStartingCharacter: Character = random.choice(self.valid_characters)
            self.starting_characters = {randStartingCharacter.name}

        item_pool: List[MeleeSlippiItem] = []
        for name, item in item_data_table.items():
            if item.id and name != "Trophy" and name not in self.starting_characters and name in valid_character_names:
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

        # We have extra slots to fill - for each win per player, there will be an extra spot. Take our starting characters out of the pool as well if any of them were valid to play
        fill_count = (len(getCharacterList()) * len(self.options.wins_needed.value) - len(self.valid_characters)) + len([character for character in self.starting_characters if character in valid_character_names])

        self.multiworld.itempool += [self.create_item("Trophy") for i in range(0,fill_count)]
    
    # Filler item - "trophy" for now
    def get_filler_item_name(self) -> str:
        return "Trophy"
    
    # Create regions
    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)

    # Create rules
    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)

    # Before filling - give us pre-unlocked characters
    def pre_fill(self):
        # Prefill all the starting characters chosen
        for character in self.starting_characters:
            self.multiworld.push_precollected(self.create_item(character))
    

    def fill_slot_data(self):
        # Send over some information to the server that the game client will need to know
        data_dict = self.options.as_dict("wins_needed")
        data_dict["valid_characters"] = [character.name for character in self.valid_characters]
        return data_dict