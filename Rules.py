import typing
import random
from ..AutoWorld import World, WebWorld
from BaseClasses import CollectionState
from ..generic.Rules import set_rule, forbid_item
from .names.Characters import CharacterName, getCharacterList
from .Options import MeleeSlippiOptions

def win_with_each_character(world: World, options: MeleeSlippiOptions, state: CollectionState, player: int):
    # Shuffle up our characters - sanity to make sure we don't do this alphabetically or tier order or something
    shuffled_characters = getCharacterList()
    random.shuffle(shuffled_characters)
    cur_total_win_count = 0
    
    # We need to be able to win with as many characters as we have unlocked
    for character in shuffled_characters:
        if character.is_valid_for_run(options) and state.has(f"{character.name}", player):
            cur_total_win_count += 1
    
    return cur_total_win_count >= options.total_character_wins_needed.value
        
def set_rules(world: World, options, player):
    
    for character in getCharacterList():
        # Ignore invalid characters
        if not character.is_valid_for_run(options):
            continue

        for number in options.wins_needed.value:
            forbid_item(world.get_location(f"{character.name} {number} Wins", player), character.name, player)
            set_rule(world.get_location(f"{character.name} {number} Wins", player), lambda state, character=character.name: state.has(character, player))

    world.completion_condition[player] = lambda state: win_with_each_character(world, options, state, player)