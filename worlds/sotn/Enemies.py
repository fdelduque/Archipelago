
enemy_dict = {
    "Dracula":
        {
            "enemy_id": 1,
            "drop_addresses": [0x0b766a, 0xb766a],
            "attack": 4,
            "attack_address": 0xb7656,
            "hp": 600,
            "hp_address": 0xb7654
        },
    "Blood skeleton":
        {
            "enemy_id": 2,
            "xp": 0,
            "xp_address": 0xb6490,
            "drop_addresses": [0xb6492, 0xb6494],
            "attack": 8,
            "attack_address": 0xb647e,
            "hp": 9,
            "hp_address": 0xb647c
        },
    "Bat":
        {
            "enemy_id": 3,
            "xp": 10,
            "xp_address": 0xb63a0,
            "vanilla_drop": ["Monster vial 2", "Potion"],
            "drop_rate": [6, 24],
            "drop_addresses": [0xb63a2, 0xb63a4],
            "attack": 16,
            "attack_address": 0xb638e,
            "hp": 1,
            "hp_address": 0xb638c
        },
    "Stone skull":
        {
            "enemy_id": 4,
            "xp": 0,
            "xp_address": 0xb9cc0,
            "drop_addresses": [0xb9cc2, 0xb9cc4],
            "attack": 60,
            "attack_address": 0xb9cae,
            "hp": 32767,
            "hp_address": 0xb9cac
        },
    "Zombie":
        {
            "enemy_id": 5,
            "xp": 5,
            "xp_address": 0xb6c00,
            "vanilla_drop": ["Cloth tunic", "$100"],
            "drop_rate": [24, 16],
            "drop_addresses": [0xb6c02, 0xb6c04],
            "attack": 14,
            "attack_address": 0xb6bee,
            "hp": 1,
            "hp_address": 0xb6bec
        },
    "Merman":
        {
            "enemy_id": 6,
            "xp": 12,
            "xp_address": 0xb5ca8,
            "vanilla_drop": ["Monster vial 1", "Zircon"],
            "drop_rate": [8, 12],
            "drop_addresses": [0xb5caa, 0xb5cac],
            "attack": 13,
            "attack_address": 0xb5c96,
            "hp": 10,
            "hp_address": 0xb5c94
        },
    "Skeleton":
        {
            "enemy_id": 7,
            "xp": 10,
            "xp_address": 0xb6558,
            "vanilla_drop": ["Monster vial 3", "Shield potion"],
            "drop_rate": [16, 24],
            "drop_addresses": [0xb655a, 0x0b655c],
            "attack": 2,
            "attack_address": 0xb6546,
            "hp": 9,
            "hp_address": 0xb6544
        },
    "Warg":
        {
            "enemy_id": 8,
            "xp": 10,
            "xp_address": 0xb7758,
            "drop_addresses": [0xb775a, 0xb775c],
            "attack": 20,
            "attack_address": 0xb7746,
            "hp": 32,
            "hp_address": 0xb7744
        },
    "Bone scimitar":
        {
            "enemy_id": 9,
            "xp": 15,
            "xp_address": 0xb6b38,
            "vanilla_drop": ["Red rust", "Short sword"],
            "drop_rate": [16, 32],
            "drop_addresses": [0xb6b3a, 0xb6b3c],
            "attack": 5,
            "attack_address": 0xb6b26,
            "hp": 18,
            "hp_address": 0xb6b24
        },
    "Merman(red)":
        {
            "enemy_id": 10,
            "xp": 12,
            "xp_address": 0xb5cf8,
            "vanilla_drop": ["Monster vial 1", "Zircon"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb5cfa, 0xb5cfc],
            "attack": 14,
            "attack_address": 0xb5ce6,
            "hp": 10,
            "hp_address": 0xb5ce4
        },
    "Spittle bone":
        {
            "enemy_id": 11,
            "xp": 20,
            "xp_address": 0xb6648,
            "drop_addresses": [0xb664a, 0xb664c],
            "attack": 7,
            "attack_address": 0xb6636,
            "hp": 18,
            "hp_address": 0xb6634
        },
    "Axe knight":
        {
            "enemy_id": 12,
            "xp": 10,
            "xp_address": 0xb83a0,
            "vanilla_drop": ["Bronze cuirass", "Axe"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb83a2, 0xb83a4],
            "attack": 6,
            "attack_address": 0xb838e,
            "hp": 32,
            "hp_address": 0xb838c,
        },
    "Bloody zombie":
        {
            "enemy_id": 13,
            "xp": 15,
            "xp_address": 0xb5a78,
            "vanilla_drop": ["Basilard", "Cloth tunic"],
            "drop_rate": [16, 32],
            "drop_addresses": [0xb5a7a, 0xb5a7c],
            "attack": 10,
            "attack_address": 0xb5a66,
            "hp": 24,
            "hp_address": 0xb5a64,
        },
    "Slinger":
        {
            "enemy_id": 14,
            "xp": 10,
            "xp_address": 0xb77d0,
            "vanilla_drop": ["Knight shield", "Leather shield"],
            "drop_rate": [4, 24],
            "drop_addresses": [0xb77d2, 0xb77d4],
            "attack": 5,
            "attack_address": 0xb77be,
            "hp": 12,
            "hp_address": 0xb77bc,
        },
    "Ouija table":
        {
            "enemy_id": 15,
            "xp": 20,
            "xp_address": 0xb7a28,
            "vanilla_drop": ["Morning set", "Barley tea"],
            "drop_rate": [8, 8],
            "drop_addresses": [0xb7a2a, 0xb7a2c],
            "attack": 4,
            "attack_address": 0xb7a16,
            "hp": 20,
            "hp_address": 0xb7a14,
        },
    "Skelerang":
        {
            "enemy_id": 16,
            "xp": 15,
            "xp_address": 0xb5a28,
            "vanilla_drop": ["Fire boomerang", "Boomerang"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb5a2a, 0xb5a2c],
            "attack": 12,
            "attack_address": 0xb5a16,
            "hp": 18,
            "hp_address": 0xb5a14,
        },
    "Thornweed":
        {
            "enemy_id": 17,
            "xp": 20,
            "xp_address": 0xb7488,
            "vanilla_drop": ["Strawberry", "Grapes"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb748a, 0xb748c],
            "attack": 10,
            "attack_address": 0xb7476,
            "hp": 12,
            "hp_address": 0xb7474,
        },
    "Gaibon":
        {
            "enemy_id": 18,
            "xp": 200,
            "xp_address": 0xb8610,
            "drop_addresses": [0xb8612, 0xb8614],
            "attack": 7,
            "attack_address": 0xb85fe,
            "hp": 200,
            "hp_address": 0xb85fc,
        },
    "Ghost":
        {
            "enemy_id": 19,
            "xp": 10,
            "xp_address": 0xb7460,
            "vanilla_drop": ["Antivenom", "$400"],
            "drop_addresses": [0xb7462, 0xb7464],
            "drop_rate": [8, 16],
            "attack": 5,
            "attack_address": 0xb744e,
            "hp": 11,
            "hp_address": 0xb744c,
        },
    "Marionette":
        {
            "enemy_id": 20,
            "xp": 30,
            "xp_address": 0xb6148,
            "vanilla_drop": ["Circlet", "Smart potion"],
            "drop_rate": [16, 24],
            "drop_addresses": [0xb614a, 0xb614c],
            "attack": 8,
            "attack_address": 0xb6136,
            "hp": 20,
            "hp_address": 0xb6134,
        },
    "Slogra":
        {
            "enemy_id": 21,
            "xp": 200,
            "xp_address": 0xb8328,
            "drop_addresses": [0xb832a, 0xb832c],
            "attack": 6,
            "attack_address": 0xb8316,
            "hp": 200,
            "hp_address": 0xb8314,
        },
    "Diplocephalus":
        {
            "enemy_id": 22,
            "xp": 50,
            "xp_address": 0xb5af0,
            "vanilla_drop": ["Tart", "Pentagram"],
            "drop_rate": [6, 8],
            "drop_addresses": [0xb5af2, 0xb5af4],
            "attack": 6,
            "attack_address": 0xb5ade,
            "hp": 80,
            "hp_address": 0xb5adc,
        },
    "Flea man":
        {
            "enemy_id": 23,
            "xp": 17,
            "xp_address": 0xb5eb0,
            "vanilla_drop": ["Cheese", "Takemitsu"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb5eb2, 0xb5eb4],
            "attack": 9,
            "attack_address": 0xb5e9e,
            "hp": 11,
            "hp_address": 0xb5e9c,
        },
    "Medusa head":
        {
            "enemy_id": 24,
            "xp": 20,
            "xp_address": 0xb8ee8,
            "vanilla_drop": ["Medusa shield", "Resist stone"],
            "drop_rate": [1, 10],
            "drop_addresses": [0xb8eea, 0xb8eec],
            "attack": 12,
            "attack_address": 0xb8ed6,
            "hp": 12,
            "hp_address": 0xb8ed4,
        },
    "Blade soldier":
        {
            "enemy_id": 25,
            "xp": 20,
            "xp_address": 0xb6e30,
            "vanilla_drop": ["Namakura", "$400"],
            "drop_rate": [16, 32],
            "drop_addresses": [0xb6e32, 0xb6e34],
            "attack": 15,
            "attack_address": 0xb6e1e,
            "hp": 16,
            "hp_address": 0xb6e1c,
        },
    "Bone musket":
        {
            "enemy_id": 26,
            "xp": 20,
            "xp_address": 0xb6ac0,
            "vanilla_drop": ["Talisman", "Magic missile"],
            "drop_rate": [1, 8],
            "drop_addresses": [0xb6ac2, 0xb6ac4],
            "attack": 12,
            "attack_address": 0xb6aae,
            "hp": 24,
            "hp_address": 0xb6aac,
        },
    "Medusa head(yellow)":
        {
            "enemy_id": 27,
            "xp": 30,
            "xp_address": 0xb8f10,
            "vanilla_drop": ["Medusa shield", "Resist stone"],
            "drop_rate": [1, 10],
            "drop_addresses": [0xb8f12, 0xb8f14],
            "attack": 7,
            "attack_address": 0xb8efe,
            "hp": 12,
            "hp_address": 0xb8efc,
        },
    "Plate lord":
        {
            "enemy_id": 28,
            "xp": 90,
            "xp_address": 0xb69f8,
            "vanilla_drop": ["Neutron bomb", "Iron ball"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb69fa, 0xb69fc],
            "attack": 18,
            "attack_address": 0xb69e6,
            "hp": 90,
            "hp_address": 0xb69e4,
        },
    "Stone rose":
        {
            "enemy_id": 29,
            "xp": 60,
            "xp_address": 0xb66e8,
            "vanilla_drop": ["Meal ticket", "Leather shield"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb66ea, 0xb66ec],
            "attack": 12,
            "attack_address": 0xb66d6,
            "hp": 60,
            "hp_address": 0xb66d4,
        },
    "Axe knight(armored)":
        {
            "enemy_id": 30,
            "xp": 50,
            "xp_address": 0xb5960,
            "vanilla_drop": ["AxeLord shield", "Axe"],
            "drop_rate": [2, 16],
            "drop_addresses": [0xb5962, 0xb5964],
            "attack": 10,
            "attack_address": 0xb594e,
            "hp": 42,
            "hp_address": 0xb594c,
        },
    "Ctulhu":
        {
            "enemy_id": 31,
            "xp": 100,
            "xp_address": 0xb8198,
            "vanilla_drop": ["Bat pentagram", "Pentagram"],
            "drop_rate": [3, 5],
            "drop_addresses": [0xb819a, 0xb819c],
            "attack": 24,
            "attack_address": 0xb8186,
            "hp": 200,
            "hp_address": 0xb8184,
        },
    "Bone archer":
        {
            "enemy_id": 32,
            "xp": 50,
            "xp_address": 0xb6bb0,
            "vanilla_drop": ["Magic missile", "$400"],
            "drop_rate": [16, 32],
            "drop_addresses": [0xb6bb2, 0xb6bb4],
            "attack": 12,
            "attack_address": 0xb6b9e,
            "hp": 10,
            "hp_address": 0xb6b9c,
        },
    "Bone pillar":
        {
            "enemy_id": 33,
            "xp": 30,
            "xp_address": 0xb7898,
            "vanilla_drop": ["Ballroom mask", "Antivenom"],
            "drop_rate": [12, 13],
            "drop_addresses": [0xb789a, 0xb789c],
            "attack": 12,
            "attack_address": 0xb7886,
            "hp": 64,
            "hp_address": 0xb7884,
        },
    "Doppleganger10":
        {
            "enemy_id": 34,
            "xp": 500,
            "xp_address": 0xb85e8,
            "drop_addresses": [0xb85ea, 0xb85ec],
            "attack": 7,
            "attack_address": 0xb85d6,
            "hp": 120,
            "hp_address": 0xb85d4,
        },
    "Owl":
        {
            "enemy_id": 35,
            "xp": 30,
            "xp_address": 0xb5be0,
            "drop_addresses": [0xb5be2, 0xb5be4],
            "attack": 20,
            "attack_address": 0xb5bce,
            "hp": 26,
            "hp_address": 0xb5bcc,
        },
    "Phantom skull":
        {
            "enemy_id": 36,
            "xp": 30,
            "xp_address": 0xb6418,
            "vanilla_drop": ["Resist dark", "Felt hat"],
            "drop_rate": [16, 16],
            "drop_addresses": [0xb641a, 0xb641c],
            "attack": 14,
            "attack_address": 0xb6406,
            "hp": 15,
            "hp_address": 0xb6404,
        },
    "Scylla wyrm":
        {
            "enemy_id": 37,
            "xp": 100,
            "xp_address": 0xb8c50,
            "drop_addresses": [0xb8c52, 0xb8c54],
            "attack": 14,
            "attack_address": 0xb8c3e,
            "hp": 130,
            "hp_address": 0xb8c3c,
        },
    "Skeleton ape":
        {
            "enemy_id": 38,
            "xp": 30,
            "xp_address": 0xb6698,
            "vanilla_drop": ["TNT", "Banana"],
            "drop_rate": [8, 24],
            "drop_addresses": [0xb669a, 0xb669c],
            "attack": 10,
            "attack_address": 0xb6686,
            "hp": 10,
            "hp_address": 0xb6684,
        },
    "Spear guard":
        {
            "enemy_id": 39,
            "xp": 70,
            "xp_address": 0xb6828,
            "vanilla_drop": ["Iron cuirass", "Javelin"],
            "drop_rate": [12, 16],
            "drop_addresses": [0xb682a, 0xb682c],
            "attack": 12,
            "attack_address": 0xb6816,
            "hp": 20,
            "hp_address": 0xb6814,
        },
    "Spellbook":
        {
            "enemy_id": 40,
            "xp": 30,
            "xp_address": 0xb83c8,
            "vanilla_drop": ["Pentagram", "$1000"],
            "drop_rate": [2, 8],
            "drop_addresses": [0xb83ca, 0xb83cc],
            "attack": 7,
            "attack_address": 0xb83b6,
            "hp": 26,
            "hp_address": 0xb83b4,
        },
    "Winged guard":
        {
            "enemy_id": 41,
            "xp": 30,
            "xp_address": 0xb6ed0,
            "vanilla_drop": ["Javelin", "Iron shield"],
            "drop_rate": [4, 10],
            "drop_addresses": [0xb6ed2, 0xb6ed4],
            "attack": 12,
            "attack_address": 0xb6ebe,
            "hp": 15,
            "hp_address": 0xb6ebc,
        },
    "Ectoplasm":
        {
            "enemy_id": 42,
            "xp": 70,
            "xp_address": 0xb6760,
            "vanilla_drop": ["Manna prism", "Uncurse"],
            "drop_rate": [2, 32],
            "drop_addresses": [0xb6762, 0xb6764],
            "attack": 6,
            "attack_address": 0xb674e,
            "hp": 18,
            "hp_address": 0xb674c,
        },
    "Sword lord":
        {
            "enemy_id": 43,
            "xp": 80,
            "xp_address": 0xb59d8,
            "vanilla_drop": ["Bekatowa", "Cutlass"],
            "drop_addresses": [0xb59da, 0xb59dc],
            "drop_rate": [8, 16],
            "attack": 12,
            "attack_address": 0xb59c6,
            "hp": 61,
            "hp_address": 0xb59c4,
        },
    "Toad":
        {
            "enemy_id": 44,
            "xp": 20,
            "xp_address": 0xb6b60,
            "vanilla_drop": ["Pizza", "Blue knuckles"],
            "drop_rate": [8, 8],
            "drop_addresses": [0xb6b62, 0xb6b64],
            "attack": 14,
            "attack_address": 0xb6b4e,
            "hp": 10,
            "hp_address": 0xb6b4c,
        },
    "Armor lord":
        {
            "enemy_id": 45,
            "xp": 100,
            "xp_address": 0xb5dc0,
            "vanilla_drop": ["Saber", "Rapier"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb5dc2, 0xb5dc4],
            "attack": 18,
            "attack_address": 0xb5dae,
            "hp": 84,
            "hp_address": 0xb5dac,
        },
    "Corner guard":
        {
            "enemy_id": 46,
            "xp": 30,
            "xp_address": 0xb7820,
            "vanilla_drop": ["Damascus sword", "Cutlass"],
            "drop_addresses": [0xb7822, 0xb7824],
            "drop_rate": [4, 16],
            "attack": 13,
            "attack_address": 0xb780e,
            "hp": 48,
            "hp_address": 0xb780c,
        },
    "Dhuron":
        {
            "enemy_id": 47,
            "xp": 50,
            "xp_address": 0xb71a0,
            "vanilla_drop": ["Rapier", "Hide cuirass"],
            "drop_rate": [8, 32],
            "drop_addresses": [0xb71a2, 0xb71a4],
            "attack": 7,
            "attack_address": 0xb718e,
            "hp": 32,
            "hp_address": 0xb718c,
        },
    "Frog":
        {
            "enemy_id": 48,
            "xp": 20,
            "xp_address": 0xb6b88,
            "vanilla_drop": ["Pizza", "Knuckle duster"],
            "drop_rate": [8, 24],
            "drop_addresses": [0xb6b8a, 0xb6b8c],
            "attack": 13,
            "attack_address": 0xb6b76,
            "hp": 2,
            "hp_address": 0xb6b74,
        },
    "Frozen shade":
        {
            "enemy_id": 49,
            "xp": 40,
            "xp_address": 0xb6a48,
            "vanilla_drop": ["Ice cream", "Ice mail"],
            "drop_rate": [6, 12],
            "drop_addresses": [0xb6a4a, 0xb6a4c],
            "attack": 16,
            "attack_address": 0xb6a36,
            "hp": 16,
            "hp_address": 0xb6a34,
        },
    "Magic tome":
        {
            "enemy_id": 50,
            "xp": 35,
            "xp_address": 0xb8598,
            "vanilla_drop": ["Saber", "$2000"],
            "drop_rate": [4, 4],
            "drop_addresses": [0xb859a, 0xb859c],
            "attack": 12,
            "attack_address": 0xb8586,
            "hp": 22,
            "hp_address": 0xb8584,
        },
    "Skull lord":
        {
            "enemy_id": 51,
            "xp": 50,
            "xp_address": 0xb8728,
            "vanilla_drop": ["Skull shield", "Scimitar"],
            "drop_rate": [2, 16],
            "drop_addresses": [0xb872a, 0xb872c],
            "attack": 25,
            "attack_address": 0xb8716,
            "hp": 80,
            "hp_address": 0xb8714,
        },
    "Black crow":
        {
            "enemy_id": 52,
            "xp": 50,
            "xp_address": 0xb6cc8,
            "vanilla_drop": ["Red bean bun", "Aquamarine"],
            "drop_rate": [6, 24],
            "drop_addresses": [0xb6cca, 0xb6ccc],
            "attack": 10,
            "attack_address": 0xb6cb6,
            "hp": 15,
            "hp_address": 0xb6cb4,
        },
    "Blue raven":
        {
            "enemy_id": 53,
            "xp": 50,
            "xp_address": 0xb6ca0,
            "vanilla_drop": ["Pork bun", "Zircon"],
            "drop_rate": [6, 24],
            "drop_addresses": [0xb6ca2, 0xb6ca4],
            "attack": 10,
            "attack_address": 0xb6c8e,
            "hp": 15,
            "hp_address": 0xb6c8c,
        },
    "Corpseweed":
        {
            "enemy_id": 54,
            "xp": 100,
            "xp_address": 0xb74b0,
            "vanilla_drop": ["Potion", "Antivenom"],
            "drop_rate": [4, 8],
            "drop_addresses": [0xb74b2, 0xb74b4],
            "attack": 20,
            "attack_address": 0xb749e,
            "hp": 18,
            "hp_address": 0xb749c,
        },
    "Flail guard":
        {
            "enemy_id": 55,
            "xp": 50,
            "xp_address": 0xb6440,
            "vanilla_drop": ["Pot roast", "Morningstar"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb6442, 0xb6444],
            "attack": 14,
            "attack_address": 0xb642e,
            "hp": 36,
            "hp_address": 0xb642c,
        },
    "Flea rider":
        {
            "enemy_id": 56,
            "xp": 50,
            "xp_address": 0xb6120,
            "vanilla_drop": ["Ham and eggs", "Turkey"],
            "drop_rate": [6, 16],
            "drop_addresses": [0xb6122, 0xb6124],
            "attack": 18,
            "attack_address": 0xb610e,
            "hp": 17,
            "hp_address": 0xb610c,
        },
    "Spectral sword":
        {
            "enemy_id": 57,
            "xp": 80,
            "xp_address": 0xb6ef8,
            "vanilla_drop": ["Bastard sword", "Broadsword"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb6efa, 0xb6efc],
            "attack": 25,
            "attack_address": 0xb6ee6,
            "hp": 90,
            "hp_address": 0xb6ee4,
        },
    "Bone halberd":
        {
            "enemy_id": 58,
            "xp": 40,
            "xp_address": 0xb6d40,
            "vanilla_drop": ["Ham and eggs", "Javelin"],
            "drop_rate": [6, 8],
            "drop_addresses": [0xb6d42, 0xb6d44],
            "attack": 12,
            "attack_address": 0xb6d2e,
            "hp": 30,
            "hp_address": 0xb6d2c,
        },
    "Scylla":
        {
            "enemy_id": 59,
            "xp": 500,
            "xp_address": 0xb8b38,
            "drop_addresses": [0xb8b3a, 0xb8b3c],
            "attack": 16,
            "attack_address": 0xb8b26,
            "hp": 200,
            "hp_address": 0xb8b24,
        },
    "Hunting girl":
        {
            "enemy_id": 60,
            "xp": 70,
            "xp_address": 0xb80a8,
            "vanilla_drop": ["Cheesecake", "Were bane"],
            "drop_rate": [6, 12],
            "drop_addresses": [0xb80aa, 0xb80ac],
            "attack": 18,
            "attack_address": 0xb8096,
            "hp": 88,
            "hp_address": 0xb8094,
        },
    "Mudman":
        {
            "enemy_id": 61,
            "xp": 50,
            "xp_address": 0xb7ea0,
            "drop_addresses": [0xb7ea2, 0xb7ea4],
            "attack": 20,
            "attack_address": 0xb7e8e,
            "hp": 15,
            "hp_address": 0xb7e8c,
        },
    "Owl knight":
        {
            "enemy_id": 62,
            "xp": 50,
            "xp_address": 0xb5b90,
            "vanilla_drop": ["Medal", "Cutlass"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb5b92, 0xb5b94],
            "attack": 17,
            "attack_address": 0xb5b7e,
            "hp": 180,
            "hp_address": 0xb5b7c,
        },
    "Spectral sword(swords)":
        {
            "enemy_id": 63,
            "xp": 100,
            "xp_address": 0xb7010,
            "vanilla_drop": ["Bastard sword", "Broadsword"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb7012, 0xb7014],
            "attack": 25,
            "attack_address": 0xb6ffe,
            "hp": 100,
            "hp_address": 0xb6ffc,
        },
    "Vandal sword":
        {
            "enemy_id": 64,
            "xp": 100,
            "xp_address": 0xb80d0,
            "vanilla_drop": ["Muramasa", "Holy sword"],
            "drop_rate": [2, 4],
            "drop_addresses": [0xb80d2, 0xb80d4],
            "attack": 30,
            "attack_address": 0xb80be,
            "hp": 120,
            "hp_address": 0xb80bc,
        },
    "Flea armor":
        {
            "enemy_id": 65,
            "xp": 40,
            "xp_address": 0xb5ed8,
            "vanilla_drop": ["Iron cuirass", "High potion"],
            "drop_rate": [8, 10],
            "drop_addresses": [0xb5eda, 0xb5edc],
            "attack": 17,
            "attack_address": 0xb5ec6,
            "hp": 18,
            "hp_address": 0xb5ec4,
        },
    "Hippogryph":
        {
            "enemy_id": 66,
            "xp": 800,
            "xp_address": 0xb8d40,
            "drop_addresses": [0xb8d42, 0xb8d44],
            "attack": 18,
            "attack_address": 0xb8d2e,
            "hp": 800,
            "hp_address": 0xb8d2c,
        },
    "Paranthropus":
        {
            "enemy_id": 67,
            "xp": 50,
            "xp_address": 0xb7e28,
            "vanilla_drop": ["Ring of varda", "Gauntlet"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb7e2a, 0xb7e2c],
            "attack": 24,
            "attack_address": 0xb7e16,
            "hp": 100,
            "hp_address": 0xb7e14,
        },
    "Slime":
        {
            "enemy_id": 68,
            "xp": 50,
            "xp_address": 0xb63f0,
            "drop_addresses": [0xb63f2, 0xb63f4],
            "attack": 16,
            "attack_address": 0xb63de,
            "hp": 32,
            "hp_address": 0xb63dc,
        },
    "Blade master":
        {
            "enemy_id": 69,
            "xp": 80,
            "xp_address": 0xb6de0,
            "vanilla_drop": ["Cross shuriken", "Shotel"],
            "drop_rate": [4, 8],
            "drop_addresses": [0xb6de2, 0xb6de4],
            "attack": 20,
            "attack_address": 0xb6dce,
            "hp": 65,
            "hp_address": 0xb6dcc,
        },
    "Wereskeleton":
        {
            "enemy_id": 70,
            "xp": 50,
            "xp_address": 0xb6328,
            "vanilla_drop": ["Garnet", "Str. potion"],
            "drop_rate": [4, 24],
            "drop_addresses": [0xb632a, 0xb632c],
            "attack": 20,
            "attack_address": 0xb6316,
            "hp": 33,
            "hp_address": 0xb6314,
        },
    "Grave keeper":
        {
            "enemy_id": 71,
            "xp": 60,
            "xp_address": 0xb6c28,
            "vanilla_drop": ["Natou", "Miso soup"],
            "drop_rate": [6, 8],
            "drop_addresses": [0xb6c2a, 0xb6c2c],
            "attack": 20,
            "attack_address": 0xb6c16,
            "hp": 123,
            "hp_address": 0xb6c14,
        },
    "Gremlin":
        {
            "enemy_id": 72,
            "xp": 60,
            "xp_address": 0xb8058,
            "vanilla_drop": ["Fire mail", "Resist fire"],
            "drop_rate": [2, 32],
            "drop_addresses": [0xb805a, 0xb805c],
            "attack": 20,
            "attack_address": 0xb8046,
            "hp": 100,
            "hp_address": 0xb8044,
        },
    "Harpy":
        {
            "enemy_id": 73,
            "xp": 70,
            "xp_address": 0xb8288,
            "vanilla_drop": ["Life apple", "Apple"],
            "drop_rate": [2, 16],
            "drop_addresses": [0xb828a, 0xb828c],
            "attack": 18,
            "attack_address": 0xb8276,
            "hp": 26,
            "hp_address": 0xb8274,
        },
    "Minotaurus":
        {
            "enemy_id": 74,
            "xp": 400,
            "xp_address": 0xb7ce8,
            "drop_addresses": [0xb7cea, 0xb7cec],
            "attack": 20,
            "attack_address": 0xb7cd6,
            "hp": 300,
            "hp_address": 0xb7cd4,
        },
    "Werewolf":
        {
            "enemy_id": 75,
            "xp": 300,
            "xp_address": 0xb7d60,
            "drop_addresses": [0xb7d62, 0xb7d64],
            "attack": 20,
            "attack_address": 0xb7d4e,
            "hp": 260,
            "hp_address": 0xb7d4c,
        },
    "Bone ark":
        {
            "enemy_id": 76,
            "xp": 40,
            "xp_address": 0xb60a8,
            "vanilla_drop": ["Skull shield", "Monster vial 3"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb60aa, 0xb60ac],
            "attack": 20,
            "attack_address": 0xb6096,
            "hp": 250,
            "hp_address": 0xb6094,
        },
    "Valhalla knight":
        {
            "enemy_id": 77,
            "xp": 100,
            "xp_address": 0xb6f98,
            "vanilla_drop": ["Claymore", "Estoc"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb6f9a, 0xb6f9c],
            "attack": 16,
            "attack_address": 0xb6f86,
            "hp": 161,
            "hp_address": 0xb6f84,
        },
    "Cloaked knight":
        {
            "enemy_id": 78,
            "xp": 80,
            "xp_address": 0xb88b8,
            "vanilla_drop": ["Heaven sword", "Flamberge"],
            "drop_rate": [1, 16],
            "drop_addresses": [0xb88ba, 0xb88bc],
            "attack": 20,
            "attack_address": 0xb88a6,
            "hp": 65,
            "hp_address": 0xb88a4,
        },
    "Fishhead":
        {
            "enemy_id": 79,
            "xp": 50,
            "xp_address": 0xb89a8,
            "vanilla_drop": ["Icebrand", "Resist ice"],
            "drop_rate": [8, 32],
            "drop_addresses": [0xb89aa, 0xb89ac],
            "attack": 15,
            "attack_address": 0xb8996,
            "hp": 70,
            "hp_address": 0xb8994,
        },
    "Lesser demon":
        {
            "enemy_id": 80,
            "xp": 100,
            "xp_address": 0xb5c08,
            "vanilla_drop": ["Holbein dagger", "Obsidian sword"],
            "drop_rate": [8, 8],
            "drop_addresses": [0xb5c0a, 0xb5c0c],
            "attack": 20,
            "attack_address": 0xb5bf6,
            "hp": 400,
            "hp_address": 0xb5bf4,
        },
    "Lossoth":
        {
            "enemy_id": 81,
            "xp": 50,
            "xp_address": 0xb6f48,
            "vanilla_drop": ["Firebrand", "Sirloin"],
            "drop_rate": [8, 12],
            "drop_addresses": [0xb6f4a, 0xb6f4c],
            "attack": 18,
            "attack_address": 0xb6f36,
            "hp": 99,
            "hp_address": 0xb6f34,
        },
    "Salem witch":
        {
            "enemy_id": 82,
            "xp": 80,
            "xp_address": 0xb7fb8,
            "vanilla_drop": ["Shortcake", "Gold circlet"],
            "drop_rate": [5, 8],
            "drop_addresses": [0xb7fba, 0xb7fbc],
            "attack": 20,
            "attack_address": 0xb7fa6,
            "hp": 180,
            "hp_address": 0xb7fa4,
        },
    "Blade":
        {
            "enemy_id": 83,
            "xp": 100,
            "xp_address": 0xb79b0,
            "vanilla_drop": ["Gold plate", "Hunter sword"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb79b2, 0xb79b4],
            "attack": 24,
            "attack_address": 0xb799e,
            "hp": 380,
            "hp_address": 0xb799c,
        },
    "Gurkha":
        {
            "enemy_id": 84,
            "xp": 120,
            "xp_address": 0xb7960,
            "vanilla_drop": ["Gold plate", "Combat knife"],
            "drop_rate": [4, 8],
            "drop_addresses": [0xb7962, 0xb7964],
            "attack": 24,
            "attack_address": 0xb794e,
            "hp": 420,
            "hp_address": 0xb794c,
        },
    "Hammer":
        {
            "enemy_id": 85,
            "xp": 110,
            "xp_address": 0xb7910,
            "vanilla_drop": ["Gold plate", "Hammer"],
            "drop_rate": [4, 32],
            "drop_addresses": [0xb7912, 0xb7914],
            "attack": 20,
            "attack_address": 0xb78fe,
            "hp": 250,
            "hp_address": 0xb78fc,
        },
    "Discus lord":
        {
            "enemy_id": 86,
            "xp": 140,
            "xp_address": 0xb65a8,
            "vanilla_drop": ["Jewel sword", "Chakram"],
            "drop_rate": [32, 16],
            "drop_addresses": [0xb65aa, 0xb65ac],
            "attack": 29,
            "attack_address": 0xb6596,
            "hp": 450,
            "hp_address": 0xb6594,
        },
    "Karasuman":
        {
            "enemy_id": 87,
            "xp": 1000,
            "xp_address": 0xb8a20,
            "vanilla_drop": ["Ring of feanor", "Resist dark"],
            "drop_rate": [2, 24],
            "drop_addresses": [0xb8a22, 0xb8a24],
            "attack": 20,
            "attack_address": 0xb8a0e,
            "hp": 500,
            "hp_address": 0xb8a0c,
        },
    "Large slime":
        {
            "enemy_id": 88,
            "xp": 100,
            "xp_address": 0xb63c8,
            "drop_addresses": [0xb63ca, 0xb63cc],
            "attack": 32,
            "attack_address": 0xb63b6,
            "hp": 64,
            "hp_address": 0xb63b4,
        },
    "Hellfire beast":
        {
            "enemy_id": 89,
            "xp": 150,
            "xp_address": 0xb64b8,
            "vanilla_drop": ["Fire mail", "Lightning mail"],
            "drop_rate": [3, 4],
            "drop_addresses": [0xb64ba, 0xb64bc],
            "attack": 17,
            "attack_address": 0xb64a6,
            "hp": 380,
            "hp_address": 0xb64a4,
        },
    "Cerberos":
        {
            "enemy_id": 90,
            "xp": 1500,
            "xp_address": 0xb9978,
            "drop_addresses": [0xb997a, 0xb997c],
            "attack": 20,
            "attack_address": 0xb9966,
            "hp": 800,
            "hp_address": 0xb9964,
        },
    "Killer fish":
        {
            "enemy_id": 91,
            "xp": 100,
            "xp_address": 0xb9640,
            "vanilla_drop": ["Sushi", "Aquamarine"],
            "drop_rate": [2, 32],
            "drop_addresses": [0xb9642, 0xb9644],
            "attack": 50,
            "attack_address": 0xb962e,
            "hp": 120,
            "hp_address": 0xb962c,
        },
    "Olrox":
        {
            "enemy_id": 92,
            "xp": 500,
            "xp_address": 0xb6170,
            "drop_addresses": [0xb6172, 0xb6174],
            "attack": 20,
            "attack_address": 0xb615e,
            "hp": 666,
            "hp_address": 0xb615c,
        },
    "Succubus":
        {
            "enemy_id": 93,
            "xp": 2000,
            "xp_address": 0xb9500,
            "drop_addresses": [0xb9502, 0xb9504],
            "attack": 25,
            "attack_address": 0xb94ee,
            "hp": 666,
            "hp_address": 0xb94ec,
        },
    "Tombstone":
        {
            "enemy_id": 94,
            "xp": 88,
            "xp_address": 0xb6c78,
            "vanilla_drop": ["Green tea", "Katana"],
            "drop_rate": [6, 16],
            "drop_addresses": [0xb6c7a, 0xb6c7c],
            "attack": 40,
            "attack_address": 0xb6c66,
            "hp": 5,
            "hp_address": 0xb6c64,
        },
    "Venus weed":
        {
            "enemy_id": 95,
            "xp": 150,
            "xp_address": 0xb7528,
            "vanilla_drop": ["Heart refresh", "Coral circlet"],
            "drop_rate": [8, 32],
            "drop_addresses": [0xb752a, 0xb752c],
            "attack": 20,
            "attack_address": 0xb7516,
            "hp": 100,
            "hp_address": 0xb7514,
        },
    "Lion":
        {
            "enemy_id": 96,
            "xp": 1000,
            "xp_address": 0xb8750,
            "vanilla_drop": ["Fist of tulkas", "Gauntlet"],
            "drop_rate": [6, 16],
            "drop_addresses": [0xb8752, 0xb8754],
            "attack": 37,
            "attack_address": 0xb873e,
            "hp": 150,
            "hp_address": 0xb873c,
        },
    "Scarecrow":
        {
            "enemy_id": 97,
            "xp": 1000,
            "xp_address": 0xb91e0,
            "vanilla_drop": ["Muramasa", "Javelin"],
            "drop_rate": [1, 24],
            "drop_addresses": [0xb91e2, 0xb91e4],
            "attack": 40,
            "attack_address": 0xb91ce,
            "hp": 120,
            "hp_address": 0xb91cc,
        },
    "Granfaloon":
        {
            "enemy_id": 98,
            "xp": 3000,
            "xp_address": 0xb8c78,
            "drop_addresses": [0xb8c7a, 0xb8c7c],
            "attack": 30,
            "attack_address": 0xb8c66,
            "hp": 400,
            "hp_address": 0xb8c64,
        },
    "Schmoo":
        {
            "enemy_id": 99,
            "xp": 1000,
            "xp_address": 0xb9208,
            "vanilla_drop": ["Crissaegrim", "Ramen"],
            "drop_rate": [1, 8],
            "drop_addresses": [0xb920a, 0xb920c],
            "attack": 40,
            "attack_address": 0xb91f6,
            "hp": 50,
            "hp_address": 0xb91f4,
        },
    "Tin man":
        {
            "enemy_id": 100,
            "xp": 1000,
            "xp_address": 0xb87a0,
            "vanilla_drop": ["Mojo mail", "Lunch A"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb87a2, 0xb87a4],
            "attack": 32,
            "attack_address": 0xb878e,
            "hp": 48,
            "hp_address": 0xb878c,
        },
    "Balloon pod":
        {
            "enemy_id": 101,
            "xp": 88,
            "xp_address": 0xb8ae8,
            "drop_addresses": [0xb8aea, 0xb8aec],
            "attack": 55,
            "attack_address": 0xb8ad6,
            "hp": 3,
            "hp_address": 0xb8ad4,
        },
    "Yorick":
        {
            "enemy_id": 102,
            "xp": 300,
            "xp_address": 0xb6d90,
            "vanilla_drop": ["Skull shield", "Monster vial 3"],
            "drop_rate": [16, 32],
            "drop_addresses": [0xb6d92, 0xb6d94],
            "attack": 20,
            "attack_address": 0xb6d7e,
            "hp": 10,
            "hp_address": 0xb6d7c,
        },
    "Bomb knight":
        {
            "enemy_id": 103,
            "xp": 140,
            "xp_address": 0xb75c8,
            "vanilla_drop": ["Dynamite", "TNT"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb75ca, 0xb75cc],
            "attack": 37,
            "attack_address": 0xb75b6,
            "hp": 46,
            "hp_address": 0xb75b4,
        },
    "Flying zombie":
        {
            "enemy_id": 104,
            "xp": 50,
            "xp_address": 0xb5aa0,
            "vanilla_drop": ["Frankfurter", "Shuriken"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb5aa2, 0xb5aa4],
            "attack": 37,
            "attack_address": 0xb5a8e,
            "hp": 190,
            "hp_address": 0xb5a8c,
        },
    "Bitterfly":
        {
            "enemy_id": 105,
            "xp": 128,
            "xp_address": 0xb7870,
            "vanilla_drop": ["Mystic pendant", "Luck potion"],
            "drop_rate": [16, 48],
            "drop_addresses": [0xb7872, 0xb7874],
            "attack": 55,
            "attack_address": 0xb785e,
            "hp": 4,
            "hp_address": 0xb785c,
        },
    "Jack O'bones":
        {
            "enemy_id": 106,
            "xp": 150,
            "xp_address": 0xb6cf0,
            "vanilla_drop": ["Flame star", "Shuriken"],
            "drop_rate": [4, 8],
            "drop_addresses": [0xb6cf2, 0xb6cf4],
            "attack": 40,
            "attack_address": 0xb6cde,
            "hp": 20,
            "hp_address": 0xb6cdc,
        },
    "Archer":
        {
            "enemy_id": 107,
            "xp": 140,
            "xp_address": 0xb8f38,
            "vanilla_drop": ["Vorpal blade", "Heart refresh"],
            "drop_rate": [1, 4],
            "drop_addresses": [0xb8f3a, 0xb8f3c],
            "attack": 40,
            "attack_address": 0xb8f26,
            "hp": 300,
            "hp_address": 0xb8f24,
        },
    "Werewolf(reverse)":
        {
            "enemy_id": 108,
            "xp": 200,
            "xp_address": 0xb9d88,
            "vanilla_drop": ["Yasutsuna", "Iron fist"],
            "drop_rate": [1, 8],
            "drop_addresses": [0xb9d8a, 0xb9d8c],
            "attack": 40,
            "attack_address": 0xb9d76,
            "hp": 280,
            "hp_address": 0xb9d74,
        },
    "Black panther":
        {
            "enemy_id": 109,
            "xp": 600,
            "xp_address": 0xb5e38,
            "vanilla_drop": ["Masamune", "Meal ticket"],
            "drop_rate": [1, 16],
            "drop_addresses": [0xb5e3a, 0xb5e3c],
            "attack": 45,
            "attack_address": 0xb5e26,
            "hp": 35,
            "hp_address": 0xb5e24,
        },
    "Darkwing bat":
        {
            "enemy_id": 110,
            "xp": 1200,
            "xp_address": 0xb8908,
            "drop_addresses": [0xb890a, 0xb890c],
            "attack": 35,
            "attack_address": 0xb88f6,
            "hp": 600,
            "hp_address": 0xb88f4,
        },
    "Dragon rider":
        {
            "enemy_id": 111,
            "xp": 150,
            "xp_address": 0xb7150,
            "drop_addresses": [0xb7152, 0xb7154],
            "attack": 41,
            "attack_address": 0xb713e,
            "hp": 120,
            "hp_address": 0xb713c,
        },
    "Minotaur":
        {
            "enemy_id": 112,
            "xp": 250,
            "xp_address": 0xb9d10,
            "vanilla_drop": ["Fury plate", "Sirloin"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb9d12, 0xb9d14],
            "attack": 45,
            "attack_address": 0xb9cfe,
            "hp": 320,
            "hp_address": 0xb9cfc,
        },
    "Nova skeleton":
        {
            "enemy_id": 113,
            "xp": 444,
            "xp_address": 0xb6e80,
            "vanilla_drop": ["Terminus est", "Monster vial 3"],
            "drop_rate": [6, 48],
            "drop_addresses": [0xb6e82, 0xb6e84],
            "attack": 20,
            "attack_address": 0xb6e6e,
            "hp": 20,
            "hp_address": 0xb6e6c,
        },
    "Orobourous":
        {
            "enemy_id": 114,
            "xp": 150,
            "xp_address": 0xb70d8,
            "vanilla_drop": ["Lapis lazuli", "Karma coin"],
            "drop_rate": [4, 16],
            "drop_addresses": [0xb70da, 0xb70dc],
            "attack": 47,
            "attack_address": 0xb70c6,
            "hp": 200,
            "hp_address": 0xb70c4,
        },
    "White dragon":
        {
            "enemy_id": 115,
            "xp": 150,
            "xp_address": 0xb5f28,
            "drop_addresses": [0xb5f2a, 0xb5f2c],
            "attack": 60,
            "attack_address": 0xb5f16,
            "hp": 260,
            "hp_address": 0xb5f14,
        },
    "Fire warg":
        {
            "enemy_id": 116,
            "xp": 160,
            "xp_address": 0xb7320,
            "vanilla_drop": ["Karma coin", "Turquoise"],
            "drop_rate": [4, 20],
            "drop_addresses": [0xb7322, 0xb7324],
            "attack": 41,
            "attack_address": 0xb730e,
            "hp": 200,
            "hp_address": 0xb730c,
        },
    "Rock knight":
        {
            "enemy_id": 117,
            "xp": 250,
            "xp_address": 0xb7618,
            "vanilla_drop": ["Platinum mail", "Jewel knuckles"],
            "drop_rate": [8, 16],
            "drop_addresses": [0xb761a, 0xb761c],
            "attack": 50,
            "attack_address": 0xb7606,
            "hp": 160,
            "hp_address": 0xb7604,
        },
    "Sniper of goth":
        {
            "enemy_id": 118,
            "xp": 200,
            "xp_address": 0xb7a78,
            "vanilla_drop": ["Brilliant mail", "Magic missile"],
            "drop_rate": [2, 32],
            "drop_addresses": [0xb7a7a, 0xb7a7c],
            "attack": 40,
            "attack_address": 0xb7a66,
            "hp": 50,
            "hp_address": 0xb7a64,
        },
    "Spectral sword(shields)":
        {
            "enemy_id": 119,
            "xp": 400,
            "xp_address": 0xb7060,
            "vanilla_drop": ["Mablung sword", "Gurthang"],
            "drop_rate": [2, 16],
            "drop_addresses": [0xb7062, 0xb7064],
            "attack": 55,
            "attack_address": 0xb704e,
            "hp": 540,
            "hp_address": 0xb704c,
        },
    "Ghost dancer":
        {
            "enemy_id": 120,
            "xp": 160,
            "xp_address": 0xb7ef0,
            "vanilla_drop": ["Stone mask", "Buffalo star"],
            "drop_rate": [16, 24],
            "drop_addresses": [0xb7ef2, 0xb7ef4],
            "attack": 56,
            "attack_address": 0xb7ede,
            "hp": 30,
            "hp_address": 0xb7edc,
        },
    "Warg rider":
        {
            "enemy_id": 121,
            "xp": 160,
            "xp_address": 0xb7398,
            "drop_addresses": [0xb739a, 0xb739c],
            "attack": 36,
            "attack_address": 0xb7386,
            "hp": 120,
            "hp_address": 0xb7384,
        },
    "Cave troll":
        {
            "enemy_id": 122,
            "xp": 333,
            "xp_address": 0xb73e8,
            "vanilla_drop": ["Nauglamir", "Neutron bomb"],
            "drop_rate": [16, 32],
            "drop_addresses": [0xb73ea, 0xb73ec],
            "attack": 35,
            "attack_address": 0xb73d6,
            "hp": 88,
            "hp_address": 0xb73d4,
        },
    "Dark octopus":
        {
            "enemy_id": 123,
            "xp": 120,
            "xp_address": 0xb5e60,
            "vanilla_drop": ["Green tea", "Sushi"],
            "drop_rate": [10, 16],
            "drop_addresses": [0xb5e62, 0xb5e64],
            "attack": 45,
            "attack_address": 0xb5e4e,
            "hp": 280,
            "hp_address": 0xb5e4c,
        },
    "Fire demon":
        {
            "enemy_id": 124,
            "xp": 666,
            "xp_address": 0xb65f8,
            "vanilla_drop": ["Marsil", "Fire shield"],
            "drop_rate": [4, 6],
            "drop_addresses": [0xb65fa, 0xb65fc],
            "attack": 45,
            "attack_address": 0xb65e6,
            "hp": 320,
            "hp_address": 0xb65e4,
        },
    "Gorgon":
        {
            "enemy_id": 125,
            "xp": 555,
            "xp_address": 0xb5d48,
            "vanilla_drop": ["Stone sword", "Hammer"],
            "drop_rate": [8, 20],
            "drop_addresses": [0xb5d4a, 0xb5d4c],
            "attack": 35,
            "attack_address": 0xb5d36,
            "hp": 240,
            "hp_address": 0xb5d34,
        },
    "Malachi":
        {
            "enemy_id": 126,
            "xp": 666,
            "xp_address": 0xb8210,
            "vanilla_drop": ["Dark armor", "Dark shield"],
            "drop_rate": [4, 8],
            "drop_addresses": [0xb8212, 0xb8214],
            "attack": 52,
            "attack_address": 0xb81fe,
            "hp": 450,
            "hp_address": 0xb81fc,
        },
    "Akmodan II":
        {
            "enemy_id": 127,
            "xp": 2500,
            "xp_address": 0xb8818,
            "drop_addresses": [0xb881a, 0xb881c],
            "attack": 40,
            "attack_address": 0xb8806,
            "hp": 1200,
            "hp_address": 0xb8804,
        },
    "Blue venus weed":
        {
            "enemy_id": 128,
            "xp": 1000,
            "xp_addresses": [0xb9e00, 0xb9e28],
            "vanilla_drop": ["Heart refresh", "Zwei hander"],
            "drop_rate": [4, 4],
            "drop_addresses": [0xb9e02, 0xb9e2a],
            "attack": [35, 45],
            "attack_addresses": [0xb9dee, 0xb9e16],
            "hp": [100, 550],
            "hp_addresses": [0xb9dec, 0xb9e14]
        },
    "Doppleganger40":
        {
            "enemy_id": 129,
            "xp": 2001,
            "xp_address": 0xb9ae0,
            "drop_addresses": [0xb9ae2, 0xb9ae4],
            "attack": 35,
            "attack_address": 0xb9ace,
            "hp": 777,
            "hp_address": 0xb9acc,
        },
    "Medusa":
        {
            "enemy_id": 130,
            "xp": 2500,
            "xp_address": 0xb99f0,
            "drop_addresses": [0xb99f2, 0xb99f4],
            "attack": 35,
            "attack_address": 0xb99de,
            "hp": 1100,
            "hp_address": 0xb99dc,
        },
    "The creature":
        {
            "enemy_id": 131,
            "xp": 2500,
            "xp_address": 0xb9a90,
            "drop_addresses": [0xb9a92, 0xb9a94],
            "attack": 30,
            "attack_address": 0xb9a7e,
            "hp": 1100,
            "hp_address": 0xb9a7c,
        },
    "Fake grant":
        {
            "enemy_id": 132,
            "xp": 1200,
            "xp_address": 0xb93c0,
            "drop_addresses": [0xb93c2, 0xb93c4],
            "attack": 38,
            "attack_address": 0xb93ae,
            "hp": 800,
            "hp_address": 0xb93ac,
        },
    "Fake trevor":
        {
            "enemy_id": 133,
            "xp": 1000,
            "xp_address": 0xb92d0,
            "drop_addresses": [0xb92d2, 0xb92d4],
            "attack": 38,
            "attack_address": 0xb92be,
            "hp": 1200,
            "hp_address": 0xb92bc,
        },
    "Imp":
        {
            "enemy_id": 134,
            "xp": 66,
            "xp_address": 0xb8ac0,
            "vanilla_drop": ["King's stone", "Luck potion"],
            "drop_rate": [4, 32],
            "drop_addresses": [0xb8ac2, 0xb8ac4],
            "attack": 10,
            "attack_address": 0xb8aae,
            "hp": 43,
            "hp_address": 0xb8aac,
        },
    "Fake sypha":
        {
            "enemy_id": 135,
            "xp": 1500,
            "xp_address": 0xb9438,
            "drop_addresses": [0xb943a, 0xb943c],
            "attack": 9,
            "attack_address": 0xb9426,
            "hp": 1000,
            "hp_address": 0xb9424,
        },
    "Beezelbub":
        {
            "enemy_id": 136,
            "xp": 4444,
            "xp_address": 0xb9230,
            "drop_addresses": [0xb9232, 0xb9234],
            "attack": 60,
            "attack_address": 0xb921e,
            "hp": 2000,
            "hp_address": 0xb921c,
        },
    "Azaghal":
        {
            "enemy_id": 137,
            "xp": 700,
            "xp_address": 0xb8030,
            "vanilla_drop": ["Mourneblade", "Covenant stone"],
            "drop_rate": [4, 12],
            "drop_addresses": [0xb8032, 0xb8034],
            "attack": 80,
            "attack_address": 0xb801e,
            "hp": 330,
            "hp_address": 0xb801c,
        },
    "Frozen half":
        {
            "enemy_id": 138,
            "xp": 600,
            "xp_address": 0xb7f18,
            "vanilla_drop": ["Opal circlet", "Necklace of j"],
            "drop_rate": [6, 16],
            "drop_addresses": [0xb7f1a, 0xb7f1c],
            "attack": 35,
            "attack_address": 0xb7f06,
            "hp": 118,
            "hp_address": 0xb7f04,
        },
    "Salome":
        {
            "enemy_id": 139,
            "xp": 450,
            "xp_address": 0xb80f8,
            "vanilla_drop": ["Manna prism", "Wizard hat"],
            "drop_rate": [6, 8],
            "drop_addresses": [0xb80fa, 0xb80fc],
            "attack": 50,
            "attack_address": 0xb80e6,
            "hp": 210,
            "hp_address": 0xb80e4,
        },
    "Richter belmont":
        {
            "enemy_id": 140,
            "xp": 0,
            "xp_address": 0xb8f88,
            "drop_addresses": [0xb8f8a, 0xb8f8c],
            "attack": 25,
            "attack_address": 0xb8f76,
            "hp": 400,
            "hp_address": 0xb8f74,
        },
    "Dodo bird":
        {
            "enemy_id": 141,
            "xp": 111,
            "xp_address": 0xb6b10,
            "vanilla_drop": ["Runesword", "Heart broach"],
            "drop_rate": [2, 8],
            "drop_addresses": [0xb6b12, 0xb6b14],
            "attack": 1,
            "attack_address": 0xb6afe,
            "hp": 2,
            "hp_address": 0xb6afc,
        },
    "Galamoth":
        {
            "enemy_id": 142,
            "xp": 9999,
            "xp_address": 0xb7c20,
            "drop_addresses": [0xb7c22, 0xb7c24],
            "attack": 544,
            "attack_address": 0xb7c0e,
            "hp": 12000,
            "hp_address": 0xb7adc,
        },
    "Guardian":
        {
            "enemy_id": 143,
            "xp": 1500,
            "xp_address": 0xb9ea0,
            "vanilla_drop": ["God's Garb", "Great sword"],
            "drop_rate": [2, 1],
            "drop_addresses": [0xb9ea2, 0xb9ea4],
            "attack": 50,
            "attack_address": 0xb9e8e,
            "hp": 500,
            "hp_address": 0xb9e8c,
        },
    "Death":
        {
            "enemy_id": 144,
            "xp": 4444,
            "xp_address": 0xb9860,
            "drop_addresses": [0xb9862, 0xb9864],
            "attack": 35,
            "attack_address": 0xb984e,
            "hp": 888,
            "hp_address": 0xb984c,
        },
    "Shaft":
        {
            "enemy_id": 145,
            "xp": 0,
            "xp_address": 0xb9668,
            "drop_addresses": [0xb966a, 0xb966c],
            "attack": 40,
            "attack_address": 0xb9656,
            "hp": 1300,
            "hp_address": 0xb9654,
        },
    "Dracula(reverse)":
        {
            "enemy_id": 146,
            "xp": 0,
            "xp_address": 0xb9bf8,
            "drop_addresses": [0xb9bfa, 0xb9bfc],
            "attack": 39,
            "attack_address": 0xb9be6,
            "hp": 10000,
            "hp_address": 0xb9be4,
        },
    "Poltergeist":
        {
            "enemy_id": 147,
            "xp": 0,
            "xp_address": 0xb6f22,
            "vanilla_drop": ["Bwaka knife"],
            "drop_rate": [8],
            "drop_addresses": [0xb6f24],
            "attack": 33,
            "attack_address": 0xb6f10,
            "hp": 20,
            "hp_address": 0xb6f0e,
        },
    "Puppet sword":
        {
            "enemy_id": 148,
            "xp": 0,
            "xp_address": 0xb703a,
            "vanilla_drop": ["Takemitsu"],
            "drop_rate": [16],
            "drop_addresses": [0xb703c],
            "attack": 65,
            "attack_address": 0xb7028,
            "hp": 15,
            "hp_address": 0xb7026,
        },
    "Shield":
        {
            "enemy_id": 149,
            "xp": 0,
            "xp_address": 0xb70b2,
            "vanilla_drop": ["Knight shield"],
            "drop_rate": [32],
            "drop_addresses": [0xb70b4],
            "attack": 33,
            "attack_address": 0xb70a0,
            "hp": 20,
            "hp_address": 0xb709e
        },
    "Spear":
        {
            "enemy_id": 150,
            "xp": 0,
            "xp_address": 0xb708a,
            "vanilla_drop": ["Javelin"],
            "drop_rate": [32],
            "drop_addresses": [0xb708c],
            "attack": 65,
            "attack_address": 0xb7078,
            "hp": 65,
            "hp_address": 0xb7076
        },
    "Ball":
        {
            "enemy_id": 151,
            "xp": 0,
            "xp_address": 0xb6db8,
            "vanilla_drop": ["Turquoise", "Iron ball"],
            "drop_addresses": [0xb6dba, 0xb6dbc],
            "drop_rate": [16, 16],
            "attack": 0,
            "attack_address": 0xb6da6,
            "hp": 2,
            "hp_address": 0xb6da4,
        },
}

