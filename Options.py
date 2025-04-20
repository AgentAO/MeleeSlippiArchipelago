from dataclasses import dataclass
from Options import PerGameCommonOptions, OptionList, ItemSet, Choice

class StartingCharacters(ItemSet):
    default = set()

class ExcludedCharacters(ItemSet):
    default = set()

class IncludedCharacters(ItemSet):
    default = set()

class WinsNeeded(OptionList):
    default = [1, 2, 3]

class RunDifficulty(Choice):
    option_default = 0 # All characters
    option_super_easy = 1 # S Tier
    option_easy = 2 # A Tier and up
    option_normal = 3 # B Tier and up
    option_hard = 4 # C Tier and up
    option_impossible = 5 # D and F tiers only

@dataclass
class MeleeSlippiOptions(PerGameCommonOptions):
    wins_needed: WinsNeeded
    starting_characters: StartingCharacters
    excluded_characters: ExcludedCharacters
    included_characters: IncludedCharacters
    run_difficulty: RunDifficulty