from dataclasses import dataclass
from Options import PerGameCommonOptions, OptionList

class WinsNeeded(OptionList):
    default = [1, 2, 3]

@dataclass
class MeleeSlippiOptions(PerGameCommonOptions):
    wins_needed: WinsNeeded