enemy_stats_list = [
    {
        "id": 6,
        "name": "Axe knight",
        "nameOffset": 0x0b5948,
        "newNameReference": 0x800e0cc8,
        "newNameText": 0x0f6120,
        "hpOffset": 0x0b594c,
        "hpValue": 42,
        "atkOffset": 0x0b594e,
        "atkValue": 10,
        "atkTypeOffset": 0x0b5950,
        "defOffset": 0x0b5952,
        "defValue": 6,
        "weakOffset": 0x0b5956,
        "resistOffset": 0x0b5958,
        "guardOffset": 0x0b595a,
        "absorbOffset": 0x0b595c
    }, {
        "id": 9,
        "name": "Sword lord",
        "nameOffset": 0x0b59c0,
        "newNameReference": 0x800e0cbc,
        "newNameText": 0x0f6114,
        "hpOffset": 0x0b59c4,
        "hpValue": 61,
        "atkOffset": 0x0b59c6,
        "atkValue": 12,
        "atkTypeOffset": 0x0b59c8,
        "defOffset": 0x0b59ca,
        "defValue": 8,
        "weakOffset": 0x0b59ce,
        "resistOffset": 0x0b59d0,
        "guardOffset": 0x0b59d2,
        "absorbOffset": 0x0b59d4
    }, {
        "id": 11,
        "name": "Skelerang",
        "nameOffset": 0x0b5a10,
        "newNameReference": 0x800e0cb0,
        "newNameText": 0x0f6108,
        "hpOffset": 0x0b5a14,
        "hpValue": 18,
        "atkOffset": 0x0b5a16,
        "atkValue": 12,
        "atkTypeOffset": 0x0b5a18,
        "defOffset": 0x0b5a1a,
        "defValue": 1,
        "weakOffset": 0x0b5a1e,
        "resistOffset": 0x0b5a20,
        "guardOffset": 0x0b5a22,
        "absorbOffset": 0x0b5a24
    }, {
        "id": 13,
        "name": "Bloody zombie",
        "nameOffset": 0x0b5a60,
        "newNameReference": 0x800e0ca4,
        "newNameText": 0x0f60fc,
        "hpOffset": 0x0b5a64,
        "hpValue": 24,
        "atkOffset": 0x0b5a66,
        "atkValue": 10,
        "atkTypeOffset": 0x0b5a68,
        "defOffset": 0x0b5a6a,
        "defValue": 3,
        "weakOffset": 0x0b5a6e,
        "resistOffset": 0x0b5a70,
        "guardOffset": 0x0b5a72,
        "absorbOffset": 0x0b5a74
    }, {
        "id": 14,
        "name": "Flying zombie",
        "nameOffset": 0x0b5a88,
        "newNameReference": 0x800e0c98,
        "newNameText": 0x0f60f0,
        "hpOffset": 0x0b5a8c,
        "hpValue": 190,
        "atkOffset": 0x0b5a8e,
        "atkValue": 37,
        "atkTypeOffset": 0x0b5a90,
        "defOffset": 0x0b5a92,
        "defValue": 10,
        "weakOffset": 0x0b5a96,
        "resistOffset": 0x0b5a98,
        "guardOffset": 0x0b5a9a,
        "absorbOffset": 0x0b5a9c
    }, {
        "id": 15,
        "name": "Flying zombie",
        "nameOffset": 0x0b5ab0,
        "newNameReference": 0x800e0c98,
        "newNameText": 0x0f60f0,
        "hpOffset": 0x0b5ab4,
        "hpValue": 190,
        "atkOffset": 0x0b5ab6,
        "atkValue": 37,
        "atkTypeOffset": 0x0b5ab8,
        "defOffset": 0x0b5aba,
        "defValue": 10,
        "weakOffset": 0x0b5abe,
        "resistOffset": 0x0b5ac0,
        "guardOffset": 0x0b5ac2,
        "absorbOffset": 0x0b5ac4
    }, {
        "id": 16,
        "name": "Diplocephalus",
        "nameOffset": 0x0b5ad8,
        "newNameReference": 0x800e0c8c,
        "newNameText": 0x0f60e4,
        "hpOffset": 0x0b5adc,
        "hpValue": 80,
        "atkOffset": 0x0b5ade,
        "atkValue": 6,
        "atkTypeOffset": 0x0b5ae0,
        "defOffset": 0x0b5ae2,
        "defValue": 1,
        "weakOffset": 0x0b5ae6,
        "resistOffset": 0x0b5ae8,
        "guardOffset": 0x0b5aea,
        "absorbOffset": 0x0b5aec
    }, {
        "id": 20,
        "name": "Owl knight",
        "nameOffset": 0x0b5b78,
        "newNameReference": 0x800e0c80,
        "newNameText": 0x0f60d8,
        "hpOffset": 0x0b5b7c,
        "hpValue": 180,
        "atkOffset": 0x0b5b7e,
        "atkValue": 17,
        "atkTypeOffset": 0x0b5b80,
        "defOffset": 0x0b5b82,
        "defValue": 2,
        "weakOffset": 0x0b5b86,
        "resistOffset": 0x0b5b88,
        "guardOffset": 0x0b5b8a,
        "absorbOffset": 0x0b5b8c
    }, {
        "id": 22,
        "name": "Owl",
        "nameOffset": 0x0b5bc8,
        "newNameReference": 0x800e0c74,
        "newNameText": 0x0f60cc,
        "hpOffset": 0x0b5bcc,
        "hpValue": 26,
        "atkOffset": 0x0b5bce,
        "atkValue": 20,
        "atkTypeOffset": 0x0b5bd0,
        "defOffset": 0x0b5bd2,
        "defValue": 1,
        "weakOffset": 0x0b5bd6,
        "resistOffset": 0x0b5bd8,
        "guardOffset": 0x0b5bda,
        "absorbOffset": 0x0b5bdc
    }, {
        "id": 23,
        "name": "Lesser demon",
        "nameOffset": 0x0b5bf0,
        "newNameReference": 0x800e0c68,
        "newNameText": 0x0f60c0,
        "hpOffset": 0x0b5bf4,
        "hpValue": 400,
        "atkOffset": 0x0b5bf6,
        "atkValue": 20,
        "atkTypeOffset": 0x0b5bf8,
        "defOffset": 0x0b5bfa,
        "defValue": 5,
        "weakOffset": 0x0b5bfe,
        "resistOffset": 0x0b5c00,
        "guardOffset": 0x0b5c02,
        "absorbOffset": 0x0b5c04
    }, {
        "id": 27,
        "name": "Merman",
        "nameOffset": 0x0b5c90,
        "newNameReference": 0x800e0c5c,
        "newNameText": 0x0f60b4,
        "hpOffset": 0x0b5c94,
        "hpValue": 10,
        "atkOffset": 0x0b5c96,
        "atkValue": 13,
        "atkTypeOffset": 0x0b5c98,
        "defOffset": 0x0b5c9a,
        "defValue": 1,
        "weakOffset": 0x0b5c9e,
        "resistOffset": 0x0b5ca0,
        "guardOffset": 0x0b5ca2,
        "absorbOffset": 0x0b5ca4
    }, {
        "id": 29,
        "name": "Merman",
        "nameOffset": 0x0b5ce0,
        "newNameReference": 0x800e0c5c,
        "newNameText": 0x0f60b4,
        "hpOffset": 0x0b5ce4,
        "hpValue": 10,
        "atkOffset": 0x0b5ce6,
        "atkValue": 14,
        "atkTypeOffset": 0x0b5ce8,
        "defOffset": 0x0b5cea,
        "defValue": 1,
        "weakOffset": 0x0b5cee,
        "resistOffset": 0x0b5cf0,
        "guardOffset": 0x0b5cf2,
        "absorbOffset": 0x0b5cf4
    }, {
        "id": 31,
        "name": "Gorgon",
        "nameOffset": 0x0b5d30,
        "newNameReference": 0x800e0c50,
        "newNameText": 0x0f60a8,
        "hpOffset": 0x0b5d34,
        "hpValue": 240,
        "atkOffset": 0x0b5d36,
        "atkValue": 35,
        "atkTypeOffset": 0x0b5d38,
        "defOffset": 0x0b5d3a,
        "defValue": 40,
        "weakOffset": 0x0b5d3e,
        "resistOffset": 0x0b5d40,
        "guardOffset": 0x0b5d42,
        "absorbOffset": 0x0b5d44
    }, {
        "id": 34,
        "name": "Armor lord",
        "nameOffset": 0x0b5da8,
        "newNameReference": 0x800e0c44,
        "newNameText": 0x0f609c,
        "hpOffset": 0x0b5dac,
        "hpValue": 84,
        "atkOffset": 0x0b5dae,
        "atkValue": 18,
        "atkTypeOffset": 0x0b5db0,
        "defOffset": 0x0b5db2,
        "defValue": 6,
        "weakOffset": 0x0b5db6,
        "resistOffset": 0x0b5db8,
        "guardOffset": 0x0b5dba,
        "absorbOffset": 0x0b5dbc
    }, {
        "id": 37,
        "name": "Black panther",
        "nameOffset": 0x0b5e20,
        "newNameReference": 0x800e0c38,
        "newNameText": 0x0f6090,
        "hpOffset": 0x0b5e24,
        "hpValue": 35,
        "atkOffset": 0x0b5e26,
        "atkValue": 45,
        "atkTypeOffset": 0x0b5e28,
        "defOffset": 0x0b5e2a,
        "defValue": 1,
        "weakOffset": 0x0b5e2e,
        "resistOffset": 0x0b5e30,
        "guardOffset": 0x0b5e32,
        "absorbOffset": 0x0b5e34
    }, {
        "id": 38,
        "name": "Dark octopus",
        "nameOffset": 0x0b5e48,
        "newNameReference": 0x800e0c2c,
        "newNameText": 0x0f6084,
        "hpOffset": 0x0b5e4c,
        "hpValue": 280,
        "atkOffset": 0x0b5e4e,
        "atkValue": 45,
        "atkTypeOffset": 0x0b5e50,
        "defOffset": 0x0b5e52,
        "defValue": 2,
        "weakOffset": 0x0b5e56,
        "resistOffset": 0x0b5e58,
        "guardOffset": 0x0b5e5a,
        "absorbOffset": 0x0b5e5c
    }, {
        "id": 40,
        "name": "Flea man",
        "nameOffset": 0x0b5e98,
        "newNameReference": 0x800e0c20,
        "newNameText": 0x0f6078,
        "hpOffset": 0x0b5e9c,
        "hpValue": 11,
        "atkOffset": 0x0b5e9e,
        "atkValue": 9,
        "atkTypeOffset": 0x0b5ea0,
        "defOffset": 0x0b5ea2,
        "defValue": 1,
        "weakOffset": 0x0b5ea6,
        "resistOffset": 0x0b5ea8,
        "guardOffset": 0x0b5eaa,
        "absorbOffset": 0x0b5eac
    }, {
        "id": 41,
        "name": "Flea armor",
        "nameOffset": 0x0b5ec0,
        "newNameReference": 0x800e0c14,
        "newNameText": 0x0f606c,
        "hpOffset": 0x0b5ec4,
        "hpValue": 18,
        "atkOffset": 0x0b5ec6,
        "atkValue": 17,
        "atkTypeOffset": 0x0b5ec8,
        "defOffset": 0x0b5eca,
        "defValue": 1,
        "weakOffset": 0x0b5ece,
        "resistOffset": 0x0b5ed0,
        "guardOffset": 0x0b5ed2,
        "absorbOffset": 0x0b5ed4
    }, {
        "id": 43,
        "name": "White dragon",
        "nameOffset": 0x0b5f10,
        "newNameReference": 0x800e0c08,
        "newNameText": 0x0f6060,
        "hpOffset": 0x0b5f14,
        "hpValue": 260,
        "atkOffset": 0x0b5f16,
        "atkValue": 60,
        "atkTypeOffset": 0x0b5f18,
        "defOffset": 0x0b5f1a,
        "defValue": 2,
        "weakOffset": 0x0b5f1e,
        "resistOffset": 0x0b5f20,
        "guardOffset": 0x0b5f22,
        "absorbOffset": 0x0b5f24
    }, {
        "id": 45,
        "name": "Bone ark",
        "nameOffset": 0x0b6090,
        "newNameReference": 0x800e0bfc,
        "newNameText": 0x0f6054,
        "hpOffset": 0x0b6094,
        "hpValue": 250,
        "atkOffset": 0x0b6096,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6098,
        "defOffset": 0x0b609a,
        "defValue": 4,
        "weakOffset": 0x0b609e,
        "resistOffset": 0x0b60a0,
        "guardOffset": 0x0b60a2,
        "absorbOffset": 0x0b60a4
    }, {
        "id": 46,
        "name": "Bone ark",
        "nameOffset": 0x0b60b8,
        "newNameReference": 0x800e0bfc,
        "newNameText": 0x0f6054,
        "hpOffset": 0x0b60bc,
        "hpValue": 140,
        "atkOffset": 0x0b60be,
        "atkValue": 20,
        "atkTypeOffset": 0x0b60c0,
        "defOffset": 0x0b60c2,
        "defValue": 2,
        "weakOffset": 0x0b60c6,
        "resistOffset": 0x0b60c8,
        "guardOffset": 0x0b60ca,
        "absorbOffset": 0x0b60cc
    }, {
        "id": 48,
        "name": "Flea rider",
        "nameOffset": 0x0b6108,
        "newNameReference": 0x800e0bf0,
        "newNameText": 0x0f6048,
        "hpOffset": 0x0b610c,
        "hpValue": 17,
        "atkOffset": 0x0b610e,
        "atkValue": 18,
        "atkTypeOffset": 0x0b6110,
        "defOffset": 0x0b6112,
        "defValue": 1,
        "weakOffset": 0x0b6116,
        "resistOffset": 0x0b6118,
        "guardOffset": 0x0b611a,
        "absorbOffset": 0x0b611c
    }, {
        "id": 49,
        "name": "Marionette",
        "nameOffset": 0x0b6130,
        "newNameReference": 0x800e0be4,
        "newNameText": 0x0f603c,
        "hpOffset": 0x0b6134,
        "hpValue": 20,
        "atkOffset": 0x0b6136,
        "atkValue": 8,
        "atkTypeOffset": 0x0b6138,
        "defOffset": 0x0b613a,
        "defValue": 2,
        "weakOffset": 0x0b613e,
        "resistOffset": 0x0b6140,
        "guardOffset": 0x0b6142,
        "absorbOffset": 0x0b6144
    }, {
        "id": 50,
        "name": "Olrox",
        "nameOffset": 0x0b6158,
        "newNameReference": 0x800e0bd8,
        "newNameText": 0x0f6030,
        "hpOffset": 0x0b615c,
        "hpValue": 666,
        "atkOffset": 0x0b615e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6160,
        "defOffset": 0x0b6162,
        "defValue": 8,
        "weakOffset": 0x0b6166,
        "resistOffset": 0x0b6168,
        "guardOffset": 0x0b616a,
        "absorbOffset": 0x0b616c
    }, {
        "id": 61,
        "name": "Wereskeleton",
        "nameOffset": 0x0b6310,
        "newNameReference": 0x800e0bcc,
        "newNameText": 0x0f6024,
        "hpOffset": 0x0b6314,
        "hpValue": 33,
        "atkOffset": 0x0b6316,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6318,
        "defOffset": 0x0b631a,
        "defValue": 4,
        "weakOffset": 0x0b631e,
        "resistOffset": 0x0b6320,
        "guardOffset": 0x0b6322,
        "absorbOffset": 0x0b6324
    }, {
        "id": 64,
        "name": "Bat",
        "nameOffset": 0x0b6388,
        "newNameReference": 0x800e0bc0,
        "newNameText": 0x0f6018,
        "hpOffset": 0x0b638c,
        "hpValue": 1,
        "atkOffset": 0x0b638e,
        "atkValue": 16,
        "atkTypeOffset": 0x0b6390,
        "defOffset": 0x0b6392,
        "defValue": 1,
        "weakOffset": 0x0b6396,
        "resistOffset": 0x0b6398,
        "guardOffset": 0x0b639a,
        "absorbOffset": 0x0b639c
    }, {
        "id": 65,
        "name": "Large slime",
        "nameOffset": 0x0b63b0,
        "newNameReference": 0x800e0bb4,
        "newNameText": 0x0f600c,
        "hpOffset": 0x0b63b4,
        "hpValue": 64,
        "atkOffset": 0x0b63b6,
        "atkValue": 32,
        "atkTypeOffset": 0x0b63b8,
        "defOffset": 0x0b63ba,
        "defValue": 10,
        "weakOffset": 0x0b63be,
        "resistOffset": 0x0b63c0,
        "guardOffset": 0x0b63c2,
        "absorbOffset": 0x0b63c4
    }, {
        "id": 66,
        "name": "Slime",
        "nameOffset": 0x0b63d8,
        "newNameReference": 0x800e0ba8,
        "newNameText": 0x0f6000,
        "hpOffset": 0x0b63dc,
        "hpValue": 32,
        "atkOffset": 0x0b63de,
        "atkValue": 16,
        "atkTypeOffset": 0x0b63e0,
        "defOffset": 0x0b63e2,
        "defValue": 10,
        "weakOffset": 0x0b63e6,
        "resistOffset": 0x0b63e8,
        "guardOffset": 0x0b63ea,
        "absorbOffset": 0x0b63ec
    }, {
        "id": 67,
        "name": "Phantom skull",
        "nameOffset": 0x0b6400,
        "newNameReference": 0x800e0b9c,
        "newNameText": 0x0f5ff4,
        "hpOffset": 0x0b6404,
        "hpValue": 15,
        "atkOffset": 0x0b6406,
        "atkValue": 14,
        "atkTypeOffset": 0x0b6408,
        "defOffset": 0x0b640a,
        "defValue": 1,
        "weakOffset": 0x0b640e,
        "resistOffset": 0x0b6410,
        "guardOffset": 0x0b6412,
        "absorbOffset": 0x0b6414
    }, {
        "id": 68,
        "name": "Flail guard",
        "nameOffset": 0x0b6428,
        "newNameReference": 0x800e0b90,
        "newNameText": 0x0f5fe8,
        "hpOffset": 0x0b642c,
        "hpValue": 36,
        "atkOffset": 0x0b642e,
        "atkValue": 14,
        "atkTypeOffset": 0x0b6430,
        "defOffset": 0x0b6432,
        "defValue": 2,
        "weakOffset": 0x0b6436,
        "resistOffset": 0x0b6438,
        "guardOffset": 0x0b643a,
        "absorbOffset": 0x0b643c
    }, {
        "id": 70,
        "name": "Blood skeleton",
        "nameOffset": 0x0b6478,
        "newNameReference": 0x800e0b84,
        "newNameText": 0x0f5fdc,
        "hpOffset": 0x0b647c,
        "hpValue": 9,
        "atkOffset": 0x0b647e,
        "atkValue": 8,
        "atkTypeOffset": 0x0b6480,
        "defOffset": 0x0b6482,
        "defValue": 1,
        "weakOffset": 0x0b6486,
        "resistOffset": 0x0b6488,
        "guardOffset": 0x0b648a,
        "absorbOffset": 0x0b648c
    }, {
        "id": 71,
        "name": "Hellfire beast",
        "nameOffset": 0x0b64a0,
        "newNameReference": 0x800e0b78,
        "newNameText": 0x0f5fd0,
        "hpOffset": 0x0b64a4,
        "hpValue": 380,
        "atkOffset": 0x0b64a6,
        "atkValue": 17,
        "atkTypeOffset": 0x0b64a8,
        "defOffset": 0x0b64aa,
        "defValue": 8,
        "weakOffset": 0x0b64ae,
        "resistOffset": 0x0b64b0,
        "guardOffset": 0x0b64b2,
        "absorbOffset": 0x0b64b4
    }, {
        "id": 75,
        "name": "Skeleton",
        "nameOffset": 0x0b6540,
        "newNameReference": 0x800e0b6c,
        "newNameText": 0x0f5fc4,
        "hpOffset": 0x0b6544,
        "hpValue": 9,
        "atkOffset": 0x0b6546,
        "atkValue": 2,
        "atkTypeOffset": 0x0b6548,
        "defOffset": 0x0b654a,
        "defValue": 1,
        "weakOffset": 0x0b654e,
        "resistOffset": 0x0b6550,
        "guardOffset": 0x0b6552,
        "absorbOffset": 0x0b6554
    }, {
        "id": 77,
        "name": "Discus lord",
        "nameOffset": 0x0b6590,
        "newNameReference": 0x800e0b60,
        "newNameText": 0x0f5fb8,
        "hpOffset": 0x0b6594,
        "hpValue": 450,
        "atkOffset": 0x0b6596,
        "atkValue": 29,
        "atkTypeOffset": 0x0b6598,
        "defOffset": 0x0b659a,
        "defValue": 10,
        "weakOffset": 0x0b659e,
        "resistOffset": 0x0b65a0,
        "guardOffset": 0x0b65a2,
        "absorbOffset": 0x0b65a4
    }, {
        "id": 79,
        "name": "Fire demon",
        "nameOffset": 0x0b65e0,
        "newNameReference": 0x800e0b54,
        "newNameText": 0x0f5fac,
        "hpOffset": 0x0b65e4,
        "hpValue": 320,
        "atkOffset": 0x0b65e6,
        "atkValue": 45,
        "atkTypeOffset": 0x0b65e8,
        "defOffset": 0x0b65ea,
        "defValue": 15,
        "weakOffset": 0x0b65ee,
        "resistOffset": 0x0b65f0,
        "guardOffset": 0x0b65f2,
        "absorbOffset": 0x0b65f4
    }, {
        "id": 81,
        "name": "Spittle bone",
        "nameOffset": 0x0b6630,
        "newNameReference": 0x800e0b48,
        "newNameText": 0x0f5fa0,
        "hpOffset": 0x0b6634,
        "hpValue": 18,
        "atkOffset": 0x0b6636,
        "atkValue": 7,
        "atkTypeOffset": 0x0b6638,
        "defOffset": 0x0b663a,
        "defValue": 3,
        "weakOffset": 0x0b663e,
        "resistOffset": 0x0b6640,
        "guardOffset": 0x0b6642,
        "absorbOffset": 0x0b6644
    }, {
        "id": 83,
        "name": "Skeleton ape",
        "nameOffset": 0x0b6680,
        "newNameReference": 0x800e0b3c,
        "newNameText": 0x0f5f94,
        "hpOffset": 0x0b6684,
        "hpValue": 10,
        "atkOffset": 0x0b6686,
        "atkValue": 10,
        "atkTypeOffset": 0x0b6688,
        "defOffset": 0x0b668a,
        "defValue": 2,
        "weakOffset": 0x0b668e,
        "resistOffset": 0x0b6690,
        "guardOffset": 0x0b6692,
        "absorbOffset": 0x0b6694
    }, {
        "id": 85,
        "name": "Stone rose",
        "nameOffset": 0x0b66d0,
        "newNameReference": 0x800e0b30,
        "newNameText": 0x0f5f88,
        "hpOffset": 0x0b66d4,
        "hpValue": 60,
        "atkOffset": 0x0b66d6,
        "atkValue": 12,
        "atkTypeOffset": 0x0b66d8,
        "defOffset": 0x0b66da,
        "defValue": 1,
        "weakOffset": 0x0b66de,
        "resistOffset": 0x0b66e0,
        "guardOffset": 0x0b66e2,
        "absorbOffset": 0x0b66e4
    }, {
        "id": 88,
        "name": "Ectoplasm",
        "nameOffset": 0x0b6748,
        "newNameReference": 0x800e0b24,
        "newNameText": 0x0f5f7c,
        "hpOffset": 0x0b674c,
        "hpValue": 18,
        "atkOffset": 0x0b674e,
        "atkValue": 6,
        "atkTypeOffset": 0x0b6750,
        "defOffset": 0x0b6752,
        "defValue": 6,
        "weakOffset": 0x0b6756,
        "resistOffset": 0x0b6758,
        "guardOffset": 0x0b675a,
        "absorbOffset": 0x0b675c
    }, {
        "id": 90,
        "name": "Bone pillar",
        "nameOffset": 0x0b6798,
        "newNameReference": 0x800e0b18,
        "newNameText": 0x0f5f70,
        "hpOffset": 0x0b679c,
        "hpValue": 16,
        "atkOffset": 0x0b679e,
        "atkValue": 1,
        "atkTypeOffset": 0x0b67a0,
        "defOffset": 0x0b67a2,
        "defValue": 8,
        "weakOffset": 0x0b67a6,
        "resistOffset": 0x0b67a8,
        "guardOffset": 0x0b67aa,
        "absorbOffset": 0x0b67ac
    }, {
        "id": 93,
        "name": "Spear guard",
        "nameOffset": 0x0b6810,
        "newNameReference": 0x800e0b0c,
        "newNameText": 0x0f5f64,
        "hpOffset": 0x0b6814,
        "hpValue": 20,
        "atkOffset": 0x0b6816,
        "atkValue": 12,
        "atkTypeOffset": 0x0b6818,
        "defOffset": 0x0b681a,
        "defValue": 4,
        "weakOffset": 0x0b681e,
        "resistOffset": 0x0b6820,
        "guardOffset": 0x0b6822,
        "absorbOffset": 0x0b6824
    }, {
        "id": 97,
        "name": "Plate lord",
        "nameOffset": 0x0b69e0,
        "newNameReference": 0x800e0b00,
        "newNameText": 0x0f5f58,
        "hpOffset": 0x0b69e4,
        "hpValue": 90,
        "atkOffset": 0x0b69e6,
        "atkValue": 18,
        "atkTypeOffset": 0x0b69e8,
        "defOffset": 0x0b69ea,
        "defValue": 6,
        "weakOffset": 0x0b69ee,
        "resistOffset": 0x0b69f0,
        "guardOffset": 0x0b69f2,
        "absorbOffset": 0x0b69f4
    }, {
        "id": 99,
        "name": "Frozen shade",
        "nameOffset": 0x0b6a30,
        "newNameReference": 0x800e0af4,
        "newNameText": 0x0f5f4c,
        "hpOffset": 0x0b6a34,
        "hpValue": 16,
        "atkOffset": 0x0b6a36,
        "atkValue": 16,
        "atkTypeOffset": 0x0b6a38,
        "defOffset": 0x0b6a3a,
        "defValue": 1,
        "weakOffset": 0x0b6a3e,
        "resistOffset": 0x0b6a40,
        "guardOffset": 0x0b6a42,
        "absorbOffset": 0x0b6a44
    }, {
        "id": 102,
        "name": "Bone musket",
        "nameOffset": 0x0b6aa8,
        "newNameReference": 0x800e0ae8,
        "newNameText": 0x0f5f40,
        "hpOffset": 0x0b6aac,
        "hpValue": 24,
        "atkOffset": 0x0b6aae,
        "atkValue": 12,
        "atkTypeOffset": 0x0b6ab0,
        "defOffset": 0x0b6ab2,
        "defValue": 5,
        "weakOffset": 0x0b6ab6,
        "resistOffset": 0x0b6ab8,
        "guardOffset": 0x0b6aba,
        "absorbOffset": 0x0b6abc
    }, {
        "id": 104,
        "name": "Dodo bird",
        "nameOffset": 0x0b6af8,
        "newNameReference": 0x800e0adc,
        "newNameText": 0x0f5f34,
        "hpOffset": 0x0b6afc,
        "hpValue": 2,
        "atkOffset": 0x0b6afe,
        "atkValue": 1,
        "atkTypeOffset": 0x0b6b00,
        "defOffset": 0x0b6b02,
        "defValue": 1,
        "weakOffset": 0x0b6b06,
        "resistOffset": 0x0b6b08,
        "guardOffset": 0x0b6b0a,
        "absorbOffset": 0x0b6b0c
    }, {
        "id": 105,
        "name": "Bone scimitar",
        "nameOffset": 0x0b6b20,
        "newNameReference": 0x800e0ad0,
        "newNameText": 0x0f5f28,
        "hpOffset": 0x0b6b24,
        "hpValue": 18,
        "atkOffset": 0x0b6b26,
        "atkValue": 5,
        "atkTypeOffset": 0x0b6b28,
        "defOffset": 0x0b6b2a,
        "defValue": 2,
        "weakOffset": 0x0b6b2e,
        "resistOffset": 0x0b6b30,
        "guardOffset": 0x0b6b32,
        "absorbOffset": 0x0b6b34
    }, {
        "id": 106,
        "name": "Toad",
        "nameOffset": 0x0b6b48,
        "newNameReference": 0x800e0ac4,
        "newNameText": 0x0f5f1c,
        "hpOffset": 0x0b6b4c,
        "hpValue": 10,
        "atkOffset": 0x0b6b4e,
        "atkValue": 14,
        "atkTypeOffset": 0x0b6b50,
        "defOffset": 0x0b6b52,
        "defValue": 4,
        "weakOffset": 0x0b6b56,
        "resistOffset": 0x0b6b58,
        "guardOffset": 0x0b6b5a,
        "absorbOffset": 0x0b6b5c
    }, {
        "id": 107,
        "name": "Frog",
        "nameOffset": 0x0b6b70,
        "newNameReference": 0x800e0ab8,
        "newNameText": 0x0f5f10,
        "hpOffset": 0x0b6b74,
        "hpValue": 2,
        "atkOffset": 0x0b6b76,
        "atkValue": 13,
        "atkTypeOffset": 0x0b6b78,
        "defOffset": 0x0b6b7a,
        "defValue": 1,
        "weakOffset": 0x0b6b7e,
        "resistOffset": 0x0b6b80,
        "guardOffset": 0x0b6b82,
        "absorbOffset": 0x0b6b84
    }, {
        "id": 108,
        "name": "Bone archer",
        "nameOffset": 0x0b6b98,
        "newNameReference": 0x800e0aac,
        "newNameText": 0x0f5f04,
        "hpOffset": 0x0b6b9c,
        "hpValue": 10,
        "atkOffset": 0x0b6b9e,
        "atkValue": 12,
        "atkTypeOffset": 0x0b6ba0,
        "defOffset": 0x0b6ba2,
        "defValue": 4,
        "weakOffset": 0x0b6ba6,
        "resistOffset": 0x0b6ba8,
        "guardOffset": 0x0b6baa,
        "absorbOffset": 0x0b6bac
    }, {
        "id": 110,
        "name": "Zombie",
        "nameOffset": 0x0b6be8,
        "newNameReference": 0x800e0aa0,
        "newNameText": 0x0f5ef8,
        "hpOffset": 0x0b6bec,
        "hpValue": 1,
        "atkOffset": 0x0b6bee,
        "atkValue": 14,
        "atkTypeOffset": 0x0b6bf0,
        "defOffset": 0x0b6bf2,
        "defValue": 1,
        "weakOffset": 0x0b6bf6,
        "resistOffset": 0x0b6bf8,
        "guardOffset": 0x0b6bfa,
        "absorbOffset": 0x0b6bfc
    }, {
        "id": 111,
        "name": "Grave keeper",
        "nameOffset": 0x0b6c10,
        "newNameReference": 0x800e0a94,
        "newNameText": 0x0f5eec,
        "hpOffset": 0x0b6c14,
        "hpValue": 123,
        "atkOffset": 0x0b6c16,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6c18,
        "defOffset": 0x0b6c1a,
        "defValue": 1,
        "weakOffset": 0x0b6c1e,
        "resistOffset": 0x0b6c20,
        "guardOffset": 0x0b6c22,
        "absorbOffset": 0x0b6c24
    }, {
        "id": 113,
        "name": "Tombstone",
        "nameOffset": 0x0b6c60,
        "newNameReference": 0x800e0a88,
        "newNameText": 0x0f5ee0,
        "hpOffset": 0x0b6c64,
        "hpValue": 5,
        "atkOffset": 0x0b6c66,
        "atkValue": 40,
        "atkTypeOffset": 0x0b6c68,
        "defOffset": 0x0b6c6a,
        "defValue": 100,
        "weakOffset": 0x0b6c6e,
        "resistOffset": 0x0b6c70,
        "guardOffset": 0x0b6c72,
        "absorbOffset": 0x0b6c74
    }, {
        "id": 114,
        "name": "Blue raven",
        "nameOffset": 0x0b6c88,
        "newNameReference": 0x800e0a7c,
        "newNameText": 0x0f5ed4,
        "hpOffset": 0x0b6c8c,
        "hpValue": 15,
        "atkOffset": 0x0b6c8e,
        "atkValue": 10,
        "atkTypeOffset": 0x0b6c90,
        "defOffset": 0x0b6c92,
        "defValue": 1,
        "weakOffset": 0x0b6c96,
        "resistOffset": 0x0b6c98,
        "guardOffset": 0x0b6c9a,
        "absorbOffset": 0x0b6c9c
    }, {
        "id": 115,
        "name": "Black crow",
        "nameOffset": 0x0b6cb0,
        "newNameReference": 0x800e0a70,
        "newNameText": 0x0f5ec8,
        "hpOffset": 0x0b6cb4,
        "hpValue": 15,
        "atkOffset": 0x0b6cb6,
        "atkValue": 10,
        "atkTypeOffset": 0x0b6cb8,
        "defOffset": 0x0b6cba,
        "defValue": 1,
        "weakOffset": 0x0b6cbe,
        "resistOffset": 0x0b6cc0,
        "guardOffset": 0x0b6cc2,
        "absorbOffset": 0x0b6cc4
    }, {
        "id": 116,
        "name": "Jack o'bones",
        "nameOffset": 0x0b6cd8,
        "newNameReference": 0x800e0a64,
        "newNameText": 0x0f5ebc,
        "hpOffset": 0x0b6cdc,
        "hpValue": 20,
        "atkOffset": 0x0b6cde,
        "atkValue": 40,
        "atkTypeOffset": 0x0b6ce0,
        "defOffset": 0x0b6ce2,
        "defValue": 4,
        "weakOffset": 0x0b6ce6,
        "resistOffset": 0x0b6ce8,
        "guardOffset": 0x0b6cea,
        "absorbOffset": 0x0b6cec
    }, {
        "id": 118,
        "name": "Bone halberd",
        "nameOffset": 0x0b6d28,
        "newNameReference": 0x800e0a58,
        "newNameText": 0x0f5eb0,
        "hpOffset": 0x0b6d2c,
        "hpValue": 30,
        "atkOffset": 0x0b6d2e,
        "atkValue": 12,
        "atkTypeOffset": 0x0b6d30,
        "defOffset": 0x0b6d32,
        "defValue": 2,
        "weakOffset": 0x0b6d36,
        "resistOffset": 0x0b6d38,
        "guardOffset": 0x0b6d3a,
        "absorbOffset": 0x0b6d3c
    }, {
        "id": 120,
        "name": "Yorick",
        "nameOffset": 0x0b6d78,
        "newNameReference": 0x800e0a4c,
        "newNameText": 0x0f5ea4,
        "hpOffset": 0x0b6d7c,
        "hpValue": 10,
        "atkOffset": 0x0b6d7e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6d80,
        "defOffset": 0x0b6d82,
        "defValue": 2,
        "weakOffset": 0x0b6d86,
        "resistOffset": 0x0b6d88,
        "guardOffset": 0x0b6d8a,
        "absorbOffset": 0x0b6d8c
    }, {
        "id": 121,
        "name": "Skull",
        "nameOffset": 0x0b6da0,
        "newNameReference": 0x800e0a40,
        "newNameText": 0x0f5e98,
        "hpOffset": 0x0b6da4,
        "hpValue": 2,
        "atkOffset": 0x0b6da6,
        "atkValue": 1,
        "atkTypeOffset": 0x0b6da8,
        "defOffset": 0x0b6daa,
        "defValue": 1,
        "weakOffset": 0x0b6dae,
        "resistOffset": 0x0b6db0,
        "guardOffset": 0x0b6db2,
        "absorbOffset": 0x0b6db4
    }, {
        "id": 122,
        "name": "Blade master",
        "nameOffset": 0x0b6dc8,
        "newNameReference": 0x800e0a34,
        "newNameText": 0x0f5e8c,
        "hpOffset": 0x0b6dcc,
        "hpValue": 65,
        "atkOffset": 0x0b6dce,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6dd0,
        "defOffset": 0x0b6dd2,
        "defValue": 4,
        "weakOffset": 0x0b6dd6,
        "resistOffset": 0x0b6dd8,
        "guardOffset": 0x0b6dda,
        "absorbOffset": 0x0b6ddc
    }, {
        "id": 124,
        "name": "Blade soldier",
        "nameOffset": 0x0b6e18,
        "newNameReference": 0x800e0a28,
        "newNameText": 0x0f5e80,
        "hpOffset": 0x0b6e1c,
        "hpValue": 16,
        "atkOffset": 0x0b6e1e,
        "atkValue": 15,
        "atkTypeOffset": 0x0b6e20,
        "defOffset": 0x0b6e22,
        "defValue": 4,
        "weakOffset": 0x0b6e26,
        "resistOffset": 0x0b6e28,
        "guardOffset": 0x0b6e2a,
        "absorbOffset": 0x0b6e2c
    }, {
        "id": 126,
        "name": "Nova skeleton",
        "nameOffset": 0x0b6e68,
        "newNameReference": 0x800e0a1c,
        "newNameText": 0x0f5e74,
        "hpOffset": 0x0b6e6c,
        "hpValue": 20,
        "atkOffset": 0x0b6e6e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6e70,
        "defOffset": 0x0b6e72,
        "defValue": 4,
        "weakOffset": 0x0b6e76,
        "resistOffset": 0x0b6e78,
        "guardOffset": 0x0b6e7a,
        "absorbOffset": 0x0b6e7c
    }, {
        "id": 128,
        "name": "Winged guard",
        "nameOffset": 0x0b6eb8,
        "newNameReference": 0x800e0a10,
        "newNameText": 0x0f5e68,
        "hpOffset": 0x0b6ebc,
        "hpValue": 15,
        "atkOffset": 0x0b6ebe,
        "atkValue": 12,
        "atkTypeOffset": 0x0b6ec0,
        "defOffset": 0x0b6ec2,
        "defValue": 1,
        "weakOffset": 0x0b6ec6,
        "resistOffset": 0x0b6ec8,
        "guardOffset": 0x0b6eca,
        "absorbOffset": 0x0b6ecc
    }, {
        "id": 129,
        "name": "Spectral sword",
        "nameOffset": 0x0b6ee0,
        "newNameReference": 0x800e0a04,
        "newNameText": 0x0f5e5c,
        "hpOffset": 0x0b6ee4,
        "hpValue": 90,
        "atkOffset": 0x0b6ee6,
        "atkValue": 25,
        "atkTypeOffset": 0x0b6ee8,
        "defOffset": 0x0b6eea,
        "defValue": 4,
        "weakOffset": 0x0b6eee,
        "resistOffset": 0x0b6ef0,
        "guardOffset": 0x0b6ef2,
        "absorbOffset": 0x0b6ef4
    }, {
        "id": 130,
        "name": "Poltergeist",
        "nameOffset": 0x0b6f08,
        "newNameReference": 0x800e09f8,
        "newNameText": 0x0f5e50,
        "hpOffset": 0x0b6f0c,
        "hpValue": 30,
        "atkOffset": 0x0b6f0e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b6f10,
        "defOffset": 0x0b6f12,
        "defValue": 2,
        "weakOffset": 0x0b6f16,
        "resistOffset": 0x0b6f18,
        "guardOffset": 0x0b6f1a,
        "absorbOffset": 0x0b6f1c
    }, {
        "id": 131,
        "name": "Lossoth",
        "nameOffset": 0x0b6f30,
        "newNameReference": 0x800e09ec,
        "newNameText": 0x0f5e44,
        "hpOffset": 0x0b6f34,
        "hpValue": 99,
        "atkOffset": 0x0b6f36,
        "atkValue": 18,
        "atkTypeOffset": 0x0b6f38,
        "defOffset": 0x0b6f3a,
        "defValue": 1,
        "weakOffset": 0x0b6f3e,
        "resistOffset": 0x0b6f40,
        "guardOffset": 0x0b6f42,
        "absorbOffset": 0x0b6f44
    }, {
        "id": 133,
        "name": "Valhalla knight",
        "nameOffset": 0x0b6f80,
        "newNameReference": 0x800e09e0,
        "newNameText": 0x0f5e38,
        "hpOffset": 0x0b6f84,
        "hpValue": 161,
        "atkOffset": 0x0b6f86,
        "atkValue": 16,
        "atkTypeOffset": 0x0b6f88,
        "defOffset": 0x0b6f8a,
        "defValue": 1,
        "weakOffset": 0x0b6f8e,
        "resistOffset": 0x0b6f90,
        "guardOffset": 0x0b6f92,
        "absorbOffset": 0x0b6f94
    }, {
        "id": 136,
        "name": "Spectral sword",
        "nameOffset": 0x0b6ff8,
        "newNameReference": 0x800e09d4,
        "newNameText": 0x0f5e2c,
        "hpOffset": 0x0b6ffc,
        "hpValue": 100,
        "atkOffset": 0x0b6ffe,
        "atkValue": 25,
        "atkTypeOffset": 0x0b7000,
        "defOffset": 0x0b7002,
        "defValue": 6,
        "weakOffset": 0x0b7006,
        "resistOffset": 0x0b7008,
        "guardOffset": 0x0b700a,
        "absorbOffset": 0x0b700c
    }, {
        "id": 137,
        "name": "Puppet sword",
        "nameOffset": 0x0b7020,
        "newNameReference": 0x800e09c8,
        "newNameText": 0x0f5e20,
        "hpOffset": 0x0b7024,
        "hpValue": 20,
        "atkOffset": 0x0b7026,
        "atkValue": 15,
        "atkTypeOffset": 0x0b7028,
        "defOffset": 0x0b702a,
        "defValue": 4,
        "weakOffset": 0x0b702e,
        "resistOffset": 0x0b7030,
        "guardOffset": 0x0b7032,
        "absorbOffset": 0x0b7034
    }, {
        "id": 138,
        "name": "Spectral sword",
        "nameOffset": 0x0b7048,
        "newNameReference": 0x800e09bc,
        "newNameText": 0x0f5e14,
        "hpOffset": 0x0b704c,
        "hpValue": 540,
        "atkOffset": 0x0b704e,
        "atkValue": 55,
        "atkTypeOffset": 0x0b7050,
        "defOffset": 0x0b7052,
        "defValue": 4,
        "weakOffset": 0x0b7056,
        "resistOffset": 0x0b7058,
        "guardOffset": 0x0b705a,
        "absorbOffset": 0x0b705c
    }, {
        "id": 139,
        "name": "Spear",
        "nameOffset": 0x0b7070,
        "newNameReference": 0x800e09b0,
        "newNameText": 0x0f5e08,
        "hpOffset": 0x0b7074,
        "hpValue": 10,
        "atkOffset": 0x0b7076,
        "atkValue": 65,
        "atkTypeOffset": 0x0b7078,
        "defOffset": 0x0b707a,
        "defValue": 2,
        "weakOffset": 0x0b707e,
        "resistOffset": 0x0b7080,
        "guardOffset": 0x0b7082,
        "absorbOffset": 0x0b7084
    }, {
        "id": 140,
        "name": "Shield",
        "nameOffset": 0x0b7098,
        "newNameReference": 0x800e09a4,
        "newNameText": 0x0f5dfc,
        "hpOffset": 0x0b709c,
        "hpValue": 120,
        "atkOffset": 0x0b709e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b70a0,
        "defOffset": 0x0b70a2,
        "defValue": 40,
        "weakOffset": 0x0b70a6,
        "resistOffset": 0x0b70a8,
        "guardOffset": 0x0b70aa,
        "absorbOffset": 0x0b70ac
    }, {
        "id": 141,
        "name": "Orobourous",
        "nameOffset": 0x0b70c0,
        "newNameReference": 0x800e0998,
        "newNameText": 0x0f5df0,
        "hpOffset": 0x0b70c4,
        "hpValue": 200,
        "atkOffset": 0x0b70c6,
        "atkValue": 47,
        "atkTypeOffset": 0x0b70c8,
        "defOffset": 0x0b70ca,
        "defValue": 4,
        "weakOffset": 0x0b70ce,
        "resistOffset": 0x0b70d0,
        "guardOffset": 0x0b70d2,
        "absorbOffset": 0x0b70d4
    }, {
        "id": 143,
        "name": "Oruburos rider",
        "nameOffset": 0x0b7110,
        "newNameReference": 0x800e098c,
        "newNameText": 0x0f5de4,
        "hpOffset": 0x0b7114,
        "hpValue": 100,
        "atkOffset": 0x0b7116,
        "atkValue": 31,
        "atkTypeOffset": 0x0b7118,
        "defOffset": 0x0b711a,
        "defValue": 1,
        "weakOffset": 0x0b711e,
        "resistOffset": 0x0b7120,
        "guardOffset": 0x0b7122,
        "absorbOffset": 0x0b7124
    }, {
        "id": 144,
        "name": "Dragon rider",
        "nameOffset": 0x0b7138,
        "newNameReference": 0x800e0980,
        "newNameText": 0x0f5dd8,
        "hpOffset": 0x0b713c,
        "hpValue": 120,
        "atkOffset": 0x0b713e,
        "atkValue": 41,
        "atkTypeOffset": 0x0b7140,
        "defOffset": 0x0b7142,
        "defValue": 4,
        "weakOffset": 0x0b7146,
        "resistOffset": 0x0b7148,
        "guardOffset": 0x0b714a,
        "absorbOffset": 0x0b714c
    }, {
        "id": 146,
        "name": "Dhuron",
        "nameOffset": 0x0b7188,
        "newNameReference": 0x800e0974,
        "newNameText": 0x0f5dcc,
        "hpOffset": 0x0b718c,
        "hpValue": 32,
        "atkOffset": 0x0b718e,
        "atkValue": 7,
        "atkTypeOffset": 0x0b7190,
        "defOffset": 0x0b7192,
        "defValue": 3,
        "weakOffset": 0x0b7196,
        "resistOffset": 0x0b7198,
        "guardOffset": 0x0b719a,
        "absorbOffset": 0x0b719c
    }, {
        "id": 148,
        "name": "Fire warg",
        "nameOffset": 0x0b7308,
        "newNameReference": 0x800e0968,
        "newNameText": 0x0f5dc0,
        "hpOffset": 0x0b730c,
        "hpValue": 200,
        "atkOffset": 0x0b730e,
        "atkValue": 41,
        "atkTypeOffset": 0x0b7310,
        "defOffset": 0x0b7312,
        "defValue": 1,
        "weakOffset": 0x0b7316,
        "resistOffset": 0x0b7318,
        "guardOffset": 0x0b731a,
        "absorbOffset": 0x0b731c
    }, {
        "id": 151,
        "name": "Warg rider",
        "nameOffset": 0x0b7380,
        "newNameReference": 0x800e095c,
        "newNameText": 0x0f5db4,
        "hpOffset": 0x0b7384,
        "hpValue": 120,
        "atkOffset": 0x0b7386,
        "atkValue": 36,
        "atkTypeOffset": 0x0b7388,
        "defOffset": 0x0b738a,
        "defValue": 3,
        "weakOffset": 0x0b738e,
        "resistOffset": 0x0b7390,
        "guardOffset": 0x0b7392,
        "absorbOffset": 0x0b7394
    }, {
        "id": 153,
        "name": "Cave troll",
        "nameOffset": 0x0b73d0,
        "newNameReference": 0x800e0950,
        "newNameText": 0x0f5da8,
        "hpOffset": 0x0b73d4,
        "hpValue": 88,
        "atkOffset": 0x0b73d6,
        "atkValue": 23,
        "atkTypeOffset": 0x0b73d8,
        "defOffset": 0x0b73da,
        "defValue": 5,
        "weakOffset": 0x0b73de,
        "resistOffset": 0x0b73e0,
        "guardOffset": 0x0b73e2,
        "absorbOffset": 0x0b73e4
    }, {
        "id": 156,
        "name": "Ghost",
        "nameOffset": 0x0b7448,
        "newNameReference": 0x800e0944,
        "newNameText": 0x0f5d9c,
        "hpOffset": 0x0b744c,
        "hpValue": 11,
        "atkOffset": 0x0b744e,
        "atkValue": 5,
        "atkTypeOffset": 0x0b7450,
        "defOffset": 0x0b7452,
        "defValue": 1,
        "weakOffset": 0x0b7456,
        "resistOffset": 0x0b7458,
        "guardOffset": 0x0b745a,
        "absorbOffset": 0x0b745c
    }, {
        "id": 157,
        "name": "Thornweed",
        "nameOffset": 0x0b7470,
        "newNameReference": 0x800e0938,
        "newNameText": 0x0f5d90,
        "hpOffset": 0x0b7474,
        "hpValue": 12,
        "atkOffset": 0x0b7476,
        "atkValue": 10,
        "atkTypeOffset": 0x0b7478,
        "defOffset": 0x0b747a,
        "defValue": 1,
        "weakOffset": 0x0b747e,
        "resistOffset": 0x0b7480,
        "guardOffset": 0x0b7482,
        "absorbOffset": 0x0b7484
    }, {
        "id": 158,
        "name": "Corpseweed",
        "nameOffset": 0x0b7498,
        "newNameReference": 0x800e092c,
        "newNameText": 0x0f5d84,
        "hpOffset": 0x0b749c,
        "hpValue": 18,
        "atkOffset": 0x0b749e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b74a0,
        "defOffset": 0x0b74a2,
        "defValue": 1,
        "weakOffset": 0x0b74a6,
        "resistOffset": 0x0b74a8,
        "guardOffset": 0x0b74aa,
        "absorbOffset": 0x0b74ac
    }, {
        "id": 159,
        "name": "Corpseweed",
        "nameOffset": 0x0b74c0,
        "newNameReference": 0x800e092c,
        "newNameText": 0x0f5d84,
        "hpOffset": 0x0b74c4,
        "hpValue": 20,
        "atkOffset": 0x0b74c6,
        "atkValue": 20,
        "atkTypeOffset": 0x0b74c8,
        "defOffset": 0x0b74ca,
        "defValue": 1,
        "weakOffset": 0x0b74ce,
        "resistOffset": 0x0b74d0,
        "guardOffset": 0x0b74d2,
        "absorbOffset": 0x0b74d4
    }, {
        "id": 161,
        "name": "Venus weed",
        "nameOffset": 0x0b7510,
        "newNameReference": 0x800e0cfb,
        "newNameText": 0x0f5d78,
        "hpOffset": 0x0b7514,
        "hpValue": 100,
        "atkOffset": 0x0b7516,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7518,
        "defOffset": 0x0b751a,
        "defValue": 1,
        "weakOffset": 0x0b751e,
        "resistOffset": 0x0b7520,
        "guardOffset": 0x0b7522,
        "absorbOffset": 0x0b7524
    }, {
        "id": 162,
        "name": "Venus weed",
        "nameOffset": 0x0b7538,
        "newNameReference": 0x800e0920,
        "newNameText": 0x0f5d78,
        "hpOffset": 0x0b753c,
        "hpValue": 500,
        "atkOffset": 0x0b753e,
        "atkValue": 28,
        "atkTypeOffset": 0x0b7540,
        "defOffset": 0x0b7542,
        "defValue": 1,
        "weakOffset": 0x0b7546,
        "resistOffset": 0x0b7548,
        "guardOffset": 0x0b754a,
        "absorbOffset": 0x0b754c
    }, {
        "id": 165,
        "name": "Bomb knight",
        "nameOffset": 0x0b75b0,
        "newNameReference": 0x800e0914,
        "newNameText": 0x0f5d6c,
        "hpOffset": 0x0b75b4,
        "hpValue": 46,
        "atkOffset": 0x0b75b6,
        "atkValue": 27,
        "atkTypeOffset": 0x0b75b8,
        "defOffset": 0x0b75ba,
        "defValue": 20,
        "weakOffset": 0x0b75be,
        "resistOffset": 0x0b75c0,
        "guardOffset": 0x0b75c2,
        "absorbOffset": 0x0b75c4
    }, {
        "id": 167,
        "name": "Rock knight",
        "nameOffset": 0x0b7600,
        "newNameReference": 0x800e0908,
        "newNameText": 0x0f5d60,
        "hpOffset": 0x0b7604,
        "hpValue": 160,
        "atkOffset": 0x0b7606,
        "atkValue": 50,
        "atkTypeOffset": 0x0b7608,
        "defOffset": 0x0b760a,
        "defValue": 20,
        "weakOffset": 0x0b760e,
        "resistOffset": 0x0b7610,
        "guardOffset": 0x0b7612,
        "absorbOffset": 0x0b7614
    }, {
        "id": 175,
        "name": "Warg",
        "nameOffset": 0x0b7740,
        "newNameReference": 0x800e08fc,
        "newNameText": 0x0f5d54,
        "hpOffset": 0x0b7744,
        "hpValue": 32,
        "atkOffset": 0x0b7746,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7748,
        "defOffset": 0x0b774a,
        "defValue": 1,
        "weakOffset": 0x0b774e,
        "resistOffset": 0x0b7750,
        "guardOffset": 0x0b7752,
        "absorbOffset": 0x0b7754
    }, {
        "id": 178,
        "name": "Slinger",
        "nameOffset": 0x0b77b8,
        "newNameReference": 0x800e08f0,
        "newNameText": 0x0f5d48,
        "hpOffset": 0x0b77bc,
        "hpValue": 12,
        "atkOffset": 0x0b77be,
        "atkValue": 5,
        "atkTypeOffset": 0x0b77c0,
        "defOffset": 0x0b77c2,
        "defValue": 1,
        "weakOffset": 0x0b77c6,
        "resistOffset": 0x0b77c8,
        "guardOffset": 0x0b77ca,
        "absorbOffset": 0x0b77cc
    }, {
        "id": 180,
        "name": "Corner guard",
        "nameOffset": 0x0b7808,
        "newNameReference": 0x800e08e4,
        "newNameText": 0x0f5d3c,
        "hpOffset": 0x0b780c,
        "hpValue": 48,
        "atkOffset": 0x0b780e,
        "atkValue": 13,
        "atkTypeOffset": 0x0b7810,
        "defOffset": 0x0b7812,
        "defValue": 3,
        "weakOffset": 0x0b7816,
        "resistOffset": 0x0b7818,
        "guardOffset": 0x0b781a,
        "absorbOffset": 0x0b781c
    }, {
        "id": 182,
        "name": "Bitterfly",
        "nameOffset": 0x0b7858,
        "newNameReference": 0x800e08d8,
        "newNameText": 0x0f5d30,
        "hpOffset": 0x0b785c,
        "hpValue": 4,
        "atkOffset": 0x0b785e,
        "atkValue": 55,
        "atkTypeOffset": 0x0b7860,
        "defOffset": 0x0b7862,
        "defValue": 1,
        "weakOffset": 0x0b7866,
        "resistOffset": 0x0b7868,
        "guardOffset": 0x0b786a,
        "absorbOffset": 0x0b786c
    }, {
        "id": 183,
        "name": "Bone pillar",
        "nameOffset": 0x0b7880,
        "newNameReference": 0x800e08cc,
        "newNameText": 0x0f5d24,
        "hpOffset": 0x0b7884,
        "hpValue": 64,
        "atkOffset": 0x0b7886,
        "atkValue": 12,
        "atkTypeOffset": 0x0b7888,
        "defOffset": 0x0b788a,
        "defValue": 2,
        "weakOffset": 0x0b788e,
        "resistOffset": 0x0b7890,
        "guardOffset": 0x0b7892,
        "absorbOffset": 0x0b7894
    }, {
        "id": 185,
        "name": "Spiked ball",
        "nameOffset": 0x0b78d0,
        "newNameReference": 0x800e08c0,
        "newNameText": 0x0f5d18,
        "hpOffset": 0x0b78d4,
        "hpValue": 500,
        "atkOffset": 0x0b78d6,
        "atkValue": 59,
        "atkTypeOffset": 0x0b78d8,
        "defOffset": 0x0b78da,
        "defValue": 28,
        "weakOffset": 0x0b78de,
        "resistOffset": 0x0b78e0,
        "guardOffset": 0x0b78e2,
        "absorbOffset": 0x0b78e4
    }, {
        "id": 186,
        "name": "Hammer",
        "nameOffset": 0x0b78f8,
        "newNameReference": 0x800e08b4,
        "newNameText": 0x0f5d0c,
        "hpOffset": 0x0b78fc,
        "hpValue": 250,
        "atkOffset": 0x0b78fe,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7900,
        "defOffset": 0x0b7902,
        "defValue": 1,
        "weakOffset": 0x0b7906,
        "resistOffset": 0x0b7908,
        "guardOffset": 0x0b790a,
        "absorbOffset": 0x0b790c
    }, {
        "id": 188,
        "name": "Gurkha",
        "nameOffset": 0x0b7948,
        "newNameReference": 0x800e08a8,
        "newNameText": 0x0f5d00,
        "hpOffset": 0x0b794c,
        "hpValue": 420,
        "atkOffset": 0x0b794e,
        "atkValue": 24,
        "atkTypeOffset": 0x0b7950,
        "defOffset": 0x0b7952,
        "defValue": 1,
        "weakOffset": 0x0b7956,
        "resistOffset": 0x0b7958,
        "guardOffset": 0x0b795a,
        "absorbOffset": 0x0b795c
    }, {
        "id": 190,
        "name": "Blade",
        "nameOffset": 0x0b7998,
        "newNameReference": 0x800e089c,
        "newNameText": 0x0f5cf4,
        "hpOffset": 0x0b799c,
        "hpValue": 380,
        "atkOffset": 0x0b799e,
        "atkValue": 24,
        "atkTypeOffset": 0x0b79a0,
        "defOffset": 0x0b79a2,
        "defValue": 1,
        "weakOffset": 0x0b79a6,
        "resistOffset": 0x0b79a8,
        "guardOffset": 0x0b79aa,
        "absorbOffset": 0x0b79ac
    }, {
        "id": 193,
        "name": "Ouija table",
        "nameOffset": 0x0b7a10,
        "newNameReference": 0x800e0890,
        "newNameText": 0x0f5ce8,
        "hpOffset": 0x0b7a14,
        "hpValue": 20,
        "atkOffset": 0x0b7a16,
        "atkValue": 4,
        "atkTypeOffset": 0x0b7a18,
        "defOffset": 0x0b7a1a,
        "defValue": 1,
        "weakOffset": 0x0b7a1e,
        "resistOffset": 0x0b7a20,
        "guardOffset": 0x0b7a22,
        "absorbOffset": 0x0b7a24
    }, {
        "id": 195,
        "name": "Sniper of goth",
        "nameOffset": 0x0b7a60,
        "newNameReference": 0x800e0884,
        "newNameText": 0x0f5cdc,
        "hpOffset": 0x0b7a64,
        "hpValue": 50,
        "atkOffset": 0x0b7a66,
        "atkValue": 40,
        "atkTypeOffset": 0x0b7a68,
        "defOffset": 0x0b7a6a,
        "defValue": 10,
        "weakOffset": 0x0b7a6e,
        "resistOffset": 0x0b7a70,
        "guardOffset": 0x0b7a72,
        "absorbOffset": 0x0b7a74
    }, {
        "id": 203,
        "name": "Minotaurus",
        "nameOffset": 0x0b7cd0,
        "newNameReference": 0x800e0878,
        "newNameText": 0x0f5cd0,
        "hpOffset": 0x0b7cd4,
        "hpValue": 300,
        "atkOffset": 0x0b7cd6,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7cd8,
        "defOffset": 0x0b7cda,
        "defValue": 3,
        "weakOffset": 0x0b7cde,
        "resistOffset": 0x0b7ce0,
        "guardOffset": 0x0b7ce2,
        "absorbOffset": 0x0b7ce4
    }, {
        "id": 206,
        "name": "Werewolf",
        "nameOffset": 0x0b7d48,
        "newNameReference": 0x800e086c,
        "newNameText": 0x0f5cc4,
        "hpOffset": 0x0b7d4c,
        "hpValue": 260,
        "atkOffset": 0x0b7d4e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7d50,
        "defOffset": 0x0b7d52,
        "defValue": 1,
        "weakOffset": 0x0b7d56,
        "resistOffset": 0x0b7d58,
        "guardOffset": 0x0b7d5a,
        "absorbOffset": 0x0b7d5c
    }, {
        "id": 211,
        "name": "Paranthropus",
        "nameOffset": 0x0b7e10,
        "newNameReference": 0x800e0860,
        "newNameText": 0x0f5cb8,
        "hpOffset": 0x0b7e14,
        "hpValue": 100,
        "atkOffset": 0x0b7e16,
        "atkValue": 24,
        "atkTypeOffset": 0x0b7e18,
        "defOffset": 0x0b7e1a,
        "defValue": 1,
        "weakOffset": 0x0b7e1e,
        "resistOffset": 0x0b7e20,
        "guardOffset": 0x0b7e22,
        "absorbOffset": 0x0b7e24
    }, {
        "id": 214,
        "name": "Mudman",
        "nameOffset": 0x0b7e88,
        "newNameReference": 0x800e0854,
        "newNameText": 0x0f5cac,
        "hpOffset": 0x0b7e8c,
        "hpValue": 15,
        "atkOffset": 0x0b7e8e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7e90,
        "defOffset": 0x0b7e92,
        "defValue": 1,
        "weakOffset": 0x0b7e96,
        "resistOffset": 0x0b7e98,
        "guardOffset": 0x0b7e9a,
        "absorbOffset": 0x0b7e9c
    }, {
        "id": 216,
        "name": "Ghost dancer",
        "nameOffset": 0x0b7ed8,
        "newNameReference": 0x800e0848,
        "newNameText": 0x0f5ca0,
        "hpOffset": 0x0b7edc,
        "hpValue": 30,
        "atkOffset": 0x0b7ede,
        "atkValue": 56,
        "atkTypeOffset": 0x0b7ee0,
        "defOffset": 0x0b7ee2,
        "defValue": 1,
        "weakOffset": 0x0b7ee6,
        "resistOffset": 0x0b7ee8,
        "guardOffset": 0x0b7eea,
        "absorbOffset": 0x0b7eec
    }, {
        "id": 217,
        "name": "Frozen half",
        "nameOffset": 0x0b7f00,
        "newNameReference": 0x800e083c,
        "newNameText": 0x0f5c94,
        "hpOffset": 0x0b7f04,
        "hpValue": 118,
        "atkOffset": 0x0b7f06,
        "atkValue": 35,
        "atkTypeOffset": 0x0b7f08,
        "defOffset": 0x0b7f0a,
        "defValue": 2,
        "weakOffset": 0x0b7f0e,
        "resistOffset": 0x0b7f10,
        "guardOffset": 0x0b7f12,
        "absorbOffset": 0x0b7f14
    }, {
        "id": 221,
        "name": "Salem witch",
        "nameOffset": 0x0b7fa0,
        "newNameReference": 0x800e0830,
        "newNameText": 0x0f5c88,
        "hpOffset": 0x0b7fa4,
        "hpValue": 180,
        "atkOffset": 0x0b7fa6,
        "atkValue": 20,
        "atkTypeOffset": 0x0b7fa8,
        "defOffset": 0x0b7faa,
        "defValue": 1,
        "weakOffset": 0x0b7fae,
        "resistOffset": 0x0b7fb0,
        "guardOffset": 0x0b7fb2,
        "absorbOffset": 0x0b7fb4
    }, {
        "id": 224,
        "name": "Azaghal",
        "nameOffset": 0x0b8018,
        "newNameReference": 0x800e0824,
        "newNameText": 0x0f5c7c,
        "hpOffset": 0x0b801c,
        "hpValue": 330,
        "atkOffset": 0x0b801e,
        "atkValue": 80,
        "atkTypeOffset": 0x0b8020,
        "defOffset": 0x0b8022,
        "defValue": 22,
        "weakOffset": 0x0b8026,
        "resistOffset": 0x0b8028,
        "guardOffset": 0x0b802a,
        "absorbOffset": 0x0b802c
    }, {
        "id": 225,
        "name": "Gremlin",
        "nameOffset": 0x0b8040,
        "newNameReference": 0x800e0818,
        "newNameText": 0x0f5c70,
        "hpOffset": 0x0b8044,
        "hpValue": 100,
        "atkOffset": 0x0b8046,
        "atkValue": 20,
        "atkTypeOffset": 0x0b8048,
        "defOffset": 0x0b804a,
        "defValue": 1,
        "weakOffset": 0x0b804e,
        "resistOffset": 0x0b8050,
        "guardOffset": 0x0b8052,
        "absorbOffset": 0x0b8054
    }, {
        "id": 227,
        "name": "Hunting girl",
        "nameOffset": 0x0b8090,
        "newNameReference": 0x800e080c,
        "newNameText": 0x0f5c64,
        "hpOffset": 0x0b8094,
        "hpValue": 88,
        "atkOffset": 0x0b8096,
        "atkValue": 18,
        "atkTypeOffset": 0x0b8098,
        "defOffset": 0x0b809a,
        "defValue": 1,
        "weakOffset": 0x0b809e,
        "resistOffset": 0x0b80a0,
        "guardOffset": 0x0b80a2,
        "absorbOffset": 0x0b80a4
    }, {
        "id": 228,
        "name": "Vandal sword",
        "nameOffset": 0x0b80b8,
        "newNameReference": 0x800e0800,
        "newNameText": 0x0f5c58,
        "hpOffset": 0x0b80bc,
        "hpValue": 120,
        "atkOffset": 0x0b80be,
        "atkValue": 30,
        "atkTypeOffset": 0x0b80c0,
        "defOffset": 0x0b80c2,
        "defValue": 3,
        "weakOffset": 0x0b80c6,
        "resistOffset": 0x0b80c8,
        "guardOffset": 0x0b80ca,
        "absorbOffset": 0x0b80cc
    }, {
        "id": 229,
        "name": "Salome",
        "nameOffset": 0x0b80e0,
        "newNameReference": 0x800e07f4,
        "newNameText": 0x0f5b1c,
        "hpOffset": 0x0b80e4,
        "hpValue": 210,
        "atkOffset": 0x0b80e6,
        "atkValue": 50,
        "atkTypeOffset": 0x0b80e8,
        "defOffset": 0x0b80ea,
        "defValue": 2,
        "weakOffset": 0x0b80ee,
        "resistOffset": 0x0b80f0,
        "guardOffset": 0x0b80f2,
        "absorbOffset": 0x0b80f4
    }, {
        "id": 233,
        "name": "Ctulhu",
        "nameOffset": 0x0b8180,
        "newNameReference": 0x800e07e8,
        "newNameText": 0x0f5b10,
        "hpOffset": 0x0b8184,
        "hpValue": 200,
        "atkOffset": 0x0b8186,
        "atkValue": 24,
        "atkTypeOffset": 0x0b8188,
        "defOffset": 0x0b818a,
        "defValue": 2,
        "weakOffset": 0x0b818e,
        "resistOffset": 0x0b8190,
        "guardOffset": 0x0b8192,
        "absorbOffset": 0x0b8194
    }, {
        "id": 236,
        "name": "Malachi",
        "nameOffset": 0x0b81f8,
        "newNameReference": 0x800e07dc,
        "newNameText": 0x0f5b04,
        "hpOffset": 0x0b81fc,
        "hpValue": 450,
        "atkOffset": 0x0b81fe,
        "atkValue": 52,
        "atkTypeOffset": 0x0b8200,
        "defOffset": 0x0b8202,
        "defValue": 20,
        "weakOffset": 0x0b8206,
        "resistOffset": 0x0b8208,
        "guardOffset": 0x0b820a,
        "absorbOffset": 0x0b820c
    }, {
        "id": 239,
        "name": "Harpy",
        "nameOffset": 0x0b8270,
        "newNameReference": 0x800e07d0,
        "newNameText": 0x0f5af8,
        "hpOffset": 0x0b8274,
        "hpValue": 26,
        "atkOffset": 0x0b8276,
        "atkValue": 18,
        "atkTypeOffset": 0x0b8278,
        "defOffset": 0x0b827a,
        "defValue": 1,
        "weakOffset": 0x0b827e,
        "resistOffset": 0x0b8280,
        "guardOffset": 0x0b8282,
        "absorbOffset": 0x0b8284
    }, {
        "id": 243,
        "name": "Slogra",
        "nameOffset": 0x0b8310,
        "newNameReference": 0x800e07c4,
        "newNameText": 0x0f5aec,
        "hpOffset": 0x0b8314,
        "hpValue": 200,
        "atkOffset": 0x0b8316,
        "atkValue": 6,
        "atkTypeOffset": 0x0b8318,
        "defOffset": 0x0b831a,
        "defValue": 1,
        "weakOffset": 0x0b831e,
        "resistOffset": 0x0b8320,
        "guardOffset": 0x0b8322,
        "absorbOffset": 0x0b8324
    }, {
        "id": 246,
        "name": "Axe knight",
        "nameOffset": 0x0b8388,
        "newNameReference": 0x800e07b8,
        "newNameText": 0x0f5ae0,
        "hpOffset": 0x0b838c,
        "hpValue": 32,
        "atkOffset": 0x0b838e,
        "atkValue": 6,
        "atkTypeOffset": 0x0b8390,
        "defOffset": 0x0b8392,
        "defValue": 3,
        "weakOffset": 0x0b8396,
        "resistOffset": 0x0b8398,
        "guardOffset": 0x0b839a,
        "absorbOffset": 0x0b839c
    }, {
        "id": 247,
        "name": "Spellbook",
        "nameOffset": 0x0b83b0,
        "newNameReference": 0x800e07ac,
        "newNameText": 0x0f5ad4,
        "hpOffset": 0x0b83b4,
        "hpValue": 26,
        "atkOffset": 0x0b83b6,
        "atkValue": 7,
        "atkTypeOffset": 0x0b83b8,
        "defOffset": 0x0b83ba,
        "defValue": 1,
        "weakOffset": 0x0b83be,
        "resistOffset": 0x0b83c0,
        "guardOffset": 0x0b83c2,
        "absorbOffset": 0x0b83c4
    }, {
        "id": 249,
        "name": "Magic tome",
        "nameOffset": 0x0b8400,
        "newNameReference": 0x800e0cfb,
        "newNameText": 0x0f5ac8,
        "hpOffset": 0x0b8404,
        "hpValue": 50,
        "atkOffset": 0x0b8406,
        "atkValue": 8,
        "atkTypeOffset": 0x0b8408,
        "defOffset": 0x0b840a,
        "defValue": 1,
        "weakOffset": 0x0b840e,
        "resistOffset": 0x0b8410,
        "guardOffset": 0x0b8412,
        "absorbOffset": 0x0b8414
    }, {
        "id": 251,
        "name": "Magic tome",
        "nameOffset": 0x0b8580,
        "newNameReference": 0x800e07a0,
        "newNameText": 0x0f5ac8,
        "hpOffset": 0x0b8584,
        "hpValue": 22,
        "atkOffset": 0x0b8586,
        "atkValue": 12,
        "atkTypeOffset": 0x0b8588,
        "defOffset": 0x0b858a,
        "defValue": 2,
        "weakOffset": 0x0b858e,
        "resistOffset": 0x0b8590,
        "guardOffset": 0x0b8592,
        "absorbOffset": 0x0b8594
    }, {
        "id": 253,
        "name": "Doppleganger10",
        "nameOffset": 0x0b85d0,
        "newNameReference": 0x800e0794,
        "newNameText": 0x0f5abc,
        "hpOffset": 0x0b85d4,
        "hpValue": 120,
        "atkOffset": 0x0b85d6,
        "atkValue": 7,
        "atkTypeOffset": 0x0b85d8,
        "defOffset": 0x0b85da,
        "defValue": 5,
        "weakOffset": 0x0b85de,
        "resistOffset": 0x0b85e0,
        "guardOffset": 0x0b85e2,
        "absorbOffset": 0x0b85e4
    }, {
        "id": 254,
        "name": "Gaibon",
        "nameOffset": 0x0b85f8,
        "newNameReference": 0x800e0788,
        "newNameText": 0x0f5ab0,
        "hpOffset": 0x0b85fc,
        "hpValue": 200,
        "atkOffset": 0x0b85fe,
        "atkValue": 7,
        "atkTypeOffset": 0x0b8600,
        "defOffset": 0x0b8602,
        "defValue": 1,
        "weakOffset": 0x0b8606,
        "resistOffset": 0x0b8608,
        "guardOffset": 0x0b860a,
        "absorbOffset": 0x0b860c
    }, {
        "id": 261,
        "name": "Skull lord",
        "nameOffset": 0x0b8710,
        "newNameReference": 0x800e077c,
        "newNameText": 0x0f5aa4,
        "hpOffset": 0x0b8714,
        "hpValue": 80,
        "atkOffset": 0x0b8716,
        "atkValue": 25,
        "atkTypeOffset": 0x0b8718,
        "defOffset": 0x0b871a,
        "defValue": 4,
        "weakOffset": 0x0b871e,
        "resistOffset": 0x0b8720,
        "guardOffset": 0x0b8722,
        "absorbOffset": 0x0b8724
    }, {
        "id": 262,
        "name": "Lion",
        "nameOffset": 0x0b8738,
        "newNameReference": 0x800e0770,
        "newNameText": 0x0f5a98,
        "hpOffset": 0x0b873c,
        "hpValue": 150,
        "atkOffset": 0x0b873e,
        "atkValue": 37,
        "atkTypeOffset": 0x0b8740,
        "defOffset": 0x0b8742,
        "defValue": 25,
        "weakOffset": 0x0b8746,
        "resistOffset": 0x0b8748,
        "guardOffset": 0x0b874a,
        "absorbOffset": 0x0b874c
    }, {
        "id": 264,
        "name": "Tin man",
        "nameOffset": 0x0b8788,
        "newNameReference": 0x800e0764,
        "newNameText": 0x0f5a8c,
        "hpOffset": 0x0b878c,
        "hpValue": 48,
        "atkOffset": 0x0b878e,
        "atkValue": 32,
        "atkTypeOffset": 0x0b8790,
        "defOffset": 0x0b8792,
        "defValue": 36,
        "weakOffset": 0x0b8796,
        "resistOffset": 0x0b8798,
        "guardOffset": 0x0b879a,
        "absorbOffset": 0x0b879c
    }, {
        "id": 267,
        "name": "Akmodan ii",
        "nameOffset": 0x0b8800,
        "newNameReference": 0x800e0758,
        "newNameText": 0x0f5a80,
        "hpOffset": 0x0b8804,
        "hpValue": 1200,
        "atkOffset": 0x0b8806,
        "atkValue": 40,
        "atkTypeOffset": 0x0b8808,
        "defOffset": 0x0b880a,
        "defValue": 1,
        "weakOffset": 0x0b880e,
        "resistOffset": 0x0b8810,
        "guardOffset": 0x0b8812,
        "absorbOffset": 0x0b8814
    }, {
        "id": 271,
        "name": "Cloaked knight",
        "nameOffset": 0x0b88a0,
        "newNameReference": 0x800e074c,
        "newNameText": 0x0f5a74,
        "hpOffset": 0x0b88a4,
        "hpValue": 65,
        "atkOffset": 0x0b88a6,
        "atkValue": 20,
        "atkTypeOffset": 0x0b88a8,
        "defOffset": 0x0b88aa,
        "defValue": 3,
        "weakOffset": 0x0b88ae,
        "resistOffset": 0x0b88b0,
        "guardOffset": 0x0b88b2,
        "absorbOffset": 0x0b88b4
    }, {
        "id": 273,
        "name": "Darkwing bat",
        "nameOffset": 0x0b88f0,
        "newNameReference": 0x800e0740,
        "newNameText": 0x0f5a68,
        "hpOffset": 0x0b88f4,
        "hpValue": 600,
        "atkOffset": 0x0b88f6,
        "atkValue": 35,
        "atkTypeOffset": 0x0b88f8,
        "defOffset": 0x0b88fa,
        "defValue": 1,
        "weakOffset": 0x0b88fe,
        "resistOffset": 0x0b8900,
        "guardOffset": 0x0b8902,
        "absorbOffset": 0x0b8904
    }, {
        "id": 277,
        "name": "Fishhead",
        "nameOffset": 0x0b8990,
        "newNameReference": 0x800e0734,
        "newNameText": 0x0f5a5c,
        "hpOffset": 0x0b8994,
        "hpValue": 70,
        "atkOffset": 0x0b8996,
        "atkValue": 15,
        "atkTypeOffset": 0x0b8998,
        "defOffset": 0x0b899a,
        "defValue": 2,
        "weakOffset": 0x0b899e,
        "resistOffset": 0x0b89a0,
        "guardOffset": 0x0b89a2,
        "absorbOffset": 0x0b89a4
    }, {
        "id": 280,
        "name": "Karasuman",
        "nameOffset": 0x0b8a08,
        "newNameReference": 0x800e0728,
        "newNameText": 0x0f5a50,
        "hpOffset": 0x0b8a0c,
        "hpValue": 500,
        "atkOffset": 0x0b8a0e,
        "atkValue": 20,
        "atkTypeOffset": 0x0b8a10,
        "defOffset": 0x0b8a12,
        "defValue": 10,
        "weakOffset": 0x0b8a16,
        "resistOffset": 0x0b8a18,
        "guardOffset": 0x0b8a1a,
        "absorbOffset": 0x0b8a1c
    }, {
        "id": 284,
        "name": "Imp",
        "nameOffset": 0x0b8aa8,
        "newNameReference": 0x800e071c,
        "newNameText": 0x0f5a44,
        "hpOffset": 0x0b8aac,
        "hpValue": 43,
        "atkOffset": 0x0b8aae,
        "atkValue": 10,
        "atkTypeOffset": 0x0b8ab0,
        "defOffset": 0x0b8ab2,
        "defValue": 1,
        "weakOffset": 0x0b8ab6,
        "resistOffset": 0x0b8ab8,
        "guardOffset": 0x0b8aba,
        "absorbOffset": 0x0b8abc
    }, {
        "id": 285,
        "name": "Balloon pod",
        "nameOffset": 0x0b8ad0,
        "newNameReference": 0x800e0710,
        "newNameText": 0x0f5a38,
        "hpOffset": 0x0b8ad4,
        "hpValue": 3,
        "atkOffset": 0x0b8ad6,
        "atkValue": 55,
        "atkTypeOffset": 0x0b8ad8,
        "defOffset": 0x0b8ada,
        "defValue": 1,
        "weakOffset": 0x0b8ade,
        "resistOffset": 0x0b8ae0,
        "guardOffset": 0x0b8ae2,
        "absorbOffset": 0x0b8ae4
    }, {
        "id": 287,
        "name": "Scylla",
        "nameOffset": 0x0b8b20,
        "newNameReference": 0x800e0704,
        "newNameText": 0x0f5a2c,
        "hpOffset": 0x0b8b24,
        "hpValue": 200,
        "atkOffset": 0x0b8b26,
        "atkValue": 16,
        "atkTypeOffset": 0x0b8b28,
        "defOffset": 0x0b8b2a,
        "defValue": 1,
        "weakOffset": 0x0b8b2e,
        "resistOffset": 0x0b8b30,
        "guardOffset": 0x0b8b32,
        "absorbOffset": 0x0b8b34
    }, {
        "id": 294,
        "name": "Scylla wyrm",
        "nameOffset": 0x0b8c38,
        "newNameReference": 0x800e06f8,
        "newNameText": 0x0f5a20,
        "hpOffset": 0x0b8c3c,
        "hpValue": 130,
        "atkOffset": 0x0b8c3e,
        "atkValue": 14,
        "atkTypeOffset": 0x0b8c40,
        "defOffset": 0x0b8c42,
        "defValue": 3,
        "weakOffset": 0x0b8c46,
        "resistOffset": 0x0b8c48,
        "guardOffset": 0x0b8c4a,
        "absorbOffset": 0x0b8c4c
    }, {
        "id": 295,
        "name": "Granfaloon",
        "nameOffset": 0x0b8c60,
        "newNameReference": 0x800e0cfb,
        "newNameText": 0x0f5a14,
        "hpOffset": 0x0b8c64,
        "hpValue": 400,
        "atkOffset": 0x0b8c66,
        "atkValue": 30,
        "atkTypeOffset": 0x0b8c68,
        "defOffset": 0x0b8c6a,
        "defValue": 10,
        "weakOffset": 0x0b8c6e,
        "resistOffset": 0x0b8c70,
        "guardOffset": 0x0b8c72,
        "absorbOffset": 0x0b8c74
    }, {
        "id": 296,
        "name": "Granfaloon",
        "nameOffset": 0x0b8c88,
        "newNameReference": 0x800e06ec,
        "newNameText": 0x0f5a14,
        "hpOffset": 0x0b8c8c,
        "hpValue": 400,
        "atkOffset": 0x0b8c8e,
        "atkValue": 28,
        "atkTypeOffset": 0x0b8c90,
        "defOffset": 0x0b8c92,
        "defValue": 1,
        "weakOffset": 0x0b8c96,
        "resistOffset": 0x0b8c98,
        "guardOffset": 0x0b8c9a,
        "absorbOffset": 0x0b8c9c
    }, {
        "id": 300,
        "name": "Hippogryph",
        "nameOffset": 0x0b8d28,
        "newNameReference": 0x800e06e0,
        "newNameText": 0x0f5a08,
        "hpOffset": 0x0b8d2c,
        "hpValue": 800,
        "atkOffset": 0x0b8d2e,
        "atkValue": 18,
        "atkTypeOffset": 0x0b8d30,
        "defOffset": 0x0b8d32,
        "defValue": 1,
        "weakOffset": 0x0b8d36,
        "resistOffset": 0x0b8d38,
        "guardOffset": 0x0b8d3a,
        "absorbOffset": 0x0b8d3c
    }, {
        "id": 303,
        "name": "Medusa head",
        "nameOffset": 0x0b8ed0,
        "newNameReference": 0x800e06d4,
        "newNameText": 0x0f59fc,
        "hpOffset": 0x0b8ed4,
        "hpValue": 12,
        "atkOffset": 0x0b8ed6,
        "atkValue": 12,
        "atkTypeOffset": 0x0b8ed8,
        "defOffset": 0x0b8eda,
        "defValue": 1,
        "weakOffset": 0x0b8ede,
        "resistOffset": 0x0b8ee0,
        "guardOffset": 0x0b8ee2,
        "absorbOffset": 0x0b8ee4
    }, {
        "id": 304,
        "name": "Medusa head",
        "nameOffset": 0x0b8ef8,
        "newNameReference": 0x800e0cd4,
        "newNameText": 0xf612c,
        "hpOffset": 0x0b8efc,
        "hpValue": 12,
        "atkOffset": 0x0b8efe,
        "atkValue": 7,
        "atkTypeOffset": 0x0b8f00,
        "defOffset": 0x0b8f02,
        "defValue": 1,
        "weakOffset": 0x0b8f06,
        "resistOffset": 0x0b8f08,
        "guardOffset": 0x0b8f0a,
        "absorbOffset": 0x0b8f0c
    }, {
        "id": 305,
        "name": "Archer",
        "nameOffset": 0x0b8f20,
        "newNameReference": 0x800e06c8,
        "newNameText": 0x0f59f0,
        "hpOffset": 0x0b8f24,
        "hpValue": 300,
        "atkOffset": 0x0b8f26,
        "atkValue": 40,
        "atkTypeOffset": 0x0b8f28,
        "defOffset": 0x0b8f2a,
        "defValue": 8,
        "weakOffset": 0x0b8f2e,
        "resistOffset": 0x0b8f30,
        "guardOffset": 0x0b8f32,
        "absorbOffset": 0x0b8f34
    }, {
        "id": 307,
        "name": "Richter belmont",
        "nameOffset": 0x0b8f70,
        "newNameReference": 0x800e06bc,
        "newNameText": 0x0f59e4,
        "hpOffset": 0x0b8f74,
        "hpValue": 400,
        "atkOffset": 0x0b8f76,
        "atkValue": 25,
        "atkTypeOffset": 0x0b8f78,
        "defOffset": 0x0b8f7a,
        "defValue": 10,
        "weakOffset": 0x0b8f7e,
        "resistOffset": 0x0b8f80,
        "guardOffset": 0x0b8f82,
        "absorbOffset": 0x0b8f84
    }, {
        "id": 322,
        "name": "Scarecrow",
        "nameOffset": 0x0b91c8,
        "newNameReference": 0x800e06b0,
        "newNameText": 0x0f59d8,
        "hpOffset": 0x0b91cc,
        "hpValue": 120,
        "atkOffset": 0x0b91ce,
        "atkValue": 40,
        "atkTypeOffset": 0x0b91d0,
        "defOffset": 0x0b91d2,
        "defValue": 6,
        "weakOffset": 0x0b91d6,
        "resistOffset": 0x0b91d8,
        "guardOffset": 0x0b91da,
        "absorbOffset": 0x0b91dc
    }, {
        "id": 323,
        "name": "Schmoo",
        "nameOffset": 0x0b91f0,
        "newNameReference": 0x800e06a4,
        "newNameText": 0x0f59cc,
        "hpOffset": 0x0b91f4,
        "hpValue": 50,
        "atkOffset": 0x0b91f6,
        "atkValue": 40,
        "atkTypeOffset": 0x0b91f8,
        "defOffset": 0x0b91fa,
        "defValue": 1,
        "weakOffset": 0x0b91fe,
        "resistOffset": 0x0b9200,
        "guardOffset": 0x0b9202,
        "absorbOffset": 0x0b9204
    }, {
        "id": 324,
        "name": "Beezelbub",
        "nameOffset": 0x0b9218,
        "newNameReference": 0x800e0698,
        "newNameText": 0x0f59c0,
        "hpOffset": 0x0b921c,
        "hpValue": 2000,
        "atkOffset": 0x0b921e,
        "atkValue": 60,
        "atkTypeOffset": 0x0b9220,
        "defOffset": 0x0b9222,
        "defValue": 13,
        "weakOffset": 0x0b9226,
        "resistOffset": 0x0b9228,
        "guardOffset": 0x0b922a,
        "absorbOffset": 0x0b922c
    }, {
        "id": 328,
        "name": "Fake trevor",
        "nameOffset": 0x0b92b8,
        "newNameReference": 0x800e068c,
        "newNameText": 0x0f59b4,
        "hpOffset": 0x0b92bc,
        "hpValue": 1200,
        "atkOffset": 0x0b92be,
        "atkValue": 38,
        "atkTypeOffset": 0x0b92c0,
        "defOffset": 0x0b92c2,
        "defValue": 8,
        "weakOffset": 0x0b92c6,
        "resistOffset": 0x0b92c8,
        "guardOffset": 0x0b92ca,
        "absorbOffset": 0x0b92cc
    }, {
        "id": 334,
        "name": "Fake grant",
        "nameOffset": 0x0b93a8,
        "newNameReference": 0x800e0680,
        "newNameText": 0x0f59a8,
        "hpOffset": 0x0b93ac,
        "hpValue": 800,
        "atkOffset": 0x0b93ae,
        "atkValue": 38,
        "atkTypeOffset": 0x0b93b0,
        "defOffset": 0x0b93b2,
        "defValue": 4,
        "weakOffset": 0x0b93b6,
        "resistOffset": 0x0b93b8,
        "guardOffset": 0x0b93ba,
        "absorbOffset": 0x0b93bc
    }, {
        "id": 337,
        "name": "Fake sypha",
        "nameOffset": 0x0b9420,
        "newNameReference": 0x800e0674,
        "newNameText": 0x0f599c,
        "hpOffset": 0x0b9424,
        "hpValue": 1000,
        "atkOffset": 0x0b9426,
        "atkValue": 9,
        "atkTypeOffset": 0x0b9428,
        "defOffset": 0x0b942a,
        "defValue": 2,
        "weakOffset": 0x0b942e,
        "resistOffset": 0x0b9430,
        "guardOffset": 0x0b9432,
        "absorbOffset": 0x0b9434
    }, {
        "id": 342,
        "name": "Succubus",
        "nameOffset": 0x0b94e8,
        "newNameReference": 0x800e0668,
        "newNameText": 0x0f5990,
        "hpOffset": 0x0b94ec,
        "hpValue": 666,
        "atkOffset": 0x0b94ee,
        "atkValue": 25,
        "atkTypeOffset": 0x0b94f0,
        "defOffset": 0x0b94f2,
        "defValue": 1,
        "weakOffset": 0x0b94f6,
        "resistOffset": 0x0b94f8,
        "guardOffset": 0x0b94fa,
        "absorbOffset": 0x0b94fc
    }, {
        "id": 350,
        "name": "Killer fish",
        "nameOffset": 0x0b9628,
        "newNameReference": 0x800e065c,
        "newNameText": 0x0f5984,
        "hpOffset": 0x0b962c,
        "hpValue": 120,
        "atkOffset": 0x0b962e,
        "atkValue": 50,
        "atkTypeOffset": 0x0b9630,
        "defOffset": 0x0b9632,
        "defValue": 4,
        "weakOffset": 0x0b9636,
        "resistOffset": 0x0b9638,
        "guardOffset": 0x0b963a,
        "absorbOffset": 0x0b963c
    }, {
        "id": 351,
        "name": "Shaft",
        "nameOffset": 0x0b9650,
        "newNameReference": 0x800e0650,
        "newNameText": 0x0f5978,
        "hpOffset": 0x0b9654,
        "hpValue": 1300,
        "atkOffset": 0x0b9656,
        "atkValue": 40,
        "atkTypeOffset": 0x0b9658,
        "defOffset": 0x0b965a,
        "defValue": 30,
        "weakOffset": 0x0b965e,
        "resistOffset": 0x0b9660,
        "guardOffset": 0x0b9662,
        "absorbOffset": 0x0b9664
    }, {
        "id": 356,
        "name": "Death",
        "nameOffset": 0x0b9848,
        "newNameReference": 0x800e0644,
        "newNameText": 0x0f596c,
        "hpOffset": 0x0b984c,
        "hpValue": 888,
        "atkOffset": 0x0b984e,
        "atkValue": 35,
        "atkTypeOffset": 0x0b9850,
        "defOffset": 0x0b9852,
        "defValue": 17,
        "weakOffset": 0x0b9856,
        "resistOffset": 0x0b9858,
        "guardOffset": 0x0b985a,
        "absorbOffset": 0x0b985c
    }, {
        "id": 361,
        "name": "Death",
        "nameOffset": 0x0b9910,
        "newNameReference": 0x800e0cfb,
        "newNameText": 0x0f596c,
        "hpOffset": 0x0b9914,
        "hpValue": 1200,
        "atkOffset": 0x0b9916,
        "atkValue": 40,
        "atkTypeOffset": 0x0b9918,
        "defOffset": 0x0b991a,
        "defValue": 14,
        "weakOffset": 0x0b991e,
        "resistOffset": 0x0b9920,
        "guardOffset": 0x0b9922,
        "absorbOffset": 0x0b9924
    }, {
        "id": 363,
        "name": "Cerberos",
        "nameOffset": 0x0b9960,
        "newNameReference": 0x800e0638,
        "newNameText": 0x0f5960,
        "hpOffset": 0x0b9964,
        "hpValue": 800,
        "atkOffset": 0x0b9966,
        "atkValue": 20,
        "atkTypeOffset": 0x0b9968,
        "defOffset": 0x0b996a,
        "defValue": 1,
        "weakOffset": 0x0b996e,
        "resistOffset": 0x0b9970,
        "guardOffset": 0x0b9972,
        "absorbOffset": 0x0b9974
    }, {
        "id": 366,
        "name": "Medusa",
        "nameOffset": 0x0b99d8,
        "newNameReference": 0x800e062c,
        "newNameText": 0x0f5954,
        "hpOffset": 0x0b99dc,
        "hpValue": 1100,
        "atkOffset": 0x0b99de,
        "atkValue": 35,
        "atkTypeOffset": 0x0b99e0,
        "defOffset": 0x0b99e2,
        "defValue": 8,
        "weakOffset": 0x0b99e6,
        "resistOffset": 0x0b99e8,
        "guardOffset": 0x0b99ea,
        "absorbOffset": 0x0b99ec
    }, {
        "id": 370,
        "name": "The creature",
        "nameOffset": 0x0b9a78,
        "newNameReference": 0x800e0620,
        "newNameText": 0x0f5948,
        "hpOffset": 0x0b9a7c,
        "hpValue": 1100,
        "atkOffset": 0x0b9a7e,
        "atkValue": 30,
        "atkTypeOffset": 0x0b9a80,
        "defOffset": 0x0b9a82,
        "defValue": 15,
        "weakOffset": 0x0b9a86,
        "resistOffset": 0x0b9a88,
        "guardOffset": 0x0b9a8a,
        "absorbOffset": 0x0b9a8c
    }, {
        "id": 372,
        "name": "Doppleganger40",
        "nameOffset": 0x0b9ac8,
        "newNameReference": 0x800e0614,
        "newNameText": 0x0f593c,
        "hpOffset": 0x0b9acc,
        "hpValue": 777,
        "atkOffset": 0x0b9ace,
        "atkValue": 35,
        "atkTypeOffset": 0x0b9ad0,
        "defOffset": 0x0b9ad2,
        "defValue": 16,
        "weakOffset": 0x0b9ad6,
        "resistOffset": 0x0b9ad8,
        "guardOffset": 0x0b9ada,
        "absorbOffset": 0x0b9adc
    }, {
        "id": 379,
        "name": "Dracula",
        "nameOffset": 0x0b9be0,
        "newNameReference": 0x800e0ce1,
        "newNameText": 0x0f5930,
        "hpOffset": 0x0b9be4,
        "hpValue": 10000,
        "atkOffset": 0x0b9be6,
        "atkValue": 39,
        "atkTypeOffset": 0x0b9be8,
        "defOffset": 0x0b9bea,
        "defValue": 18,
        "weakOffset": 0x0b9bee,
        "resistOffset": 0x0b9bf0,
        "guardOffset": 0x0b9bf2,
        "absorbOffset": 0x0b9bf4
    }, {
        "id": 386,
        "name": "Minotaur",
        "nameOffset": 0x0b9cf8,
        "newNameReference": 0x800e05fc,
        "newNameText": 0x0f5924,
        "hpOffset": 0x0b9cfc,
        "hpValue": 320,
        "atkOffset": 0x0b9cfe,
        "atkValue": 45,
        "atkTypeOffset": 0x0b9d00,
        "defOffset": 0x0b9d02,
        "defValue": 4,
        "weakOffset": 0x0b9d06,
        "resistOffset": 0x0b9d08,
        "guardOffset": 0x0b9d0a,
        "absorbOffset": 0x0b9d0c
    }, {
        "id": 389,
        "name": "Werewolf",
        "nameOffset": 0x0b9d70,
        "newNameReference": 0x800e05f0,
        "newNameText": 0x0f5918,
        "hpOffset": 0x0b9d74,
        "hpValue": 280,
        "atkOffset": 0x0b9d76,
        "atkValue": 40,
        "atkTypeOffset": 0x0b9d78,
        "defOffset": 0x0b9d7a,
        "defValue": 1,
        "weakOffset": 0x0b9d7e,
        "resistOffset": 0x0b9d80,
        "guardOffset": 0x0b9d82,
        "absorbOffset": 0x0b9d84
    }, {
        "id": 392,
        "name": "Blue venus weed",
        "nameOffset": 0x0b9de8,
        "newNameReference": 0x800e0cfb,
        "newNameText": 0x0f590c,
        "hpOffset": 0x0b9dec,
        "hpValue": 100,
        "atkOffset": 0x0b9dee,
        "atkValue": 35,
        "atkTypeOffset": 0x0b9df0,
        "defOffset": 0x0b9df2,
        "defValue": 1,
        "weakOffset": 0x0b9df6,
        "resistOffset": 0x0b9df8,
        "guardOffset": 0x0b9dfa,
        "absorbOffset": 0x0b9dfc
    }, {
        "id": 393,
        "name": "Blue venus weed",
        "nameOffset": 0x0b9e10,
        "newNameReference": 0x800e05e4,
        "newNameText": 0x0f590c,
        "hpOffset": 0x0b9e14,
        "hpValue": 550,
        "atkOffset": 0x0b9e16,
        "atkValue": 45,
        "atkTypeOffset": 0x0b9e18,
        "defOffset": 0x0b9e1a,
        "defValue": 1,
        "weakOffset": 0x0b9e1e,
        "resistOffset": 0x0b9e20,
        "guardOffset": 0x0b9e22,
        "absorbOffset": 0x0b9e24
    },
]

