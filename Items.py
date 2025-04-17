from typing import Dict, NamedTuple, Optional
from BaseClasses import Item, ItemClassification
from .names.Characters import CharacterName

class MeleeSlippiItem(Item):
    game: str = "Melee Slippi"

class ItemData(NamedTuple):
    id: Optional[int]
    type: ItemClassification = ItemClassification.filler

melee_slippi_base_id: int = 153761962

# 4 colors - https://www.ssbwiki.com/Alternate_costume_(SSBM)
filler_item = {"Trophy": ItemData(melee_slippi_base_id + 0,ItemClassification.filler)}

characters: Dict[str, ItemData] = {
    CharacterName.MARIO: ItemData(melee_slippi_base_id + 1, ItemClassification.progression),
    CharacterName.DK: ItemData(melee_slippi_base_id + 2, ItemClassification.progression),
    CharacterName.LINK: ItemData(melee_slippi_base_id + 3, ItemClassification.progression),
    CharacterName.SAMUS: ItemData(melee_slippi_base_id + 4, ItemClassification.progression),
    CharacterName.YOSHI: ItemData(melee_slippi_base_id + 5, ItemClassification.progression),
    CharacterName.KIRBY: ItemData(melee_slippi_base_id + 6, ItemClassification.progression),
    CharacterName.FOX: ItemData(melee_slippi_base_id + 7, ItemClassification.progression),
    CharacterName.PIKACHU: ItemData(melee_slippi_base_id + 8, ItemClassification.progression),
    CharacterName.NESS: ItemData(melee_slippi_base_id + 9, ItemClassification.progression),
    CharacterName.CF: ItemData(melee_slippi_base_id + 10, ItemClassification.progression),
    CharacterName.BOWSER: ItemData(melee_slippi_base_id + 11, ItemClassification.progression),
    CharacterName.PEACH: ItemData(melee_slippi_base_id + 12, ItemClassification.progression),
    CharacterName.IC: ItemData(melee_slippi_base_id + 13, ItemClassification.progression),
    CharacterName.ZELDA: ItemData(melee_slippi_base_id + 14, ItemClassification.progression),
    CharacterName.SHEIK: ItemData(melee_slippi_base_id + 15, ItemClassification.progression),
    CharacterName.LUIGI: ItemData(melee_slippi_base_id + 16, ItemClassification.progression),
    CharacterName.JIGGLYPUFF: ItemData(melee_slippi_base_id + 17, ItemClassification.progression),
    CharacterName.MEWTWO: ItemData(melee_slippi_base_id + 18, ItemClassification.progression),
    CharacterName.MARTH: ItemData(melee_slippi_base_id + 19, ItemClassification.progression),
    CharacterName.GW: ItemData(melee_slippi_base_id + 20, ItemClassification.progression),
    CharacterName.DRMARIO: ItemData(melee_slippi_base_id + 21, ItemClassification.progression),
    CharacterName.GANONDORF: ItemData(melee_slippi_base_id + 22, ItemClassification.progression),
    CharacterName.FALCO: ItemData(melee_slippi_base_id + 23, ItemClassification.progression),
    CharacterName.YLINK: ItemData(melee_slippi_base_id + 24, ItemClassification.progression),
    CharacterName.PICHU: ItemData(melee_slippi_base_id + 25, ItemClassification.progression),
    CharacterName.ROY: ItemData(melee_slippi_base_id + 26, ItemClassification.progression),
}

item_data_table = {**filler_item, **characters}
item_data = {name:data.id for name,data in item_data_table.items() if data.id is not None}