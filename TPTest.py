import dolphin_memory_engine
import asyncio
from CommonClient import ClientCommandProcessor, CommonContext, logger, gui_enabled
from collections import namedtuple

from worlds.tp.Locations import Regions, locations
from worlds.tp.Items import bottles, items


item_id_to_name = {value.game_value: key for key, value in items.items()}
item_wheel_start = 0x80406274
item_inventory_start = 0x8040625c
region_node = 0x80406b18


class TPCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)


class TPContext(CommonContext):
    def __init__(self):
        super().__init__("", "")
        self.dolphin_sync_task = None

    def run_gui(self):
        from kvui import GameManager

        class TPManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago TP Client"

        self.ui = TPManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def dolphin_sync_task(ctx: TPContext):
    current_inventory = list(dolphin_memory_engine.read_bytes(item_wheel_start, 24))
    last_checked_locations = set()
    checked_locations = set()

    logger.info("Current inventory:")
    for item in current_inventory:
        if item == 0xff:
            continue
        current_item = dolphin_memory_engine.read_byte(item_inventory_start + item)
        try:
            item_name = item_id_to_name[current_item]
        except KeyError:
            item_name = bottles[current_item]
        logger.info(item_name)

    while not ctx.exit_event.is_set():
        current_zone = dolphin_memory_engine.read_bytes(0x8040afc0, 8)
        zone_name = ""
        for k, v in Regions.items():
            if zone_name != "":
                break
            for a in v:
                if current_zone == a:
                    zone_name = k
                    break

        last_offset = 0xffff
        for k, v in locations.items():
            if zone_name == v.zone:
                if v.offset != last_offset:
                    last_offset = v.offset
                    flag_read = dolphin_memory_engine.read_byte(region_node + last_offset)

                if flag_read & v.mask:
                    checked_locations.add(k)

        if checked_locations != last_checked_locations:
            difference = checked_locations.difference(last_checked_locations)
            for check in difference:
                logger.info(f"New check: {check}")
                last_checked_locations.add(check)
        await asyncio.sleep(0.2)


def grant_item(item_name: str) -> None:
    try:
        item_to_grant = items[item_name]
    except KeyError:
        print(f"Error! {item_name} not found")
        return

    mem_read = dolphin_memory_engine.read_byte(item_to_grant.inventory_position + item_inventory_start)
    if mem_read != 0xFF:
        print("Error! Already have item")
        return

    item_wheel_list = list(dolphin_memory_engine.read_bytes(item_wheel_start, 24))

    for i, item in enumerate(item_wheel_list):
        if item == 0xff:
            # Reach an empty space
            item_wheel_list[i] = item_to_grant.inventory_position
            dolphin_memory_engine.write_byte(item_inventory_start + item_to_grant.inventory_position,
                                             item_to_grant.game_value)
            dolphin_memory_engine.write_bytes(item_wheel_start, bytes(item_wheel_list))
            break
        else:
            cur_item_id = dolphin_memory_engine.read_byte(item_inventory_start + item)
            if cur_item_id in bottles.keys():
                cur_item = items["Bottle #1"]
            else:
                cur_item = items[item_id_to_name[cur_item_id]]

            if cur_item.default_wheel_position > item_to_grant.default_wheel_position:
                # WE MIGHT LOSE LAST ITEM. NEED MORE RESEARCH
                item_wheel_list = item_wheel_list[0:i] + [item_to_grant.inventory_position] + item_wheel_list[i:-1]
                dolphin_memory_engine.write_byte(item_inventory_start + item_to_grant.inventory_position,
                                                 item_to_grant.game_value)
                dolphin_memory_engine.write_bytes(item_wheel_start, bytes(item_wheel_list))
                break


def main():
    async def _main():
        ctx = TPContext()
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await asyncio.sleep(1)

        dolphin_memory_engine.hook()
        if dolphin_memory_engine.is_hooked():
            logger.info("Hooked to Dolphin")

        ctx.dolphin_sync_task = asyncio.create_task(dolphin_sync_task(ctx), name="DolphinSync")
        await ctx.dolphin_sync_task
        await asyncio.sleep(.25)

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        await asyncio.sleep(.5)

    import colorama

    colorama.init()
    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    main()