enemy_atk_type_list = [
    0x0000,  # No hitbox
    0x0000,  # No hitbox
    0x0000,  # No hitbox
    0x0006,  # guard
    0x0006,  # guard
    0x0006,  # guard
    0x0021,  # Normal Hit
    0x0021,  # Normal Hit
    0x0021,  # Normal Hit
    0x0121,  # Hit Curse
    0x0221,  # Hit Stone
    0x0321,  # Hit Stone Curse
    0x0421,  # Hit Water
    0x0421,  # Hit Water
    0x0421,  # Hit Water
    0x0521,  # Hit Water Curse
    0x0621,  # Hit Water Stone
    0x0821,  # Hit Dark
    0x0821,  # Hit Dark
    0x0821,  # Hit Dark
    0x0921,  # Hit Dark Curse
    0x0a21,  # Hit Dark Stone
    0x0c21,  # Hit Dark Water
    0x0c21,  # Hit Dark Water
    0x0c21,  # Hit Dark Water
    0x1021,  # Hit Holy
    0x1021,  # Hit Holy
    0x1021,  # Hit Holy
    0x1021,  # Hit Holy
    0x1021,  # Hit Holy
    0x1121,  # Hit Holy Curse
    0x1221,  # Hit Holy Stone
    0x1421,  # Hit Holy Water
    0x1421,  # Hit Holy Water
    0x1421,  # Hit Holy Water
    0x1821,  # Hit Holy Dark
    0x1821,  # Hit Holy Dark
    0x1821,  # Hit Holy Dark
    0x2021,  # Hit Ice
    0x2021,  # Hit Ice
    0x2021,  # Hit Ice
    0x2121,  # Hit Ice Curse
    0x2221,  # Hit Ice Stone
    0x2421,  # Hit Ice Water
    0x2821,  # Hit Ice Dark
    0x2821,  # Hit Ice Dark
    0x2821,  # Hit Ice Dark
    0x3021,  # Hit Holy Ice
    0x3021,  # Hit Holy Ice
    0x3021,  # Hit Holy Ice
    0x4021,  # Hit Lightning
    0x4021,  # Hit Lightning
    0x4021,  # Hit Lightning
    0x4121,  # Hit Lightning Curse
    0x4221,  # Hit Lightning Stone
    0x4421,  # Hit Lightning Water
    0x4421,  # Hit Lightning Water
    0x4421,  # Hit Lightning Water
    0x4821,  # Hit Lightning Dark
    0x4821,  # Hit Lightning Dark
    0x4821,  # Hit Lightning Dark
    0x5021,  # Hit Holy Lightning
    0x5021,  # Hit Holy Lightning
    0x5021,  # Hit Holy Lightning
    0x6021,  # Hit Ice Lightning
    0x6021,  # Hit Ice Lightning
    0x6021,  # Hit Ice Lightning
    0x8021,  # Hit Fire
    0x8021,  # Hit Fire
    0x8021,  # Hit Fire
    0x8121,  # Hit Fire Curse
    0x8221,  # Hit Fire Stone
    0x8421,  # Hit Fire Water
    0x8421,  # Hit Fire Water
    0x8421,  # Hit Fire Water
    0x8821,  # Hit Fire Dark
    0x8821,  # Hit Fire Dark
    0x8821,  # Hit Fire Dark
    0x9021,  # Hit Holy Fire
    0x9021,  # Hit Holy Fire
    0x9021,  # Hit Holy Fire
    0xA021,  # Hit Ice Fire
    0xA021,  # Hit Ice Fire
    0xA021,  # Hit Ice Fire
    0xC021,  # Hit Lightning Fire
    0xC021,  # Hit Lightning Fire
    0xC021,  # Hit Lightning Fire
    0x0124,  # Hit Curse
    0x0224,  # Hit Stone
    0x0324,  # Hit Stone Curse
    0x0424,  # Hit Water
    0x0424,  # Hit Water
    0x0424,  # Hit Water
    0x0524,  # Hit Water Curse
    0x0624,  # Hit Water Stone
    0x0824,  # Hit Dark
    0x0824,  # Hit Dark
    0x0824,  # Hit Dark
    0x0924,  # Hit Dark Curse
    0x0a24,  # Hit Dark Stone
    0x0c24,  # Hit Dark Water
    0x0c24,  # Hit Dark Water
    0x0c24,  # Hit Dark Water
    0x1024,  # Hit Holy
    0x1024,  # Hit Holy
    0x1024,  # Hit Holy
    0x1024,  # Hit Holy
    0x1024,  # Hit Holy
    0x1124,  # Hit Holy Curse
    0x1224,  # Hit Holy Stone
    0x1424,  # Hit Holy Water
    0x1424,  # Hit Holy Water
    0x1424,  # Hit Holy Water
    0x1824,  # Hit Holy Dark
    0x1824,  # Hit Holy Dark
    0x1824,  # Hit Holy Dark
    0x2024,  # Hit Ice
    0x2024,  # Hit Ice
    0x2024,  # Hit Ice
    0x2124,  # Hit Ice Curse
    0x2224,  # Hit Ice Stone
    0x2424,  # Hit Ice Water
    0x2824,  # Hit Ice Dark
    0x2824,  # Hit Ice Dark
    0x2824,  # Hit Ice Dark
    0x3024,  # Hit Holy Ice
    0x3024,  # Hit Holy Ice
    0x3024,  # Hit Holy Ice
    0x4024,  # Hit Lightning
    0x4024,  # Hit Lightning
    0x4024,  # Hit Lightning
    0x4124,  # Hit Lightning Curse
    0x4224,  # Hit Lightning Stone
    0x4424,  # Hit Lightning Water
    0x4424,  # Hit Lightning Water
    0x4424,  # Hit Lightning Water
    0x4824,  # Hit Lightning Dark
    0x4824,  # Hit Lightning Dark
    0x4824,  # Hit Lightning Dark
    0x5024,  # Hit Holy Lightning
    0x5024,  # Hit Holy Lightning
    0x5024,  # Hit Holy Lightning
    0x6024,  # Hit Ice Lightning
    0x6024,  # Hit Ice Lightning
    0x6024,  # Hit Ice Lightning
    0x8024,  # Hit Fire
    0x8024,  # Hit Fire
    0x8024,  # Hit Fire
    0x8124,  # Hit Fire Curse
    0x8224,  # Hit Fire Stone
    0x8424,  # Hit Fire Water
    0x8424,  # Hit Fire Water
    0x8424,  # Hit Fire Water
    0x8824,  # Hit Fire Dark
    0x8824,  # Hit Fire Dark
    0x8824,  # Hit Fire Dark
    0x9024,  # Hit Holy Fire
    0x9024,  # Hit Holy Fire
    0x9024,  # Hit Holy Fire
    0xA024,  # Hit Ice Fire
    0xA024,  # Hit Ice Fire
    0xA024,  # Hit Ice Fire
    0xC024,  # Hit Lightning Fire
    0xC024,  # Hit Lightning Fire
    0xC024,  # Hit Lightning Fire
    0x0041,  # Normal Cut
    0x0041,  # Normal Cut
    0x0041,  # Normal Cut
    0x0141,  # Cut Curse
    0x0241,  # Cut Stone
    0x0341,  # Cut Stone Curse
    0x0441,  # Cut Water
    0x0441,  # Cut Water
    0x0441,  # Cut Water
    0x0541,  # Cut Water Curse
    0x0641,  # Cut Water Stone
    0x0841,  # Cut Dark
    0x0841,  # Cut Dark
    0x0841,  # Cut Dark
    0x0941,  # Cut Dark Curse
    0x0a41,  # Cut Dark Stone
    0x0c41,  # Cut Dark Water
    0x0c41,  # Cut Dark Water
    0x0c41,  # Cut Dark Water
    0x1041,  # Cut Holy
    0x1041,  # Cut Holy
    0x1041,  # Cut Holy
    0x1141,  # Cut Holy Curse
    0x1241,  # Cut Holy Stone
    0x1441,  # Cut Holy Water
    0x1441,  # Cut Holy Water
    0x1441,  # Cut Holy Water
    0x1841,  # Cut Holy Dark
    0x1841,  # Cut Holy Dark
    0x1841,  # Cut Holy Dark
    0x2041,  # Cut Ice
    0x2041,  # Cut Ice
    0x2041,  # Cut Ice
    0x2141,  # Cut Ice Curse
    0x2241,  # Cut Ice Stone
    0x2441,  # Cut Ice Water
    0x2441,  # Cut Ice Water
    0x2441,  # Cut Ice Water
    0x2841,  # Cut Ice Dark
    0x2841,  # Cut Ice Dark
    0x2841,  # Cut Ice Dark
    0x3041,  # Cut Holy Ice
    0x3041,  # Cut Holy Ice
    0x3041,  # Cut Holy Ice
    0x4041,  # Cut Lightning
    0x4041,  # Cut Lightning
    0x4041,  # Cut Lightning
    0x4141,  # Cut Lightning Curse
    0x4241,  # Cut Lightning Stone
    0x4441,  # Cut Lightning Water
    0x4441,  # Cut Lightning Water
    0x4441,  # Cut Lightning Water
    0x4841,  # Cut Lightning Dark
    0x4841,  # Cut Lightning Dark
    0x4841,  # Cut Lightning Dark
    0x5041,  # Cut Holy Lightning
    0x5041,  # Cut Holy Lightning
    0x5041,  # Cut Holy Lightning
    0x6041,  # Cut Ice Lightning
    0x6041,  # Cut Ice Lightning
    0x6041,  # Cut Ice Lightning
    0x8041,  # Cut Fire
    0x8041,  # Cut Fire
    0x8041,  # Cut Fire
    0x8141,  # Cut Fire Curse
    0x8241,  # Cut Fire Stone
    0x8441,  # Cut Fire Water
    0x8441,  # Cut Fire Water
    0x8441,  # Cut Fire Water
    0x8841,  # Cut Fire Dark
    0x8841,  # Cut Fire Dark
    0x8841,  # Cut Fire Dark
    0x9041,  # Cut Holy Fire
    0x9041,  # Cut Holy Fire
    0x9041,  # Cut Holy Fire
    0xA041,  # Cut Ice Fire
    0xA041,  # Cut Ice Fire
    0xA041,  # Cut Ice Fire
    0xC041,  # Cut Lightning Fire
    0xC041,  # Cut Lightning Fire
    0xC041,  # Cut Lightning Fire
    0x0044,  # Normal Cut
    0x0044,  # Normal Cut
    0x0044,  # Normal Cut
    0x0144,  # Cut Curse
    0x0244,  # Cut Stone
    0x0344,  # Cut Stone Curse
    0x0444,  # Cut Water
    0x0444,  # Cut Water
    0x0444,  # Cut Water
    0x0544,  # Cut Water Curse
    0x0644,  # Cut Water Stone
    0x0844,  # Cut Dark
    0x0844,  # Cut Dark
    0x0844,  # Cut Dark
    0x0944,  # Cut Dark Curse
    0x0a44,  # Cut Dark Stone
    0x0c44,  # Cut Dark Water
    0x0c44,  # Cut Dark Water
    0x0c44,  # Cut Dark Water
    0x1044,  # Cut Holy
    0x1044,  # Cut Holy
    0x1044,  # Cut Holy
    0x1144,  # Cut Holy Curse
    0x1244,  # Cut Holy Stone
    0x1444,  # Cut Holy Water
    0x1444,  # Cut Holy Water
    0x1444,  # Cut Holy Water
    0x1844,  # Cut Holy Dark
    0x1844,  # Cut Holy Dark
    0x1844,  # Cut Holy Dark
    0x2044,  # Cut Ice
    0x2044,  # Cut Ice
    0x2044,  # Cut Ice
    0x2144,  # Cut Ice Curse
    0x2244,  # Cut Ice Stone
    0x2444,  # Cut Ice Water
    0x2444,  # Cut Ice Water
    0x2444,  # Cut Ice Water
    0x2844,  # Cut Ice Dark
    0x2844,  # Cut Ice Dark
    0x2844,  # Cut Ice Dark
    0x3044,  # Cut Holy Ice
    0x3044,  # Cut Holy Ice
    0x3044,  # Cut Holy Ice
    0x4044,  # Cut Lightning
    0x4044,  # Cut Lightning
    0x4044,  # Cut Lightning
    0x4144,  # Cut Lightning Curse
    0x4244,  # Cut Lightning Stone
    0x4444,  # Cut Lightning Water
    0x4444,  # Cut Lightning Water
    0x4444,  # Cut Lightning Water
    0x4844,  # Cut Lightning Dark
    0x4844,  # Cut Lightning Dark
    0x4844,  # Cut Lightning Dark
    0x5044,  # Cut Holy Lightning
    0x5044,  # Cut Holy Lightning
    0x5044,  # Cut Holy Lightning
    0x6044,  # Cut Ice Lightning
    0x6044,  # Cut Ice Lightning
    0x6044,  # Cut Ice Lightning
    0x8044,  # Cut Fire
    0x8044,  # Cut Fire
    0x8044,  # Cut Fire
    0x8144,  # Cut Fire Curse
    0x8244,  # Cut Fire Stone
    0x8444,  # Cut Fire Water
    0x8444,  # Cut Fire Water
    0x8444,  # Cut Fire Water
    0x8844,  # Cut Fire Dark
    0x8844,  # Cut Fire Dark
    0x8844,  # Cut Fire Dark
    0x9044,  # Cut Holy Fire
    0x9044,  # Cut Holy Fire
    0x9044,  # Cut Holy Fire
    0xA044,  # Cut Ice Fire
    0xA044,  # Cut Ice Fire
    0xA044,  # Cut Ice Fire
    0xC044,  # Cut Lightning Fire
    0xC044,  # Cut Lightning Fire
    0xC044,  # Cut Lightning Fire
    0x0080,  # Normal Poison
    0x0080,  # Normal Poison
    0x0080,  # Normal Poison
    0x0180,  # Poison Curse
    0x0280,  # Poison Stone
    0x0480,  # Poison Water
    0x0480,  # Poison Water
    0x0480,  # Poison Water
    0x0880,  # Poison Dark
    0x0880,  # Poison Dark
    0x0880,  # Poison Dark
    0x1080,  # Poison Holy
    0x1080,  # Poison Holy
    0x1080,  # Poison Holy
    0x2080,  # Poison Ice
    0x2080,  # Poison Ice
    0x2080,  # Poison Ice
    0x4080,  # Poison Lightning
    0x4080,  # Poison Lightning
    0x4080,  # Poison Lightning
    0x8080,  # Poison Fire
    0x8080,  # Poison Fire
    0x8080,  # Poison Fire
    0x0084,  # Poison Big Toss
    0x0084,  # Poison Big Toss
    0x0084,  # Poison Big Toss
    0x0184,  # Poison Big Toss Curse
    0x0284,  # Poison Big Toss Stone
    0x0484,  # Poison Big Toss Water
    0x0484,  # Poison Big Toss Water
    0x0484,  # Poison Big Toss Water
    0x0884,  # Poison Big Toss Dark
    0x0884,  # Poison Big Toss Dark
    0x0884,  # Poison Big Toss Dark
    0x1084,  # Poison Big Toss Holy
    0x1084,  # Poison Big Toss Holy
    0x1084,  # Poison Big Toss Holy
    0x2084,  # Poison Big Toss Ice
    0x2084,  # Poison Big Toss Ice
    0x2084,  # Poison Big Toss Ice
    0x4084,  # Poison Big Toss Lightning
    0x4084,  # Poison Big Toss Lightning
    0x4084,  # Poison Big Toss Lightning
    0x8084,  # Poison Big Toss Fire
    0x8084,  # Poison Big Toss Fire
    0x8084,  # Poison Big Toss Fire
    0x0007,  # Cat
    0x0007,  # Cat
    0x0007,  # Cat
    0x0107,  # Cat Curse
    0x0207,  # Cat Stone
    0x0407,  # Cat Water
    0x0407,  # Cat Water
    0x0407,  # Cat Water
    0x0807,  # Cat Dark
    0x0807,  # Cat Dark
    0x0807,  # Cat Dark
    0x1007,  # Cat Holy
    0x1007,  # Cat Holy
    0x1007,  # Cat Holy
    0x2007,  # Cat Ice
    0x2007,  # Cat Ice
    0x2007,  # Cat Ice
    0x4007,  # Cat Lightning
    0x4007,  # Cat Lightning
    0x4007,  # Cat Lightning
    0x8007,  # Cat Fire
    0x8007,  # Cat Fire
    0x8007,  # Cat Fire
    0x0011,  # Normal Hit 1/6
    0x0011,  # Normal Hit 1/6
    0x0011,  # Normal Hit 1/6
    0x0411,  # Hit 1/6 Water
    0x0411,  # Hit 1/6 Water
    0x0411,  # Hit 1/6 Water
    0x0811,  # Hit 1/6 Dark
    0x0811,  # Hit 1/6 Dark
    0x0811,  # Hit 1/6 Dark
    0x0c11,  # Hit 1/6 Dark Water
    0x0c11,  # Hit 1/6 Dark Water
    0x0c11,  # Hit 1/6 Dark Water
    0x1011,  # Hit 1/6 Holy
    0x1011,  # Hit 1/6 Holy
    0x1011,  # Hit 1/6 Holy
    0x1411,  # Hit 1/6 Holy Water
    0x1411,  # Hit 1/6 Holy Water
    0x1411,  # Hit 1/6 Holy Water
    0x1811,  # Hit 1/6 Holy Dark
    0x1811,  # Hit 1/6 Holy Dark
    0x1811,  # Hit 1/6 Holy Dark
    0x2011,  # Hit 1/6 Ice
    0x2011,  # Hit 1/6 Ice
    0x2011,  # Hit 1/6 Ice
    0x2411,  # Hit 1/6 Ice Water
    0x2411,  # Hit 1/6 Ice Water
    0x2411,  # Hit 1/6 Ice Water
    0x2811,  # Hit 1/6 Ice Dark
    0x2811,  # Hit 1/6 Ice Dark
    0x2811,  # Hit 1/6 Ice Dark
    0x3011,  # Hit 1/6 Holy Ice
    0x3011,  # Hit 1/6 Holy Ice
    0x3011,  # Hit 1/6 Holy Ice
    0x4011,  # Hit 1/6 Lightning
    0x4011,  # Hit 1/6 Lightning
    0x4011,  # Hit 1/6 Lightning
    0x4411,  # Hit 1/6 Lightning Water
    0x4411,  # Hit 1/6 Lightning Water
    0x4411,  # Hit 1/6 Lightning Water
    0x4811,  # Hit 1/6 Lightning Dark
    0x4811,  # Hit 1/6 Lightning Dark
    0x4811,  # Hit 1/6 Lightning Dark
    0x5011,  # Hit 1/6 Holy Lightning
    0x5011,  # Hit 1/6 Holy Lightning
    0x5011,  # Hit 1/6 Holy Lightning
    0x6011,  # Hit 1/6 Ice Lightning
    0x6011,  # Hit 1/6 Ice Lightning
    0x6011,  # Hit 1/6 Ice Lightning
    0x8011,  # Hit 1/6 Fire
    0x8011,  # Hit 1/6 Fire
    0x8011,  # Hit 1/6 Fire
    0x8411,  # Hit 1/6 Fire Water
    0x8411,  # Hit 1/6 Fire Water
    0x8411,  # Hit 1/6 Fire Water
    0x8811,  # Hit 1/6 Fire Dark
    0x8811,  # Hit 1/6 Fire Dark
    0x8811,  # Hit 1/6 Fire Dark
    0x9011,  # Hit 1/6 Holy Fire
    0x9011,  # Hit 1/6 Holy Fire
    0x9011,  # Hit 1/6 Holy Fire
    0xA011,  # Hit 1/6 Ice Fire
    0xA011,  # Hit 1/6 Ice Fire
    0xA011,  # Hit 1/6 Ice Fire
    0xC011,  # Hit 1/6 Lightning Fire
    0xC011,  # Hit 1/6 Lightning Fire
    0xC011,  # Hit 1/6 Lightning Fire
    0x0051,  # Normal Cut 1/6
    0x0051,  # Normal Cut 1/6
    0x0051,  # Normal Cut 1/6
    0x0451,  # Cut 1/6 Water
    0x0451,  # Cut 1/6 Water
    0x0451,  # Cut 1/6 Water
    0x0851,  # Cut 1/6 Dark
    0x0851,  # Cut 1/6 Dark
    0x0851,  # Cut 1/6 Dark
    0x0c51,  # Cut 1/6 Dark Water
    0x0c51,  # Cut 1/6 Dark Water
    0x0c51,  # Cut 1/6 Dark Water
    0x1051,  # Cut 1/6 Holy
    0x1051,  # Cut 1/6 Holy
    0x1051,  # Cut 1/6 Holy
    0x1451,  # Cut 1/6 Holy Water
    0x1451,  # Cut 1/6 Holy Water
    0x1451,  # Cut 1/6 Holy Water
    0x1851,  # Cut 1/6 Holy Dark
    0x1851,  # Cut 1/6 Holy Dark
    0x1851,  # Cut 1/6 Holy Dark
    0x2051,  # Cut 1/6 Ice
    0x2051,  # Cut 1/6 Ice
    0x2051,  # Cut 1/6 Ice
    0x2451,  # Cut 1/6 Ice Water
    0x2451,  # Cut 1/6 Ice Water
    0x2451,  # Cut 1/6 Ice Water
    0x2851,  # Cut 1/6 Ice Dark
    0x2851,  # Cut 1/6 Ice Dark
    0x2851,  # Cut 1/6 Ice Dark
    0x3051,  # Cut 1/6 Holy Ice
    0x3051,  # Cut 1/6 Holy Ice
    0x3051,  # Cut 1/6 Holy Ice
    0x4051,  # Cut 1/6 Lightning
    0x4051,  # Cut 1/6 Lightning
    0x4051,  # Cut 1/6 Lightning
    0x4451,  # Cut 1/6 Lightning Water
    0x4451,  # Cut 1/6 Lightning Water
    0x4451,  # Cut 1/6 Lightning Water
    0x4851,  # Cut 1/6 Lightning Dark
    0x4851,  # Cut 1/6 Lightning Dark
    0x4851,  # Cut 1/6 Lightning Dark
    0x5051,  # Cut 1/6 Holy Lightning
    0x5051,  # Cut 1/6 Holy Lightning
    0x5051,  # Cut 1/6 Holy Lightning
    0x6051,  # Cut 1/6 Ice Lightning
    0x6051,  # Cut 1/6 Ice Lightning
    0x6051,  # Cut 1/6 Ice Lightning
    0x8051,  # Cut 1/6 Fire
    0x8051,  # Cut 1/6 Fire
    0x8051,  # Cut 1/6 Fire
    0x8451,  # Cut 1/6 Fire Water
    0x8451,  # Cut 1/6 Fire Water
    0x8451,  # Cut 1/6 Fire Water
    0x8851,  # Cut 1/6 Fire Dark
    0x8851,  # Cut 1/6 Fire Dark
    0x8851,  # Cut 1/6 Fire Dark
    0x9051,  # Cut 1/6 Holy Fire
    0x9051,  # Cut 1/6 Holy Fire
    0x9051,  # Cut 1/6 Holy Fire
    0xA051,  # Cut 1/6 Ice Fire
    0xA051,  # Cut 1/6 Ice Fire
    0xA051,  # Cut 1/6 Ice Fire
    0xC051,  # Cut 1/6 Lightning Fire
    0xC051,  # Cut 1/6 Lightning Fire
    0xC051,  # Cut 1/6 Lightning Fire
]

