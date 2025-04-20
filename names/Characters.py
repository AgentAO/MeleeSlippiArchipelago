from ..Options import RunDifficulty, MeleeSlippiOptions

class CharacterTier:
    S = 0
    A = 1
    B = 2
    BPLUS = 2
    BMINUS = 3
    C = 4
    CPLUS = 4
    CMINUS = 5
    D = 6
    F = 7

    # Helper function for grabbing grouped tiers, but we can still keep them separated out if needed
    @staticmethod
    def get_tier_class(tierClass: str):
        if tierClass == "S":
            return CharacterTier.S
        if tierClass == "A":
            return CharacterTier.A
        if tierClass == "B":
            return CharacterTier.BMINUS
        if tierClass == "C":
            return CharacterTier.CMINUS
        if tierClass == "D":
            return CharacterTier.D
        if tierClass == "F":
            return CharacterTier.F

class CharacterName:
    MARIO = "Mario"
    DK = "Donkey Kong"
    LINK = "Link"
    SAMUS = "Samus"
    YOSHI = "Yoshi"
    KIRBY = "Kirby"
    FOX = "Fox"
    PIKACHU = "Pikachu"
    NESS = "Ness"
    CF = "Captain Falcon"
    BOWSER = "Bowser"
    PEACH = "Peach"
    IC = "Ice Climbers"
    ZELDA = "Zelda"
    SHEIK = "Sheik"
    LUIGI = "Luigi"
    JIGGLYPUFF = "Jigglypuff"
    MEWTWO = "Mewtwo"
    MARTH = "Marth"
    GW = "Mr. Game & Watch"
    DRMARIO = "Dr. Mario"
    GANONDORF = "Ganondorf"
    FALCO = "Falco"
    YLINK = "Young Link"
    PICHU = "Pichu"
    ROY = "Roy"

class Character:
    id: str
    name: str
    tier: int

    def __init__(self, id, tier):
        if id not in dir(CharacterName):
            raise Exception(f"Character name {id} is invalid")
        
        if tier not in dir(CharacterTier):
            raise Exception(f"Tier {tier} is invalid")
        
        self.id = id
        self.name = getattr(CharacterName,id)
        self.tier = getattr(CharacterTier,tier)

    # Check if the current character is valid in the current difficulty setting
    def is_valid_for_run(self, options: MeleeSlippiOptions):

        # Our starting character is valid
        if self.name in options.starting_characters:
            return True

        # Included characters are always valid
        if self.name in options.included_characters:
            return True
        
        # Excluded characters are never valid
        if self.name in options.excluded_characters:
            return False

        # Difficulty checks
        # On default - all characters are valid
        if options.run_difficulty == RunDifficulty.option_default:
            return True

        # Return true if the character meets conditions
        if options.run_difficulty == RunDifficulty.option_super_easy and self.tier <= CharacterTier.get_tier_class("S"):
            return True
        elif options.run_difficulty == RunDifficulty.option_easy and self.tier <= CharacterTier.get_tier_class("A"):
            return True
        elif options.run_difficulty == RunDifficulty.option_normal and self.tier <= CharacterTier.get_tier_class("B"):
            return True
        elif options.run_difficulty == RunDifficulty.option_hard and self.tier <= CharacterTier.get_tier_class("C"):
            return True
        elif options.run_difficulty == RunDifficulty.option_impossible and self.tier >= CharacterTier.get_tier_class("D"):
            return True
        
        # Otherwise - bail with a false
        return False

def getCharacterList():
    return [
        Character("FOX", "S"),
        Character("MARTH", "S"),
        Character("JIGGLYPUFF", "S"),
        Character("FALCO", "S"),
        Character("SHEIK", "A"),
        Character("CF", "A"),
        Character("PEACH", "A"),
        Character("IC", "A"),
        Character("PIKACHU", "BPLUS"),
        Character("YOSHI", "BPLUS"),
        Character("DK", "BPLUS"),
        Character("SAMUS", "BPLUS"),
        Character("LUIGI", "BMINUS"),
        Character("DRMARIO", "BMINUS"),
        Character("LINK", "CPLUS"),
        Character("GANONDORF", "CPLUS"),
        Character("MARIO", "CPLUS"),
        Character("YLINK", "CMINUS"),
        Character("GW", "CMINUS"),
        Character("MEWTWO", "D"),
        Character("ROY", "D"),
        Character("PICHU", "D"),
        Character("NESS", "D"),
        Character("ZELDA", "D"),
        Character("KIRBY", "F"),
        Character("BOWSER", "F")
    ]