from dataclasses import dataclass
from Options import PerGameCommonOptions, OptionList, ItemSet, Choice, Range

class StartingCharacters(ItemSet):
    display_name = "Starting Characters"
    default = set()

class ExcludedCharacters(ItemSet):
    display_name = "Excluded Characters"
    default = set()

class IncludedCharacters(ItemSet):
    display_name = "Included Characters"
    default = set()

class WinsNeeded(OptionList):
    display_name ="Wins Needed per Check"
    default = [1, 2, 3]

class TotalCharacterWinsNeeded(Range):
    display_name = "Total Characters to meet required wins"
    default = 0
    range_start = 0
    range_end = 26

class RequiredWinsPerCharacter(Range):
    display_name = "Required wins per character"
    default = 1
    range_start = 1
    range_end = 10

class RunDifficulty(Choice):
    display_name = "Run Difficulty"
    default = 0
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
    total_character_wins_needed: TotalCharacterWinsNeeded
    required_wins_per_character: RequiredWinsPerCharacter