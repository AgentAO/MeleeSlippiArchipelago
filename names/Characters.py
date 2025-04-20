class CharacterTier:
    S = 0
    A = 1
    BPLUS = 2
    BMINUS = 3
    CPLUS = 4
    CMINUS = 5
    D = 6
    F = 7

    # Helper function for grabbing grouped tiers, but we can still keep them separated out if needed
    @staticmethod
    def get_tier_class(tierClass: str):
        if tierClass == "S":
            return 0
        if tierClass == "A":
            return 1
        if tierClass == "B":
            return 3
        if tierClass == "C":
            return 5
        if tierClass == "D":
            return 6
        if tierClass == "F":
            return 7

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

def getCharacterList():
    return [
        Character("FOX", "S"),
        Character("MARTH", "S"),
        Character("JIGGLYPUFF", "S"),
        Character("FALCO", "S"),
        Character("SHEIK", "A"),
        Character("CF", "A"),
        Character("PEACH", "A"),
        Character("IC", "BPLUS"),
        Character("PIKACHU", "BPLUS"),
        Character("YOSHI", "BPLUS"),
        Character("SAMUS", "BPLUS"),
        Character("LUIGI", "BMINUS"),
        Character("DRMARIO", "BMINUS"),
        Character("GANONDORF", "CPLUS"),
        Character("MARIO", "CPLUS"),
        Character("DK", "CMINUS"),
        Character("YLINK", "CMINUS"),
        Character("LINK", "CMINUS"),
        Character("GW", "CMINUS"),
        Character("MEWTWO", "D"),
        Character("ROY", "D"),
        Character("PICHU", "D"),
        Character("NESS", "D"),
        Character("ZELDA", "D"),
        Character("KIRBY", "F"),
        Character("BOWSER", "F")
    ]
    # return [{"id": name, "name": getattr(CharacterName,name)} for name in dir(CharacterName) if not name.startswith('__') ]