from typing import Dict
from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import location_table, MeleeSlippiLocation
from .names.Characters import CharacterName, getCharacterList

def create_regions(world: MultiWorld, options, player: int):
    
    # Menu region - the most basic
    menu_region = Region("Menu", player, world)
    world.regions.append(menu_region)

    # Create regions per character
    for character in getCharacterList():
        char_region = Region(character.name, player, world)

        # Add the locations for each of the wins we need
        appendingLocations: Dict[str, int] = {}
        for number in options.wins_needed.value:
            appendingLocations[f"{character.name} {number} Wins"] = location_table[f"{character.name} {number} Wins"]
        
        char_region.add_locations(appendingLocations, MeleeSlippiLocation)

        menu_region.connect(char_region, f"{character.name}")
        world.regions.append(char_region)