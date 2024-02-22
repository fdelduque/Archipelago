import Utils
from sys import platform
from worlds.Files import APDeltaPatch
from settings import get_settings
from worlds.AutoWorld import World
from .Items import item_table, relic_table, SotnItem, ItemData, base_item_id, event_table, IType, vanilla_list
from .Locations import location_table, SotnLocation

import hashlib
import os
import subprocess
import bsdiff4

USHASH = 'acbb3a2e4a8f865f363dc06df147afa2'


class SOTNDeltaPatch(APDeltaPatch):
    hash = USHASH
    game = "Symphony of the Night"
    patch_file_ending = ".apsotn"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


def get_base_rom_bytes() -> bytes:
    with open(get_settings().sotn_settings.rom_file, "rb") as infile:
        base_rom_bytes = bytes(infile.read())

    basemd5 = hashlib.md5()
    basemd5.update(base_rom_bytes)
    if USHASH != basemd5.hexdigest():
        raise Exception('Supplied Base Rom does not match known MD5 for SLU067 release. '
                        'Get the correct game and version, then dump it')

    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options = get_settings()
    if not file_name:
        file_name = options["sotn_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name


def write_char(buffer, address: int, value: int):
    buffer[address] = value


def write_short(buffer, address: int, value: int):
    x1, x2 = (value & 0xFFFF).to_bytes(2, 'little')
    buffer[address] = x1
    buffer[address + 1] = x2


def write_word(buffer, address: int, value):
    x1, x2, x3, x4 = (value & 0xFFFFFFFF).to_bytes(4, 'little')
    buffer[address] = x1
    buffer[address + 1] = x2
    buffer[address + 2] = x3
    buffer[address + 3] = x4
    return address + 4


def replace_shop_text(buffer, new_text):
    start_address = 0x047d5650

    for c in new_text:
        if c == " ":
            write_char(buffer, start_address, 0x00)
        else:
            write_char(buffer, start_address, ord(c) - 0x20)
        start_address += 1

    write_char(buffer, start_address, 0xff)
    write_char(buffer, start_address + 1, 0x00)


def patch_rom(world: World) -> str:
    player = world.player
    patched_rom = bytearray(get_base_rom_bytes())
    no4 = world.options.opened_no4
    are = world.options.opened_are
    no2 = world.options.opened_no2
    bosses = world.options.bosses_need

    relics_vlad = ["Heart of Vlad", "Tooth of Vlad", "Rib of Vlad", "Ring of Vlad", "Eye of Vlad"]

    for loc in world.multiworld.get_locations(world.player):
        if loc.item and loc.item.player == world.player:
            if loc.item.name == "Victory" or loc.item.name == "Boss token":
                continue
            item_data = item_table[loc.item.name]
            loc_data = location_table[loc.name]
            if loc_data.rom_address:
                for address in loc_data.rom_address:
                    if loc_data.no_offset:
                        if item_data.type == IType.RELIC:
                            write_short(patched_rom, address, 0x0000)
                        else:
                            write_short(patched_rom, address, item_data.get_item_id_no_offset())
                    else:
                        if loc_data.can_be_relic:
                            if item_data.type == IType.RELIC:
                                write_short(patched_rom, address, item_data.get_item_id())
                                if loc.name == "Jewel of Open":
                                    replace_shop_text(patched_rom, loc.item.name)
                                    # Fix shop menu check
                                    write_char(patched_rom, 0x047dbde0, item_data.get_item_id() + 0x64)
                            else:
                                # Skill of wolf, bat card can't be item. Replace with ghost card instead
                                if loc.name == "Skill of Wolf" or loc.name == "Bat Card":
                                    write_short(patched_rom, address, 0x0013)
                                elif loc.name == "Jewel of Open":
                                    replace_shop_text(patched_rom, "Ghost Card")
                                    write_short(patched_rom, address, 0x0013)
                                    write_char(patched_rom, 0x047dbde0, 0x77)
                                elif loc.name in relics_vlad:
                                    write_short(patched_rom, address, 0x0013)
                                else:
                                    write_short(patched_rom, address - 4, 0x000c)
                                    write_word(patched_rom, address - 2, loc_data.get_delete())
                        else:
                            if item_data.type == IType.RELIC:
                                write_short(patched_rom, address, 0x0007)
                            else:
                                write_short(patched_rom, address, item_data.get_item_id())
        elif loc.item and loc.item.player != world.player:
            loc_data = location_table[loc.name]
            if loc_data.rom_address:
                for address in loc_data.rom_address:
                    if loc_data.no_offset:
                        write_short(patched_rom, address, 0x0000)
                    else:
                        if loc_data.can_be_relic:
                            if loc.name == "Skill of Wolf" or loc.name == "Bat Card":
                                write_short(patched_rom, address, 0x0013)
                            if loc.name == "Jewel of Open":
                                write_short(patched_rom, address, 0x0013)
                                replace_shop_text(patched_rom, "Ghost Card")
                            elif loc.name in relics_vlad:
                                write_short(patched_rom, address, 0x0013)
                            else:
                                write_short(patched_rom, address - 4, 0x000c)
                                write_word(patched_rom, address - 2, loc_data.get_delete())
                        else:
                            write_short(patched_rom, address, 0x0004)

    offset = 0x492df64
    offset = write_word(patched_rom, offset, 0xa0202ee8)
    offset = write_word(patched_rom, offset, 0x080735cc)
    offset = write_word(patched_rom, offset, 0x00000000)
    write_word(patched_rom, 0x4952454, 0x0806b647)
    write_word(patched_rom, 0x4952474, 0x0806b647)

    # Patch Alchemy Laboratory cutscene
    write_short(patched_rom, 0x054f0f44 + 2, 0x1000)

    # Patch Clock Room cutscene
    write_char(patched_rom, 0x0aeaa0, 0x00)
    write_char(patched_rom, 0x119af4, 0x00)

    # patchPowerOfSireFlashing Patches researched by MottZilla.
    write_word(patched_rom, 0x00136580, 0x03e00008)

    # outfile_name = world.multiworld.get_out_file_name_base(world.player)
    # outfile_name += ".bin"

    """
    The flag that get set on NO4 switch: 0x03be1c and the instruction is jz, r2, 80181230 on 0x5430404 we patched
    to jne r0, r0 so it never branch.

    The flag that get set on ARE switch: 0x03be9d and the instruction is jz, r2, 801b6f84 on 0x440110c we patched
    to jne r0, r0 so it never branch.

    The flag that get set on NO2 switch: 0x03be4c and the instruction is jz, r2, 801c1028 on 0x46c0968 we patched
    to jne r0, r0 so it never branch.
    """
    #  NO3 and NP3 doesn't share instruction.
    if no4:
        # Open NO4 too soon, make death skippable. Keep close till visit Alchemy Laboratory
        # write_word(patched_rom, 0x4ba8798, 0x14000005)
        write_word(patched_rom, 0x5430404, 0x14000005)

    if are:
        write_word(patched_rom, 0x440110c, 0x14000066)

    if no2:
        write_word(patched_rom, 0x46c0968, 0x1400000b)
    # Changing ROM name prevent "replay game", had to watch all cinematics and dialogs
    # Write bosses need it on index 12 of RNO0 4f85afc
    # Todo: Try index -1 4f85ae3
    write_char(patched_rom, 0x4f85ae3, bosses)
    """
    The instruction that check relics of Vlad is jnz r2, 801c1790 we gonna change to je r0, r0 so it's always 
    branch. ROM is @ 0x4fcf7b4 and RAM is @ 0x801c132c
    @ 4f85ae3 on ram its 0x180f8b
    """
    write_word(patched_rom, 0x4fcf7b4, 0x10000118)

    seed_num = world.multiworld.seed
    write_seed(patched_rom, seed_num)

    filename = f'SOTN_{seed_num}_P{player}.bin'
    write_to_file(patched_rom, filename)

    abs_path = os.path.abspath(filename)

    return abs_path


def write_seed(buffer, seed):
    write_short(buffer, 0x043930c4, 0x78b4)
    write_short(buffer, 0x043930d4, 0x78d4)
    write_short(buffer, 0x0439312c, 0x78b4)
    write_short(buffer, 0x0439313c, 0x78d4)
    write_short(buffer, 0x04393484, 0x78b4)
    write_short(buffer, 0x04393494, 0x78d4)
    # No idea why, but SOTN.io write those values. I guess

    start_address = 0x04389c6c

    for n in str(seed):
        write_char(buffer, start_address, 0x82)
        start_address += 1
        write_char(buffer, start_address, ord(n) + 0x1f)
        start_address += 1
    write_char(buffer, start_address, 0x00)
    write_char(buffer, start_address + 1, 0x00)
    write_char(buffer, start_address + 2, 0x00)


def write_to_file(buffer, filename=""):
    print(filename)
    if filename == "":
        output_file = get_settings().sotn_settings.rom_file
    else:
        output_file = filename

        cue_file = f'FILE "{filename}" BINARY\n  TRACK 01 MODE2/2352\n\tINDEX 01 00:00:00\n'
        cue_file += f'FILE "Castlevania - Symphony of the Night (USA) (Track 2).bin" BINARY\n  TRACK 02 AUDIO\n'
        cue_file += f'\tINDEX 00 00:00:00\n\tINDEX 01 00:02:00'

    with open(output_file, 'wb') as outfile:
        outfile.write(buffer)

    if platform == "win32":
        print("ERROR RECALC started. Please wait")
        subprocess.call(["error_recalc", f"{filename}"])
    else:
        print("ERROR RECALC FAILED!!!")

    """print("bsdiff started")
    bsdiff4.file_diff("C:\\Python_projects\\APSOTN\\Castlevania - Symphony of the Night (USA) (Track 1).bin",
                      f"{filename}", "C:\\Python_projects\\APSOTN\\teste.diff")"""

    with open(f"{filename[0:-4]}.cue", 'wb') as outfile:
        outfile.write(bytes(cue_file, 'utf-8'))