enemy_weak_type_list = [
    0x0020,  # hit
    0x0040,  # cut
    0x0080,  # poison
    0x8000,  # Fire
    0x2000,  # Ice
    0x1000,  # Holy
    0x4000,  # Lightning
    0x0100,  # Curse
    0x0200,  # Stone
    0x0800,  # Dark
]


class DropData:
    def __init__(self, vanilla_drop: str, drop_addresses: list):
        self.vanilla_drop = vanilla_drop
        self.drop_addresses = drop_addresses


Global_drop = [
    DropData("Heart", [0x043c3612, 0x044917e2, 0x0455cc62, 0x045e99ba, 0x0467755a, 0x048fb156,
                       0x049d3a26, 0x04aa1a42, 0x04b68aea, 0x04c328ee, 0x04cfbd2e, 0x04da5736, 0x04e327d2, 0x04ee32fe,
                       0x04f86072, 0x05050946, 0x050f8e72, 0x051ade86, 0x0526c722, 0x053f6466, 0x054b290e, 0x05573db2,
                       0x0560fbe2, 0x056be926, 0x0575197a, 0x057e077a, 0x05883f4a, 0x0590361a, 0x059bca06, 0x05a6ee9a,
                       0x05af32a6, 0x0606f0da, 0x060fdd0e, 0x061a7792, 0x0624789a, 0x0630618a, 0x063aafe2, 0x06471a0a,
                       0x065094be, 0x065918ba, 0x06621d0a, 0x066b4092, 0x06742eaa, 0x067d0d06, 0x06862056, 0x0692c45e,
                       0x069d21f2, 0x06a611d6, 0x047a3e76]),
    DropData("Heart", [0x043c362e, 0x044917fe, 0x0455cc7e, 0x045e99d6, 0x04677576, 0x048fb172,
                       0x049d3a42, 0x04aa1a5e, 0x04b68b06, 0x04c3290a, 0x04cfbd4a, 0x04da5752, 0x04e327ee, 0x04ee331a,
                       0x04f8608e, 0x05050962, 0x050f8e8e, 0x051adea2, 0x0526c73e, 0x053f6482, 0x054b292a, 0x05573dce,
                       0x0560fbfe, 0x056be942, 0x05751996, 0x057e0796, 0x05883f66, 0x05903636, 0x059bca22, 0x05a6eeb6,
                       0x05af32c2, 0x0606f0f6, 0x060fdd2a, 0x061a77ae, 0x062478b6, 0x063061a6, 0x063aaffe, 0x06471a26,
                       0x065094da, 0x065918d6, 0x06621d26, 0x066b40ae, 0x06742ec6, 0x067d0d22, 0x06862072, 0x0692c47a,
                       0x069d220e, 0x06a611f2, 0x047a3fc2]),
    DropData("Heart", [0x043c3630, 0x04491800, 0x0455cc80, 0x045e99d8, 0x04677578, 0x048fb174,
                       0x049d3a44, 0x04aa1a60, 0x04b68b08, 0x04c3290c, 0x04cfbd4c, 0x04da5754, 0x04e327f0, 0x04ee331c,
                       0x04f86090, 0x05050964, 0x050f8e90, 0x051adea4, 0x0526c740, 0x053f6484, 0x054b292c, 0x05573dd0,
                       0x0560fc00, 0x056be944, 0x05751998, 0x057e0798, 0x05883f68, 0x05903638, 0x059bca24, 0x05a6eeb8,
                       0x05af32c4, 0x0606f0f8, 0x060fdd2c, 0x061a77b0, 0x062478b8, 0x063061a8, 0x063ab000, 0x06471a28,
                       0x065094dc, 0x065918d8, 0x06621d28, 0x066b40b0, 0x06742ec8, 0x067d0d24, 0x06862074, 0x0692c47c,
                       0x069d2210, 0x06a611f4, 0x047a3fc4]),
    DropData("Heart", [0x043c3632, 0x04491802, 0x0455cc82, 0x045e99da, 0x0467757a, 0x048fb176,
                       0x049d3a46, 0x04aa1a62, 0x04b68b0a, 0x04c3290e, 0x04cfbd4e, 0x04da5756, 0x04e327f2, 0x04ee331e,
                       0x04f86092, 0x05050966, 0x050f8e92, 0x051adea6, 0x0526c742, 0x053f6486, 0x054b292e, 0x05573dd2,
                       0x0560fc02, 0x056be946, 0x0575199a, 0x057e079a, 0x05883f6a, 0x0590363a, 0x059bca26, 0x05a6eeba,
                       0x05af32c6, 0x0606f0fa, 0x060fdd2e, 0x061a77b2, 0x062478ba, 0x063061aa, 0x063ab002, 0x06471a2a,
                       0x065094de, 0x065918da, 0x06621d2a, 0x066b40b2, 0x06742eca, 0x067d0d26, 0x06862076, 0x0692c47e,
                       0x069d2212, 0x06a611f6, 0x047a3fc6]),
    DropData("Heart", [0x043c3634, 0x04491804, 0x0455cc84, 0x045e99dc, 0x0467757c, 0x048fb178,
                       0x049d3a48, 0x04aa1a64, 0x04b68b0c, 0x04c32910, 0x04cfbd50, 0x04da5758, 0x04e327f4, 0x04ee3320,
                       0x04f86094, 0x05050968, 0x050f8e94, 0x051adea8, 0x0526c744, 0x053f6488, 0x054b2930, 0x05573dd4,
                       0x0560fc04, 0x056be948, 0x0575199c, 0x057e079c, 0x05883f6c, 0x0590363c, 0x059bca28, 0x05a6eebc,
                       0x05af32c8, 0x0606f0fc, 0x060fdd30, 0x061a77b4, 0x062478bc, 0x063061ac, 0x063ab004, 0x06471a2c,
                       0x065094e0, 0x065918dc, 0x06621d2c, 0x066b40b4, 0x06742ecc, 0x067d0d28, 0x06862078, 0x0692c480,
                       0x069d2214, 0x06a611f8, 0x047a3fc8]),
    DropData("Heart", [0x043c3636, 0x04491806, 0x0455cc86, 0x045e99de, 0x0467757e, 0x048fb17a,
                       0x049d3a4a, 0x04aa1a66, 0x04b68b0e, 0x04c32912, 0x04cfbd52, 0x04da575a, 0x04e327f6, 0x04ee3322,
                       0x04f86096, 0x0505096a, 0x050f8e96, 0x051adeaa, 0x0526c746, 0x053f648a, 0x054b2932, 0x05573dd6,
                       0x0560fc06, 0x056be94a, 0x0575199e, 0x057e079e, 0x05883f6e, 0x0590363e, 0x059bca2a, 0x05a6eebe,
                       0x05af32ca, 0x0606f0fe, 0x060fdd32, 0x061a77b6, 0x062478be, 0x063061ae, 0x063ab006, 0x06471a2e,
                       0x065094e2, 0x065918de, 0x06621d2e, 0x066b40b6, 0x06742ece, 0x067d0d2a, 0x0686207a, 0x0692c482,
                       0x069d2216, 0x06a611fa, 0x047a3fca]),
    DropData("Heart", [0x043c3638, 0x04491808, 0x0455cc88, 0x045e99e0, 0x04677580, 0x048fb17c,
                       0x049d3a4c, 0x04aa1a68, 0x04b68b10, 0x04c32914, 0x04cfbd54, 0x04da575c, 0x04e327f8, 0x04ee3324,
                       0x04f86098, 0x0505096c, 0x050f8e98, 0x051adeac, 0x0526c748, 0x053f648c, 0x054b2934, 0x05573dd8,
                       0x0560fc08, 0x056be94c, 0x057519a0, 0x057e07a0, 0x05883f70, 0x05903640, 0x059bca2c, 0x05a6eec0,
                       0x05af32cc, 0x0606f100, 0x060fdd34, 0x061a77b8, 0x062478c0, 0x063061b0, 0x063ab008, 0x06471a30,
                       0x065094e4, 0x065918e0, 0x06621d30, 0x066b40b8, 0x06742ed0, 0x067d0d2c, 0x0686207c, 0x0692c484,
                       0x069d2218, 0x06a611fc, 0x047a3fcc]),
    DropData("Heart", [0x043c363a, 0x0449180a, 0x0455cc8a, 0x045e99e2, 0x04677582, 0x048fb17e,
                       0x049d3a4e, 0x04aa1a6a, 0x04b68b12, 0x04c32916, 0x04cfbd56, 0x04da575e, 0x04e327fa, 0x04ee3326,
                       0x04f8609a, 0x0505096e, 0x050f8e9a, 0x051adeae, 0x0526c74a, 0x053f648e, 0x054b2936, 0x05573dda,
                       0x0560fc0a, 0x056be94e, 0x057519a2, 0x057e07a2, 0x05883f72, 0x05903642, 0x059bca2e, 0x05a6eec2,
                       0x05af32ce, 0x0606f102, 0x060fdd36, 0x061a77ba, 0x062478c2, 0x063061b2, 0x063ab00a, 0x06471a32,
                       0x065094e6, 0x065918e2, 0x06621d32, 0x066b40ba, 0x06742ed2, 0x067d0d2e, 0x0686207e, 0x0692c486,
                       0x069d221a, 0x06a611fe, 0x047a3fce]),
    DropData("Heart", [0x043c363c, 0x0449180c, 0x0455cc8c, 0x045e99e4, 0x04677584, 0x048fb180,
                       0x049d3a50, 0x04aa1a6c, 0x04b68b14, 0x04c32918, 0x04cfbd58, 0x04da5760, 0x04e327fc, 0x04ee3328,
                       0x04f8609c, 0x05050970, 0x050f8e9c, 0x051adeb0, 0x0526c74c, 0x053f6490, 0x054b2938, 0x05573ddc,
                       0x0560fc0c, 0x056be950, 0x057519a4, 0x057e07a4, 0x05883f74, 0x05903644, 0x059bca30, 0x05a6eec4,
                       0x05af32d0, 0x0606f104, 0x060fdd38, 0x061a77bc, 0x062478c4, 0x063061b4, 0x063ab00c, 0x06471a34,
                       0x065094e8, 0x065918e4, 0x06621d34, 0x066b40bc, 0x06742ed4, 0x067d0d30, 0x06862080, 0x0692c488,
                       0x069d221c, 0x06a61200, 0x047a3fd0]),
    DropData("Heart", [0x043c363e, 0x0449180e, 0x0455cc8e, 0x045e99e6, 0x04677586, 0x048fb182,
                       0x049d3a52, 0x04aa1a6e, 0x04b68b16, 0x04c3291a, 0x04cfbd5a, 0x04da5762, 0x04e327fe, 0x04ee332a,
                       0x04f8609e, 0x05050972, 0x050f8e9e, 0x051adeb2, 0x0526c74e, 0x053f6492, 0x054b293a, 0x05573dde,
                       0x0560fc0e, 0x056be952, 0x057519a6, 0x057e07a6, 0x05883f76, 0x05903646, 0x059bca32, 0x05a6eec6,
                       0x05af32d2, 0x0606f106, 0x060fdd3a, 0x061a77be, 0x062478c6, 0x063061b6, 0x063ab00e, 0x06471a36,
                       0x065094ea, 0x065918e6, 0x06621d36, 0x066b40be, 0x06742ed6, 0x067d0d32, 0x06862082, 0x0692c48a,
                       0x069d221e, 0x06a61202, 0x047a3fd2]),
    DropData("Heart", [0x043c3640, 0x04491810, 0x0455cc90, 0x045e99e8, 0x04677588, 0x048fb184,
                       0x049d3a54, 0x04aa1a70, 0x04b68b18, 0x04c3291c, 0x04cfbd5c, 0x04da5764, 0x04e32800, 0x04ee332c,
                       0x04f860a0, 0x05050974, 0x050f8ea0, 0x051adeb4, 0x0526c750, 0x053f6494, 0x054b293c, 0x05573de0,
                       0x0560fc10, 0x056be954, 0x057519a8, 0x057e07a8, 0x05883f78, 0x05903648, 0x059bca34, 0x05a6eec8,
                       0x05af32d4, 0x0606f108, 0x060fdd3c, 0x061a77c0, 0x062478c8, 0x063061b8, 0x063ab010, 0x06471a38,
                       0x065094ec, 0x065918e8, 0x06621d38, 0x066b40c0, 0x06742ed8, 0x067d0d34, 0x06862084, 0x0692c48c,
                       0x069d2220, 0x06a61204, 0x047a3fd4]),
    DropData("Heart", [0x043c3642, 0x04491812, 0x0455cc92, 0x045e99ea, 0x0467758a, 0x048fb186,
                       0x049d3a56, 0x04aa1a72, 0x04b68b1a, 0x04c3291e, 0x04cfbd5e, 0x04da5766, 0x04e32802, 0x04ee332e,
                       0x04f860a2, 0x05050976, 0x050f8ea2, 0x051adeb6, 0x0526c752, 0x053f6496, 0x054b293e, 0x05573de2,
                       0x0560fc12, 0x056be956, 0x057519aa, 0x057e07aa, 0x05883f7a, 0x0590364a, 0x059bca36, 0x05a6eeca,
                       0x05af32d6, 0x0606f10a, 0x060fdd3e, 0x061a77c2, 0x062478ca, 0x063061ba, 0x063ab012, 0x06471a3a,
                       0x065094ee, 0x065918ea, 0x06621d3a, 0x066b40c2, 0x06742eda, 0x067d0d36, 0x06862086, 0x0692c48e,
                       0x069d2222, 0x06a61206, 0x047a3fd6]),
    DropData("Big heart", [0x043c3644, 0x04491814, 0x0455cc94, 0x045e99ec, 0x0467758c,
                           0x048fb188, 0x049d3a58, 0x04aa1a74, 0x04b68b1c, 0x04c32920, 0x04cfbd60, 0x04da5768,
                           0x04e32804, 0x04ee3330, 0x04f860a4, 0x05050978, 0x050f8ea4, 0x051adeb8, 0x0526c754,
                           0x053f6498, 0x054b2940, 0x05573de4, 0x0560fc14, 0x056be958, 0x057519ac, 0x057e07ac,
                           0x05883f7c, 0x0590364c, 0x059bca38, 0x05a6eecc, 0x05af32d8, 0x0606f10c, 0x060fdd40,
                           0x061a77c4, 0x062478cc, 0x063061bc, 0x063ab014, 0x06471a3c, 0x065094f0, 0x065918ec,
                           0x06621d3c, 0x066b40c4, 0x06742edc, 0x067d0d38, 0x06862088, 0x0692c490, 0x069d2224,
                           0x06a61208, 0x047a3fd8]),
    DropData("Big heart", [0x043c3646, 0x04491816, 0x0455cc96, 0x045e99ee, 0x0467758e,
                           0x048fb18a, 0x049d3a5a, 0x04aa1a76, 0x04b68b1e, 0x04c32922, 0x04cfbd62, 0x04da576a,
                           0x04e32806, 0x04ee3332, 0x04f860a6, 0x0505097a, 0x050f8ea6, 0x051adeba, 0x0526c756,
                           0x053f649a, 0x054b2942, 0x05573de6, 0x0560fc16, 0x056be95a, 0x057519ae, 0x057e07ae,
                           0x05883f7e, 0x0590364e, 0x059bca3a, 0x05a6eece, 0x05af32da, 0x0606f10e, 0x060fdd42,
                           0x061a77c6, 0x062478ce, 0x063061be, 0x063ab016, 0x06471a3e, 0x065094f2, 0x065918ee,
                           0x06621d3e, 0x066b40c6, 0x06742ede, 0x067d0d3a, 0x0686208a, 0x0692c492, 0x069d2226,
                           0x06a6120a, 0x047a3fda]),
    DropData("$1", [0x043c3614, 0x044917e4, 0x0455cc64, 0x045e99bc, 0x0467755c, 0x048fb158,
                    0x049d3a28, 0x04aa1a44, 0x04b68aec, 0x04c328f0, 0x04cfbd30, 0x04da5738, 0x04e327d4, 0x04ee3300,
                    0x04f86074, 0x05050948, 0x050f8e74, 0x051ade88, 0x0526c724, 0x053f6468, 0x054b2910, 0x05573db4,
                    0x0560fbe4, 0x056be928, 0x0575197c, 0x057e077c, 0x05883f4c, 0x0590361c, 0x059bca08, 0x05a6ee9c,
                    0x05af32a8, 0x0606f0dc, 0x060fdd10, 0x061a7794, 0x0624789c, 0x0630618c, 0x063aafe4, 0x06471a0c,
                    0x065094c0, 0x065918bc, 0x06621d0c, 0x066b4094, 0x06742eac, 0x067d0d08, 0x06862058, 0x0692c460,
                    0x069d21f4, 0x06a611d8, 0x047a3fa8]),
    DropData("$1", [0x043c3648, 0x04491818, 0x0455cc98, 0x045e99f0, 0x04677590, 0x048fb18c,
                    0x049d3a5c, 0x04aa1a78, 0x04b68b20, 0x04c32924, 0x04cfbd64, 0x04da576c, 0x04e32808, 0x04ee3334,
                    0x04f860a8, 0x0505097c, 0x050f8ea8, 0x051adebc, 0x0526c758, 0x053f649c, 0x054b2944, 0x05573de8,
                    0x0560fc18, 0x056be95c, 0x057519b0, 0x057e07b0, 0x05883f80, 0x05903650, 0x059bca3c, 0x05a6eed0,
                    0x05af32dc, 0x0606f110, 0x060fdd44, 0x061a77c8, 0x062478d0, 0x063061c0, 0x063ab018, 0x06471a40,
                    0x065094f4, 0x065918f0, 0x06621d40, 0x066b40c8, 0x06742ee0, 0x067d0d3c, 0x0686208c, 0x0692c494,
                    0x069d2228, 0x06a6120c, 0x047a3fdc]),
    DropData("$25", [0x043c3610, 0x044917e0, 0x0455cc60, 0x045e99b8, 0x04677558, 0x048fb154,
                     0x049d3a24, 0x04aa1a40, 0x04b68ae8, 0x04c328ec, 0x04cfbd2c, 0x04da5734, 0x04e327d0, 0x04ee32fc,
                     0x04f86070, 0x05050944, 0x050f8e70, 0x051ade84, 0x0526c720, 0x053f6464, 0x054b290c, 0x05573db0,
                     0x0560fbe0, 0x056be924, 0x05751978, 0x057e0778, 0x05883f48, 0x05903618, 0x059bca04, 0x05a6ee98,
                     0x05af32a4, 0x0606f0d8, 0x060fdd0c, 0x061a7790, 0x06247898, 0x06306188, 0x063aafe0, 0x06471a08,
                     0x065094bc, 0x065918b8, 0x06621d08, 0x066b4090, 0x06742ea8, 0x067d0d04, 0x06862054, 0x0692c45c,
                     0x069d21f0, 0x06a611d4, 0x047a3e74]),
    DropData("$25", [0x043c3616, 0x044917e6, 0x0455cc66, 0x045e99be, 0x0467755e, 0x048fb15a,
                     0x049d3a2a, 0x04aa1a46, 0x04b68aee, 0x04c328f2, 0x04cfbd32, 0x04da573a, 0x04e327d6, 0x04ee3302,
                     0x04f86076, 0x0505094a, 0x050f8e76, 0x051ade8a, 0x0526c726, 0x053f646a, 0x054b2912, 0x05573db6,
                     0x0560fbe6, 0x056be92a, 0x0575197e, 0x057e077e, 0x05883f4e, 0x0590361e, 0x059bca0a, 0x05a6ee9e,
                     0x05af32aa, 0x0606f0de, 0x060fdd12, 0x061a7796, 0x0624789e, 0x0630618e, 0x063aafe6, 0x06471a0e,
                     0x065094c2, 0x065918be, 0x06621d0e, 0x066b4096, 0x06742eae, 0x067d0d0a, 0x0686205a, 0x0692c462,
                     0x069d21f6, 0x06a611da, 0x047a3faa]),
    DropData("$25", [0x043c3618, 0x044917e8, 0x0455cc68, 0x045e99c0, 0x04677560, 0x048fb15c,
                     0x049d3a2c, 0x04aa1a48, 0x04b68af0, 0x04c328f4, 0x04cfbd34, 0x04da573c, 0x04e327d8, 0x04ee3304,
                     0x04f86078, 0x0505094c, 0x050f8e78, 0x051ade8c, 0x0526c728, 0x053f646c, 0x054b2914, 0x05573db8,
                     0x0560fbe8, 0x056be92c, 0x05751980, 0x057e0780, 0x05883f50, 0x05903620, 0x059bca0c, 0x05a6eea0,
                     0x05af32ac, 0x0606f0e0, 0x060fdd14, 0x061a7798, 0x062478a0, 0x06306190, 0x063aafe8, 0x06471a10,
                     0x065094c4, 0x065918c0, 0x06621d10, 0x066b4098, 0x06742eb0, 0x067d0d0c, 0x0686205c, 0x0692c464,
                     0x069d21f8, 0x06a611dc, 0x047a3fac]),
    DropData("$25", [0x043c361a, 0x044917ea, 0x0455cc6a, 0x045e99c2, 0x04677562, 0x048fb15e,
                     0x049d3a2e, 0x04aa1a4a, 0x04b68af2, 0x04c328f6, 0x04cfbd36, 0x04da573e, 0x04e327da, 0x04ee3306,
                     0x04f8607a, 0x0505094e, 0x050f8e7a, 0x051ade8e, 0x0526c72a, 0x053f646e, 0x054b2916, 0x05573dba,
                     0x0560fbea, 0x056be92e, 0x05751982, 0x057e0782, 0x05883f52, 0x05903622, 0x059bca0e, 0x05a6eea2,
                     0x05af32ae, 0x0606f0e2, 0x060fdd16, 0x061a779a, 0x062478a2, 0x06306192, 0x063aafea, 0x06471a12,
                     0x065094c6, 0x065918c2, 0x06621d12, 0x066b409a, 0x06742eb2, 0x067d0d0e, 0x0686205e, 0x0692c466,
                     0x069d21fa, 0x06a611de, 0x047a3fae]),
    DropData("$25", [0x043c361c, 0x044917ec, 0x0455cc6c, 0x045e99c4, 0x04677564, 0x048fb160,
                     0x049d3a30, 0x04aa1a4c, 0x04b68af4, 0x04c328f8, 0x04cfbd38, 0x04da5740, 0x04e327dc, 0x04ee3308,
                     0x04f8607c, 0x05050950, 0x050f8e7c, 0x051ade90, 0x0526c72c, 0x053f6470, 0x054b2918, 0x05573dbc,
                     0x0560fbec, 0x056be930, 0x05751984, 0x057e0784, 0x05883f54, 0x05903624, 0x059bca10, 0x05a6eea4,
                     0x05af32b0, 0x0606f0e4, 0x060fdd18, 0x061a779c, 0x062478a4, 0x06306194, 0x063aafec, 0x06471a14,
                     0x065094c8, 0x065918c4, 0x06621d14, 0x066b409c, 0x06742eb4, 0x067d0d10, 0x06862060, 0x0692c468,
                     0x069d21fc, 0x06a611e0, 0x047a3fb0]),
    DropData("$25", [0x043c361e, 0x044917ee, 0x0455cc6e, 0x045e99c6, 0x04677566, 0x048fb162,
                     0x049d3a32, 0x04aa1a4e, 0x04b68af6, 0x04c328fa, 0x04cfbd3a, 0x04da5742, 0x04e327de, 0x04ee330a,
                     0x04f8607e, 0x05050952, 0x050f8e7e, 0x051ade92, 0x0526c72e, 0x053f6472, 0x054b291a, 0x05573dbe,
                     0x0560fbee, 0x056be932, 0x05751986, 0x057e0786, 0x05883f56, 0x05903626, 0x059bca12, 0x05a6eea6,
                     0x05af32b2, 0x0606f0e6, 0x060fdd1a, 0x061a779e, 0x062478a6, 0x06306196, 0x063aafee, 0x06471a16,
                     0x065094ca, 0x065918c6, 0x06621d16, 0x066b409e, 0x06742eb6, 0x067d0d12, 0x06862062, 0x0692c46a,
                     0x069d21fe, 0x06a611e2, 0x047a3fb2]),
    DropData("$25", [0x043c3620, 0x044917f0, 0x0455cc70, 0x045e99c8, 0x04677568, 0x048fb164,
                     0x049d3a34, 0x04aa1a50, 0x04b68af8, 0x04c328fc, 0x04cfbd3c, 0x04da5744, 0x04e327e0, 0x04ee330c,
                     0x04f86080, 0x05050954, 0x050f8e80, 0x051ade94, 0x0526c730, 0x053f6474, 0x054b291c, 0x05573dc0,
                     0x0560fbf0, 0x056be934, 0x05751988, 0x057e0788, 0x05883f58, 0x05903628, 0x059bca14, 0x05a6eea8,
                     0x05af32b4, 0x0606f0e8, 0x060fdd1c, 0x061a77a0, 0x062478a8, 0x06306198, 0x063aaff0, 0x06471a18,
                     0x065094cc, 0x065918c8, 0x06621d18, 0x066b40a0, 0x06742eb8, 0x067d0d14, 0x06862064, 0x0692c46c,
                     0x069d2200, 0x06a611e4, 0x047a3fb4]),
    DropData("$50", [0x043c3622, 0x044917f2, 0x0455cc72, 0x045e99ca, 0x0467756a, 0x048fb166,
                     0x049d3a36, 0x04aa1a52, 0x04b68afa, 0x04c328fe, 0x04cfbd3e, 0x04da5746, 0x04e327e2, 0x04ee330e,
                     0x04f86082, 0x05050956, 0x050f8e82, 0x051ade96, 0x0526c732, 0x053f6476, 0x054b291e, 0x05573dc2,
                     0x0560fbf2, 0x056be936, 0x0575198a, 0x057e078a, 0x05883f5a, 0x0590362a, 0x059bca16, 0x05a6eeaa,
                     0x05af32b6, 0x0606f0ea, 0x060fdd1e, 0x061a77a2, 0x062478aa, 0x0630619a, 0x063aaff2, 0x06471a1a,
                     0x065094ce, 0x065918ca, 0x06621d1a, 0x066b40a2, 0x06742eba, 0x067d0d16, 0x06862066, 0x0692c46e,
                     0x069d2202, 0x06a611e6, 0x047a3fb6]),
    DropData("$50", [0x043c3624, 0x044917f4, 0x0455cc74, 0x045e99cc, 0x0467756c, 0x048fb168,
                     0x049d3a38, 0x04aa1a54, 0x04b68afc, 0x04c32900, 0x04cfbd40, 0x04da5748, 0x04e327e4, 0x04ee3310,
                     0x04f86084, 0x05050958, 0x050f8e84, 0x051ade98, 0x0526c734, 0x053f6478, 0x054b2920, 0x05573dc4,
                     0x0560fbf4, 0x056be938, 0x0575198c, 0x057e078c, 0x05883f5c, 0x0590362c, 0x059bca18, 0x05a6eeac,
                     0x05af32b8, 0x0606f0ec, 0x060fdd20, 0x061a77a4, 0x062478ac, 0x0630619c, 0x063aaff4, 0x06471a1c,
                     0x065094d0, 0x065918cc, 0x06621d1c, 0x066b40a4, 0x06742ebc, 0x067d0d18, 0x06862068, 0x0692c470,
                     0x069d2204, 0x06a611e8, 0x047a3fb8]),
    DropData("$50", [0x043c3626, 0x044917f6, 0x0455cc76, 0x045e99ce, 0x0467756e, 0x048fb16a,
                     0x049d3a3a, 0x04aa1a56, 0x04b68afe, 0x04c32902, 0x04cfbd42, 0x04da574a, 0x04e327e6, 0x04ee3312,
                     0x04f86086, 0x0505095a, 0x050f8e86, 0x051ade9a, 0x0526c736, 0x053f647a, 0x054b2922, 0x05573dc6,
                     0x0560fbf6, 0x056be93a, 0x0575198e, 0x057e078e, 0x05883f5e, 0x0590362e, 0x059bca1a, 0x05a6eeae,
                     0x05af32ba, 0x0606f0ee, 0x060fdd22, 0x061a77a6, 0x062478ae, 0x0630619e, 0x063aaff6, 0x06471a1e,
                     0x065094d2, 0x065918ce, 0x06621d1e, 0x066b40a6, 0x06742ebe, 0x067d0d1a, 0x0686206a, 0x0692c472,
                     0x069d2206, 0x06a611ea, 0x047a3fba]),
    DropData("$50", [0x043c3628, 0x044917f8, 0x0455cc78, 0x045e99d0, 0x04677570, 0x048fb16c,
                     0x049d3a3c, 0x04aa1a58, 0x04b68b00, 0x04c32904, 0x04cfbd44, 0x04da574c, 0x04e327e8, 0x04ee3314,
                     0x04f86088, 0x0505095c, 0x050f8e88, 0x051ade9c, 0x0526c738, 0x053f647c, 0x054b2924, 0x05573dc8,
                     0x0560fbf8, 0x056be93c, 0x05751990, 0x057e0790, 0x05883f60, 0x05903630, 0x059bca1c, 0x05a6eeb0,
                     0x05af32bc, 0x0606f0f0, 0x060fdd24, 0x061a77a8, 0x062478b0, 0x063061a0, 0x063aaff8, 0x06471a20,
                     0x065094d4, 0x065918d0, 0x06621d20, 0x066b40a8, 0x06742ec0, 0x067d0d1c, 0x0686206c, 0x0692c474,
                     0x069d2208, 0x06a611ec, 0x047a3fbc]),
    DropData("$100", [0x043c362a, 0x044917fa, 0x0455cc7a, 0x045e99d2, 0x04677572, 0x048fb16e,
                      0x049d3a3e, 0x04aa1a5a, 0x04b68b02, 0x04c32906, 0x04cfbd46, 0x04da574e, 0x04e327ea, 0x04ee3316,
                      0x04f8608a, 0x0505095e, 0x050f8e8a, 0x051ade9e, 0x0526c73a, 0x053f647e, 0x054b2926, 0x05573dca,
                      0x0560fbfa, 0x056be93e, 0x05751992, 0x057e0792, 0x05883f62, 0x05903632, 0x059bca1e, 0x05a6eeb2,
                      0x05af32be, 0x0606f0f2, 0x060fdd26, 0x061a77aa, 0x062478b2, 0x063061a2, 0x063aaffa, 0x06471a22,
                      0x065094d6, 0x065918d2, 0x06621d22, 0x066b40aa, 0x06742ec2, 0x067d0d1e, 0x0686206e, 0x0692c476,
                      0x069d220a, 0x06a611ee, 0x047a3fbe]),
    DropData("$100", [0x043c362c, 0x044917fc, 0x0455cc7c, 0x045e99d4, 0x04677574, 0x048fb170,
                      0x049d3a40, 0x04aa1a5c, 0x04b68b04, 0x04c32908, 0x04cfbd48, 0x04da5750, 0x04e327ec, 0x04ee3318,
                      0x04f8608c, 0x05050960, 0x050f8e8c, 0x051adea0, 0x0526c73c, 0x053f6480, 0x054b2928, 0x05573dcc,
                      0x0560fbfc, 0x056be940, 0x05751994, 0x057e0794, 0x05883f64, 0x05903634, 0x059bca20, 0x05a6eeb4,
                      0x05af32c0, 0x0606f0f4, 0x060fdd28, 0x061a77ac, 0x062478b4, 0x063061a4, 0x063aaffc, 0x06471a24,
                      0x065094d8, 0x065918d4, 0x06621d24, 0x066b40ac, 0x06742ec4, 0x067d0d20, 0x06862070, 0x0692c478,
                      0x069d220c, 0x06a611f0, 0x047a3fc0]),
    DropData("$250", [0x043c364a, 0x0449181a, 0x0455cc9a, 0x045e99f2, 0x04677592, 0x048fb18e,
                      0x049d3a5e, 0x04aa1a7a, 0x04b68b22, 0x04c32926, 0x04cfbd66, 0x04da576e, 0x04e3280a, 0x04ee3336,
                      0x04f860aa, 0x0505097e, 0x050f8eaa, 0x051adebe, 0x0526c75a, 0x053f649e, 0x054b2946, 0x05573dea,
                      0x0560fc1a, 0x056be95e, 0x057519b2, 0x057e07b2, 0x05883f82, 0x05903652, 0x059bca3e, 0x05a6eed2,
                      0x05af32de, 0x0606f112, 0x060fdd46, 0x061a77ca, 0x062478d2, 0x063061c2, 0x063ab01a, 0x06471a42,
                      0x065094f6, 0x065918f2, 0x06621d42, 0x066b40ca, 0x06742ee2, 0x067d0d3e, 0x0686208e, 0x0692c496,
                      0x069d222a, 0x06a6120e, 0x047a3fde]),
    DropData("$400", [0x043c364c, 0x0449181c, 0x0455cc9c, 0x045e99f4, 0x04677594, 0x048fb190,
                      0x049d3a60, 0x04aa1a7c, 0x04b68b24, 0x04c32928, 0x04cfbd68, 0x04da5770, 0x04e3280c, 0x04ee3338,
                      0x04f860ac, 0x05050980, 0x050f8eac, 0x051adec0, 0x0526c75c, 0x053f64a0, 0x054b2948, 0x05573dec,
                      0x0560fc1c, 0x056be960, 0x057519b4, 0x057e07b4, 0x05883f84, 0x05903654, 0x059bca40, 0x05a6eed4,
                      0x05af32e0, 0x0606f114, 0x060fdd48, 0x061a77cc, 0x062478d4, 0x063061c4, 0x063ab01c, 0x06471a44,
                      0x065094f8, 0x065918f4, 0x06621d44, 0x066b40cc, 0x06742ee4, 0x067d0d40, 0x06862090, 0x0692c498,
                      0x069d222c, 0x06a61210, 0x047a3fe0]),
    DropData("Meal ticket", [0x043c364e, 0x0449181e, 0x0455cc9e, 0x045e99f6, 0x04677596,
                             0x048fb192, 0x049d3a62, 0x04aa1a7e, 0x04b68b26, 0x04c3292a, 0x04cfbd6a, 0x04da5772,
                             0x04e3280e, 0x04ee333a, 0x04f860ae, 0x05050982, 0x050f8eae, 0x051adec2, 0x0526c75e,
                             0x053f64a2, 0x054b294a, 0x05573dee, 0x0560fc1e, 0x056be962, 0x057519b6, 0x057e07b6,
                             0x05883f86, 0x05903656, 0x059bca42, 0x05a6eed6, 0x05af32e2, 0x0606f116, 0x060fdd4a,
                             0x061a77ce, 0x062478d6, 0x063061c6, 0x063ab01e, 0x06471a46, 0x065094fa, 0x065918f6,
                             0x06621d46, 0x066b40ce, 0x06742ee6, 0x067d0d42, 0x06862092, 0x0692c49a, 0x069d222e,
                             0x06a61212, 0x047a3fe2])
]
