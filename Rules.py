import typing
from ..AutoWorld import World, WebWorld
from BaseClasses import CollectionState
from ..generic.Rules import set_rule, forbid_item
from .names.Characters import CharacterName, getCharacterList
from .Options import MeleeSlippiOptions

def win_with_each_character(world: World, options: MeleeSlippiOptions, state: CollectionState, player: int):
    for character in getCharacterList():
        if character.is_valid_for_run(options) and not state.has(f"{character.name}", player):
            return False
    
    return True
        
def set_rules(world: World, options, player):
    
    for character in getCharacterList():
        # Ignore invalid characters
        if not character.is_valid_for_run(options):
            continue

        for number in options.wins_needed.value:
            forbid_item(world.get_location(f"{character.name} {number} Wins", player), character.name, player)
            set_rule(world.get_location(f"{character.name} {number} Wins", player), lambda state, character=character.name: state.has(character, player))

    world.completion_condition[player] = lambda state: win_with_each_character(world, options, state, player)