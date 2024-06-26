from BaseClasses import MultiWorld, Region

from .Locations import SotnLocation, enemy_locations, drop_locations, castle_table, exploration_table
from .Rules import sotn_has_flying, sotn_has_any, sotn_has_wolf, sotn_has_reverse, sotn_has_dracula
from .Rom import limited_locations


def create_regions(multiworld: MultiWorld, player: int, seed_options: dict) -> None:
    open_no4 = seed_options["open_no4"]
    open_are = seed_options["open_are"]
    open_no2 = seed_options["open_no2"]
    esanity = seed_options["esanity"]
    dsanity = seed_options["dsanity"]
    goal = seed_options["goal"]
    rules = seed_options["rules"]

    regions_dict = {
        1: Region("Colosseum", player, multiworld),
        2: Region("Catacombs", player, multiworld),
        4: Region("Abandoned Mine", player, multiworld),
        5: Region("Royal Chapel", player, multiworld),
        7: Region("Long Library", player, multiworld),
        8: Region("Marble Gallery", player, multiworld),
        9: Region("Outer Wall", player, multiworld),
        10: Region("Olrox's Quarters", player, multiworld),
        11: Region("Castle Entrance", player, multiworld),
        13: Region("Underground Caverns", player, multiworld),
        14: Region("Alchemy Laboratory", player, multiworld),
        15: Region("Clock Tower", player, multiworld),
        16: Region("Castle Keep", player, multiworld),
        18: Region("Reverse Colosseum", player, multiworld),
        19: Region("Floating Catacombs", player, multiworld),
        20: Region("Reverse Center Cube", player, multiworld),
        21: Region("Cave", player, multiworld),
        22: Region("Anti-Chapel", player, multiworld),
        23: Region("Forbidden Library", player, multiworld),
        24: Region("Black Marble Gallery", player, multiworld),
        25: Region("Reverse Outer Wall", player, multiworld),
        26: Region("Death Wing's Lair", player, multiworld),
        27: Region("Reverse Entrance", player, multiworld),
        28: Region("Reverse Caverns", player, multiworld),
        29: Region("Necromancy Laboratory", player, multiworld),
        30: Region("Reverse Clock Tower", player, multiworld),
        31: Region("Reverse Castle Keep", player, multiworld),
    }

    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    name_to_region = {value.name: value for key, value in regions_dict.items()}
    if 0 <= goal <= 2 or (goal == 4 and rules == 1):
        region = name_to_region["Castle Keep"]
        region.locations.append(SotnLocation(player, "Keep Boss", None, region))

    if goal == 3 or goal == 5:
        region = name_to_region["Reverse Center Cube"]
        region.locations.append(SotnLocation(player, "RCEN - Kill Dracula", None, region))

    for k, v in castle_table.items():
        if rules > 0:
            if k not in limited_locations:
                continue
        region = name_to_region[v.zone]
        region.locations.append(SotnLocation(player, k, v.location_id, region))
    # Exploration locations
    no3 = name_to_region["Castle Entrance"]
    for k, v in exploration_table.items():
        if rules == 1 and "item" in k:
            continue
        no3.locations.append(SotnLocation(player, k, v.location_id, no3))

    if esanity:
        for k, v in enemy_locations.items():
            if rules == 1:
                continue
            region = name_to_region[v.zone]
            region.locations.append(SotnLocation(player, k, v.location_id, region))
    if dsanity:
        for k, v in drop_locations.items():
            if rules == 1:
                continue
            region = name_to_region[v.zone]
            region.locations.append(SotnLocation(player, k, v.location_id, region))

    for k, v in regions_dict.items():
        multiworld.regions.append(v)

    menu.connect(name_to_region["Castle Entrance"])
    # Colosseum
    if not open_are:
        name_to_region["Colosseum"].connect(name_to_region["Royal Chapel"], "ARE->DAI", lambda state:
                                            sotn_has_any(state, player))
    else:
        # Could access normally or thru back door coming from NZ1 or NZ0
        name_to_region["Colosseum"].connect(name_to_region["Royal Chapel"], "ARE->DAI", lambda state:
                                            state.has("Jewel of open", player) or sotn_has_any(state, player))
    name_to_region["Colosseum"].connect(name_to_region["Olrox's Quarters"])
    # Catacombs
    name_to_region["Catacombs"].connect(name_to_region["Abandoned Mine"])
    # Abandoned Mine
    name_to_region["Abandoned Mine"].connect(name_to_region["Catacombs"])
    if not open_no4:
        name_to_region["Abandoned Mine"].connect(name_to_region["Underground Caverns"], "CHI->NO4", lambda state:
                                                 (state.has("Leap stone", player) or sotn_has_flying(state, player) or
                                                  sotn_has_wolf(state, player)) and
                                                 state.has("Jewel of open", player))
    else:
        name_to_region["Abandoned Mine"].connect(name_to_region["Underground Caverns"], "CHI->NO4", lambda state:
                                                 sotn_has_flying(state, player) or ((state.has("Leap stone", player) or
                                                                                     sotn_has_flying(state, player) or
                                                                                     sotn_has_wolf(state, player)) and
                                                                                    state.has("Jewel of open", player)))
    # Royal Chapel
    name_to_region["Royal Chapel"].connect(name_to_region["Alchemy Laboratory"], "DAI->NZ0", lambda state:
                                           state.has("Jewel of open", player) or
                                           sotn_has_any(state, player))
    if not open_are:
        name_to_region["Royal Chapel"].connect(name_to_region["Colosseum"], "DAI->ARE", lambda state: sotn_has_any(state, player))
    else:
        name_to_region["Royal Chapel"].connect(name_to_region["Colosseum"], "DAI->ARE", lambda state:
                                               sotn_has_any(state, player) or state.has("Jewel of open", player))
    if not open_no2:
        name_to_region["Royal Chapel"].connect(name_to_region["Olrox's Quarters"], "DAI->NO2", lambda state:
                                               sotn_has_flying(state, player))
    else:
        name_to_region["Royal Chapel"].connect(name_to_region["Olrox's Quarters"], "DAI->NO2", lambda state:
                                               sotn_has_any(state, player) or state.has("Jewel of open", player))

    name_to_region["Royal Chapel"].connect(name_to_region["Castle Keep"])
    # Long Library
    name_to_region["Long Library"].connect(name_to_region["Outer Wall"])
    # Marble Gallery
    name_to_region["Marble Gallery"].connect(name_to_region["Outer Wall"])
    name_to_region["Marble Gallery"].connect(name_to_region["Olrox's Quarters"], "NO0->NO2", lambda state:
                                             sotn_has_any(state, player))
    name_to_region["Marble Gallery"].connect(name_to_region["Underground Caverns"], "NO0->NO4", lambda state:
                                             state.has("Jewel of open", player))
    name_to_region["Marble Gallery"].connect(name_to_region["Castle Entrance"])
    name_to_region["Marble Gallery"].connect(name_to_region["Alchemy Laboratory"])
    # Outer Wall
    name_to_region["Outer Wall"].connect(name_to_region["Long Library"])
    name_to_region["Outer Wall"].connect(name_to_region["Marble Gallery"])
    name_to_region["Outer Wall"].connect(name_to_region["Clock Tower"], "NO1->NZ1", lambda state:
                                         sotn_has_any(state, player))
    # Olrox's Quarters
    name_to_region["Olrox's Quarters"].connect(name_to_region["Royal Chapel"])
    if not open_no2:
        name_to_region["Olrox's Quarters"].connect(name_to_region["Colosseum"])
    else:
        name_to_region["Olrox's Quarters"].connect(name_to_region["Colosseum"], "NO2->ARE", lambda state:
                                                   sotn_has_flying(state, player))
    name_to_region["Olrox's Quarters"].connect(name_to_region["Marble Gallery"], "NO2->NO0", lambda state:
                                               sotn_has_any(state, player))
    # Castle Entrance
    if not open_no4:
        name_to_region["Castle Entrance"].connect(name_to_region["Underground Caverns"], "NO3->NO4", lambda state:
                                                  state.has("Jewel of open", player))
    else:
        name_to_region["Castle Entrance"].connect(name_to_region["Underground Caverns"])
    name_to_region["Castle Entrance"].connect(name_to_region["Alchemy Laboratory"])
    name_to_region["Castle Entrance"].connect(name_to_region["Marble Gallery"])
    # Underground Caverns
    name_to_region["Underground Caverns"].connect(name_to_region["Marble Gallery"], "NO4->NO0", lambda state:
                                                  state.has("Jewel of open", player))
    if not open_no4:
        name_to_region["Underground Caverns"].connect(name_to_region["Castle Entrance"], "NO4->NO3", lambda state:
                                                      state.has("Jewel of open", player))
        name_to_region["Underground Caverns"].connect(name_to_region["Abandoned Mine"], "NO4->CHI", lambda state:
                                                      sotn_has_wolf(state, player) or
                                                      state.has("Leap stone", player) or sotn_has_flying(state, player))
    else:
        name_to_region["Underground Caverns"].connect(name_to_region["Castle Entrance"])
        name_to_region["Underground Caverns"].connect(name_to_region["Abandoned Mine"], "NO4->CHI", lambda state:
                                                      (state.has("Jewel of Open", player) and
                                                       (state.has("Leap stone", player) or
                                                        sotn_has_wolf(state, player))) or
                                                      sotn_has_flying(state, player))
    # Alchemy Laboratory
    name_to_region["Alchemy Laboratory"].connect(name_to_region["Marble Gallery"])
    name_to_region["Alchemy Laboratory"].connect(name_to_region["Castle Entrance"])
    name_to_region["Alchemy Laboratory"].connect(name_to_region["Royal Chapel"], "NZ0->DAI", lambda state:
                                                 state.has("Jewel of open", player))
    # Clock Tower
    name_to_region["Clock Tower"].connect(name_to_region["Outer Wall"])
    name_to_region["Clock Tower"].connect(name_to_region["Castle Keep"], "NZ1->TOP", lambda state:
                                          sotn_has_any(state, player))
    # Castle Keep
    name_to_region["Castle Keep"].connect(name_to_region["Clock Tower"], "TOP->NZ1", lambda state:
                                          sotn_has_flying(state, player))
    name_to_region["Castle Keep"].connect(name_to_region["Royal Chapel"])
    name_to_region["Castle Keep"].connect(name_to_region["Reverse Castle Keep"], "TOP->RTOP", lambda state:
                                          sotn_has_reverse(state,player))
    # Reverse Keep
    name_to_region["Reverse Castle Keep"].connect(name_to_region["Castle Keep"], "RTOP->TOP", lambda state:
                                                  sotn_has_reverse(state, player))
    name_to_region["Reverse Castle Keep"].connect(name_to_region["Anti-Chapel"])
    name_to_region["Reverse Castle Keep"].connect(name_to_region["Reverse Clock Tower"])
    # Anti-Chapel
    name_to_region["Anti-Chapel"].connect(name_to_region["Reverse Castle Keep"])
    name_to_region["Anti-Chapel"].connect(name_to_region["Death Wing's Lair"])
    name_to_region["Anti-Chapel"].connect(name_to_region["Reverse Colosseum"])
    name_to_region["Anti-Chapel"].connect(name_to_region["Necromancy Laboratory"])
    # Reverse Clock Tower
    name_to_region["Reverse Clock Tower"].connect(name_to_region["Reverse Castle Keep"])
    name_to_region["Reverse Clock Tower"].connect(name_to_region["Reverse Outer Wall"])
    # Death Wing's Lair
    name_to_region["Death Wing's Lair"].connect(name_to_region["Anti-Chapel"])
    name_to_region["Death Wing's Lair"].connect(name_to_region["Reverse Colosseum"])
    name_to_region["Death Wing's Lair"].connect(name_to_region["Black Marble Gallery"])
    # Reverse Colosseum
    name_to_region["Reverse Colosseum"].connect(name_to_region["Reverse Clock Tower"])
    name_to_region["Reverse Colosseum"].connect(name_to_region["Death Wing's Lair"])
    # Necromancy Laboratory
    name_to_region["Necromancy Laboratory"].connect(name_to_region["Anti-Chapel"])
    name_to_region["Necromancy Laboratory"].connect(name_to_region["Black Marble Gallery"])
    name_to_region["Necromancy Laboratory"].connect(name_to_region["Reverse Entrance"])
    # Reverse Outer Wall
    name_to_region["Reverse Outer Wall"].connect(name_to_region["Reverse Clock Tower"])
    name_to_region["Reverse Outer Wall"].connect(name_to_region["Forbidden Library"])
    name_to_region["Reverse Outer Wall"].connect(name_to_region["Black Marble Gallery"])
    # Black Marble Gallery
    name_to_region["Black Marble Gallery"].connect(name_to_region["Death Wing's Lair"])
    name_to_region["Black Marble Gallery"].connect(name_to_region["Reverse Outer Wall"])
    name_to_region["Black Marble Gallery"].connect(name_to_region["Reverse Caverns"])
    name_to_region["Black Marble Gallery"].connect(name_to_region["Reverse Entrance"])
    name_to_region["Black Marble Gallery"].connect(name_to_region["Necromancy Laboratory"])
    name_to_region["Black Marble Gallery"].connect(name_to_region["Reverse Center Cube"], "RNO0->RCEN", lambda state:
                                                   sotn_has_dracula(state, player))
    # Reverse Center Cube
    name_to_region["Reverse Center Cube"]. connect(name_to_region["Black Marble Gallery"])
    # Reverse Castle Entrance
    name_to_region["Reverse Entrance"].connect(name_to_region["Death Wing's Lair"])
    name_to_region["Reverse Entrance"].connect(name_to_region["Black Marble Gallery"])
    name_to_region["Reverse Entrance"].connect(name_to_region["Reverse Caverns"])
    # Forbidden Library
    name_to_region["Forbidden Library"].connect(name_to_region["Reverse Outer Wall"])
    # Reverse Caverns
    name_to_region["Reverse Caverns"].connect(name_to_region["Black Marble Gallery"])
    name_to_region["Reverse Caverns"].connect(name_to_region["Reverse Entrance"])
    name_to_region["Reverse Caverns"].connect(name_to_region["Cave"])
    # Cave
    name_to_region["Cave"].connect(name_to_region["Reverse Caverns"])
    name_to_region["Cave"].connect(name_to_region["Floating Catacombs"])
    # Floating Catacombs
    name_to_region["Floating Catacombs"].connect(name_to_region["Cave"])
