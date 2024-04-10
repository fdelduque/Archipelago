
class EnemyData:
    def __init__(self, name: str, enemy: str, addresses: list):
        self.name = name
        self.enemy = enemy
        self.addresses = addresses


Enemies = [
    EnemyData("Heart", "Global", [0x043c3612, 0x044917e2, 0x0455cc62, 0x045e99ba, 0x0467755a,
                                  0x048fb156, 0x049d3a26, 0x04aa1a42, 0x04b68aea, 0x04c328ee, 0x04cfbd2e, 0x04da5736,
                                  0x04e327d2, 0x04ee32fe, 0x04f86072, 0x05050946, 0x050f8e72, 0x051ade86, 0x0526c722,
                                  0x053f6466, 0x054b290e, 0x05573db2, 0x0560fbe2, 0x056be926, 0x0575197a, 0x057e077a,
                                  0x05883f4a, 0x0590361a, 0x059bca06, 0x05a6ee9a, 0x05af32a6, 0x0606f0da, 0x060fdd0e,
                                  0x061a7792, 0x0624789a, 0x0630618a, 0x063aafe2, 0x06471a0a, 0x065094be, 0x065918ba,
                                  0x06621d0a, 0x066b4092, 0x06742eaa, 0x067d0d06, 0x06862056, 0x0692c45e, 0x069d21f2,
                                  0x06a611d6, 0x047a3e76]),
    EnemyData("Heart", "Global", [0x043c362e, 0x044917fe, 0x0455cc7e, 0x045e99d6, 0x04677576,
                                  0x048fb172, 0x049d3a42, 0x04aa1a5e, 0x04b68b06, 0x04c3290a, 0x04cfbd4a, 0x04da5752,
                                  0x04e327ee, 0x04ee331a, 0x04f8608e, 0x05050962, 0x050f8e8e, 0x051adea2, 0x0526c73e,
                                  0x053f6482, 0x054b292a, 0x05573dce, 0x0560fbfe, 0x056be942, 0x05751996, 0x057e0796,
                                  0x05883f66, 0x05903636, 0x059bca22, 0x05a6eeb6, 0x05af32c2, 0x0606f0f6, 0x060fdd2a,
                                  0x061a77ae, 0x062478b6, 0x063061a6, 0x063aaffe, 0x06471a26, 0x065094da, 0x065918d6,
                                  0x06621d26, 0x066b40ae, 0x06742ec6, 0x067d0d22, 0x06862072, 0x0692c47a, 0x069d220e,
                                  0x06a611f2, 0x047a3fc2]),
    EnemyData("Heart", "Global", [0x043c3630, 0x04491800, 0x0455cc80, 0x045e99d8, 0x04677578,
                                  0x048fb174, 0x049d3a44, 0x04aa1a60, 0x04b68b08, 0x04c3290c, 0x04cfbd4c, 0x04da5754,
                                  0x04e327f0, 0x04ee331c, 0x04f86090, 0x05050964, 0x050f8e90, 0x051adea4, 0x0526c740,
                                  0x053f6484, 0x054b292c, 0x05573dd0, 0x0560fc00, 0x056be944, 0x05751998, 0x057e0798,
                                  0x05883f68, 0x05903638, 0x059bca24, 0x05a6eeb8, 0x05af32c4, 0x0606f0f8, 0x060fdd2c,
                                  0x061a77b0, 0x062478b8, 0x063061a8, 0x063ab000, 0x06471a28, 0x065094dc, 0x065918d8,
                                  0x06621d28, 0x066b40b0, 0x06742ec8, 0x067d0d24, 0x06862074, 0x0692c47c, 0x069d2210,
                                  0x06a611f4, 0x047a3fc4]),
    EnemyData("Heart", "Global", [0x043c3632, 0x04491802, 0x0455cc82, 0x045e99da, 0x0467757a,
                                  0x048fb176, 0x049d3a46, 0x04aa1a62, 0x04b68b0a, 0x04c3290e, 0x04cfbd4e, 0x04da5756,
                                  0x04e327f2, 0x04ee331e, 0x04f86092, 0x05050966, 0x050f8e92, 0x051adea6, 0x0526c742,
                                  0x053f6486, 0x054b292e, 0x05573dd2, 0x0560fc02, 0x056be946, 0x0575199a, 0x057e079a,
                                  0x05883f6a, 0x0590363a, 0x059bca26, 0x05a6eeba, 0x05af32c6, 0x0606f0fa, 0x060fdd2e,
                                  0x061a77b2, 0x062478ba, 0x063061aa, 0x063ab002, 0x06471a2a, 0x065094de, 0x065918da,
                                  0x06621d2a, 0x066b40b2, 0x06742eca, 0x067d0d26, 0x06862076, 0x0692c47e, 0x069d2212,
                                  0x06a611f6, 0x047a3fc6]),
    EnemyData("Heart", "Global", [0x043c3634, 0x04491804, 0x0455cc84, 0x045e99dc, 0x0467757c,
                                  0x048fb178, 0x049d3a48, 0x04aa1a64, 0x04b68b0c, 0x04c32910, 0x04cfbd50, 0x04da5758,
                                  0x04e327f4, 0x04ee3320, 0x04f86094, 0x05050968, 0x050f8e94, 0x051adea8, 0x0526c744,
                                  0x053f6488, 0x054b2930, 0x05573dd4, 0x0560fc04, 0x056be948, 0x0575199c, 0x057e079c,
                                  0x05883f6c, 0x0590363c, 0x059bca28, 0x05a6eebc, 0x05af32c8, 0x0606f0fc, 0x060fdd30,
                                  0x061a77b4, 0x062478bc, 0x063061ac, 0x063ab004, 0x06471a2c, 0x065094e0, 0x065918dc,
                                  0x06621d2c, 0x066b40b4, 0x06742ecc, 0x067d0d28, 0x06862078, 0x0692c480, 0x069d2214,
                                  0x06a611f8, 0x047a3fc8]),
    EnemyData("Heart", "Global", [0x043c3636, 0x04491806, 0x0455cc86, 0x045e99de, 0x0467757e,
                                  0x048fb17a, 0x049d3a4a, 0x04aa1a66, 0x04b68b0e, 0x04c32912, 0x04cfbd52, 0x04da575a,
                                  0x04e327f6, 0x04ee3322, 0x04f86096, 0x0505096a, 0x050f8e96, 0x051adeaa, 0x0526c746,
                                  0x053f648a, 0x054b2932, 0x05573dd6, 0x0560fc06, 0x056be94a, 0x0575199e, 0x057e079e,
                                  0x05883f6e, 0x0590363e, 0x059bca2a, 0x05a6eebe, 0x05af32ca, 0x0606f0fe, 0x060fdd32,
                                  0x061a77b6, 0x062478be, 0x063061ae, 0x063ab006, 0x06471a2e, 0x065094e2, 0x065918de,
                                  0x06621d2e, 0x066b40b6, 0x06742ece, 0x067d0d2a, 0x0686207a, 0x0692c482, 0x069d2216,
                                  0x06a611fa, 0x047a3fca]),
    EnemyData("Heart", "Global", [0x043c3638, 0x04491808, 0x0455cc88, 0x045e99e0, 0x04677580,
                                  0x048fb17c, 0x049d3a4c, 0x04aa1a68, 0x04b68b10, 0x04c32914, 0x04cfbd54, 0x04da575c,
                                  0x04e327f8, 0x04ee3324, 0x04f86098, 0x0505096c, 0x050f8e98, 0x051adeac, 0x0526c748,
                                  0x053f648c, 0x054b2934, 0x05573dd8, 0x0560fc08, 0x056be94c, 0x057519a0, 0x057e07a0,
                                  0x05883f70, 0x05903640, 0x059bca2c, 0x05a6eec0, 0x05af32cc, 0x0606f100, 0x060fdd34,
                                  0x061a77b8, 0x062478c0, 0x063061b0, 0x063ab008, 0x06471a30, 0x065094e4, 0x065918e0,
                                  0x06621d30, 0x066b40b8, 0x06742ed0, 0x067d0d2c, 0x0686207c, 0x0692c484, 0x069d2218,
                                  0x06a611fc, 0x047a3fcc]),
    EnemyData("Heart", "Global", [0x043c363a, 0x0449180a, 0x0455cc8a, 0x045e99e2, 0x04677582,
                                  0x048fb17e, 0x049d3a4e, 0x04aa1a6a, 0x04b68b12, 0x04c32916, 0x04cfbd56, 0x04da575e,
                                  0x04e327fa, 0x04ee3326, 0x04f8609a, 0x0505096e, 0x050f8e9a, 0x051adeae, 0x0526c74a,
                                  0x053f648e, 0x054b2936, 0x05573dda, 0x0560fc0a, 0x056be94e, 0x057519a2, 0x057e07a2,
                                  0x05883f72, 0x05903642, 0x059bca2e, 0x05a6eec2, 0x05af32ce, 0x0606f102, 0x060fdd36,
                                  0x061a77ba, 0x062478c2, 0x063061b2, 0x063ab00a, 0x06471a32, 0x065094e6, 0x065918e2,
                                  0x06621d32, 0x066b40ba, 0x06742ed2, 0x067d0d2e, 0x0686207e, 0x0692c486, 0x069d221a,
                                  0x06a611fe, 0x047a3fce]),
    EnemyData("Heart", "Global", [0x043c363c, 0x0449180c, 0x0455cc8c, 0x045e99e4, 0x04677584,
                                  0x048fb180, 0x049d3a50, 0x04aa1a6c, 0x04b68b14, 0x04c32918, 0x04cfbd58, 0x04da5760,
                                  0x04e327fc, 0x04ee3328, 0x04f8609c, 0x05050970, 0x050f8e9c, 0x051adeb0, 0x0526c74c,
                                  0x053f6490, 0x054b2938, 0x05573ddc, 0x0560fc0c, 0x056be950, 0x057519a4, 0x057e07a4,
                                  0x05883f74, 0x05903644, 0x059bca30, 0x05a6eec4, 0x05af32d0, 0x0606f104, 0x060fdd38,
                                  0x061a77bc, 0x062478c4, 0x063061b4, 0x063ab00c, 0x06471a34, 0x065094e8, 0x065918e4,
                                  0x06621d34, 0x066b40bc, 0x06742ed4, 0x067d0d30, 0x06862080, 0x0692c488, 0x069d221c,
                                  0x06a61200, 0x047a3fd0]),
    EnemyData("Heart", "Global", [0x043c363e, 0x0449180e, 0x0455cc8e, 0x045e99e6, 0x04677586,
                                  0x048fb182, 0x049d3a52, 0x04aa1a6e, 0x04b68b16, 0x04c3291a, 0x04cfbd5a, 0x04da5762,
                                  0x04e327fe, 0x04ee332a, 0x04f8609e, 0x05050972, 0x050f8e9e, 0x051adeb2, 0x0526c74e,
                                  0x053f6492, 0x054b293a, 0x05573dde, 0x0560fc0e, 0x056be952, 0x057519a6, 0x057e07a6,
                                  0x05883f76, 0x05903646, 0x059bca32, 0x05a6eec6, 0x05af32d2, 0x0606f106, 0x060fdd3a,
                                  0x061a77be, 0x062478c6, 0x063061b6, 0x063ab00e, 0x06471a36, 0x065094ea, 0x065918e6,
                                  0x06621d36, 0x066b40be, 0x06742ed6, 0x067d0d32, 0x06862082, 0x0692c48a, 0x069d221e,
                                  0x06a61202, 0x047a3fd2]),
    EnemyData("Heart", "Global", [0x043c3640, 0x04491810, 0x0455cc90, 0x045e99e8, 0x04677588,
                                  0x048fb184, 0x049d3a54, 0x04aa1a70, 0x04b68b18, 0x04c3291c, 0x04cfbd5c, 0x04da5764,
                                  0x04e32800, 0x04ee332c, 0x04f860a0, 0x05050974, 0x050f8ea0, 0x051adeb4, 0x0526c750,
                                  0x053f6494, 0x054b293c, 0x05573de0, 0x0560fc10, 0x056be954, 0x057519a8, 0x057e07a8,
                                  0x05883f78, 0x05903648, 0x059bca34, 0x05a6eec8, 0x05af32d4, 0x0606f108, 0x060fdd3c,
                                  0x061a77c0, 0x062478c8, 0x063061b8, 0x063ab010, 0x06471a38, 0x065094ec, 0x065918e8,
                                  0x06621d38, 0x066b40c0, 0x06742ed8, 0x067d0d34, 0x06862084, 0x0692c48c, 0x069d2220,
                                  0x06a61204, 0x047a3fd4]),
    EnemyData("Heart", "Global", [0x043c3642, 0x04491812, 0x0455cc92, 0x045e99ea, 0x0467758a,
                                  0x048fb186, 0x049d3a56, 0x04aa1a72, 0x04b68b1a, 0x04c3291e, 0x04cfbd5e, 0x04da5766,
                                  0x04e32802, 0x04ee332e, 0x04f860a2, 0x05050976, 0x050f8ea2, 0x051adeb6, 0x0526c752,
                                  0x053f6496, 0x054b293e, 0x05573de2, 0x0560fc12, 0x056be956, 0x057519aa, 0x057e07aa,
                                  0x05883f7a, 0x0590364a, 0x059bca36, 0x05a6eeca, 0x05af32d6, 0x0606f10a, 0x060fdd3e,
                                  0x061a77c2, 0x062478ca, 0x063061ba, 0x063ab012, 0x06471a3a, 0x065094ee, 0x065918ea,
                                  0x06621d3a, 0x066b40c2, 0x06742eda, 0x067d0d36, 0x06862086, 0x0692c48e, 0x069d2222,
                                  0x06a61206, 0x047a3fd6]),
    EnemyData("Big heart", "Global", [0x043c3644, 0x04491814, 0x0455cc94, 0x045e99ec, 0x0467758c,
                                      0x048fb188, 0x049d3a58, 0x04aa1a74, 0x04b68b1c, 0x04c32920, 0x04cfbd60,
                                      0x04da5768, 0x04e32804, 0x04ee3330, 0x04f860a4, 0x05050978, 0x050f8ea4,
                                      0x051adeb8, 0x0526c754, 0x053f6498, 0x054b2940, 0x05573de4, 0x0560fc14,
                                      0x056be958, 0x057519ac, 0x057e07ac, 0x05883f7c, 0x0590364c, 0x059bca38,
                                      0x05a6eecc, 0x05af32d8, 0x0606f10c, 0x060fdd40, 0x061a77c4, 0x062478cc,
                                      0x063061bc, 0x063ab014, 0x06471a3c, 0x065094f0, 0x065918ec, 0x06621d3c,
                                      0x066b40c4, 0x06742edc, 0x067d0d38, 0x06862088, 0x0692c490, 0x069d2224,
                                      0x06a61208, 0x047a3fd8]),
    EnemyData("Big heart", "Global", [0x043c3646, 0x04491816, 0x0455cc96, 0x045e99ee, 0x0467758e,
                                      0x048fb18a, 0x049d3a5a, 0x04aa1a76, 0x04b68b1e, 0x04c32922, 0x04cfbd62,
                                      0x04da576a, 0x04e32806, 0x04ee3332, 0x04f860a6, 0x0505097a, 0x050f8ea6,
                                      0x051adeba, 0x0526c756, 0x053f649a, 0x054b2942, 0x05573de6, 0x0560fc16,
                                      0x056be95a, 0x057519ae, 0x057e07ae, 0x05883f7e, 0x0590364e, 0x059bca3a,
                                      0x05a6eece, 0x05af32da, 0x0606f10e, 0x060fdd42, 0x061a77c6, 0x062478ce,
                                      0x063061be, 0x063ab016, 0x06471a3e, 0x065094f2, 0x065918ee, 0x06621d3e,
                                      0x066b40c6, 0x06742ede, 0x067d0d3a, 0x0686208a, 0x0692c492, 0x069d2226,
                                      0x06a6120a, 0x047a3fda]),
    EnemyData("$1", "Global", [0x043c3614, 0x044917e4, 0x0455cc64, 0x045e99bc, 0x0467755c,
                               0x048fb158, 0x049d3a28, 0x04aa1a44, 0x04b68aec, 0x04c328f0, 0x04cfbd30, 0x04da5738,
                               0x04e327d4, 0x04ee3300, 0x04f86074, 0x05050948, 0x050f8e74, 0x051ade88, 0x0526c724,
                               0x053f6468, 0x054b2910, 0x05573db4, 0x0560fbe4, 0x056be928, 0x0575197c, 0x057e077c,
                               0x05883f4c, 0x0590361c, 0x059bca08, 0x05a6ee9c, 0x05af32a8, 0x0606f0dc, 0x060fdd10,
                               0x061a7794, 0x0624789c, 0x0630618c, 0x063aafe4, 0x06471a0c, 0x065094c0, 0x065918bc,
                               0x06621d0c, 0x066b4094, 0x06742eac, 0x067d0d08, 0x06862058, 0x0692c460, 0x069d21f4,
                               0x06a611d8, 0x047a3fa8]),
    EnemyData("$1", "Global", [0x043c3648, 0x04491818, 0x0455cc98, 0x045e99f0, 0x04677590,
                               0x048fb18c, 0x049d3a5c, 0x04aa1a78, 0x04b68b20, 0x04c32924, 0x04cfbd64, 0x04da576c,
                               0x04e32808, 0x04ee3334, 0x04f860a8, 0x0505097c, 0x050f8ea8, 0x051adebc, 0x0526c758,
                               0x053f649c, 0x054b2944, 0x05573de8, 0x0560fc18, 0x056be95c, 0x057519b0, 0x057e07b0,
                               0x05883f80, 0x05903650, 0x059bca3c, 0x05a6eed0, 0x05af32dc, 0x0606f110, 0x060fdd44,
                               0x061a77c8, 0x062478d0, 0x063061c0, 0x063ab018, 0x06471a40, 0x065094f4, 0x065918f0,
                               0x06621d40, 0x066b40c8, 0x06742ee0, 0x067d0d3c, 0x0686208c, 0x0692c494, 0x069d2228,
                               0x06a6120c, 0x047a3fdc]),
    EnemyData("$25", "Global", [0x043c3610, 0x044917e0, 0x0455cc60, 0x045e99b8, 0x04677558,
                                0x048fb154, 0x049d3a24, 0x04aa1a40, 0x04b68ae8, 0x04c328ec, 0x04cfbd2c, 0x04da5734,
                                0x04e327d0, 0x04ee32fc, 0x04f86070, 0x05050944, 0x050f8e70, 0x051ade84, 0x0526c720,
                                0x053f6464, 0x054b290c, 0x05573db0, 0x0560fbe0, 0x056be924, 0x05751978, 0x057e0778,
                                0x05883f48, 0x05903618, 0x059bca04, 0x05a6ee98, 0x05af32a4, 0x0606f0d8, 0x060fdd0c,
                                0x061a7790, 0x06247898, 0x06306188, 0x063aafe0, 0x06471a08, 0x065094bc, 0x065918b8,
                                0x06621d08, 0x066b4090, 0x06742ea8, 0x067d0d04, 0x06862054, 0x0692c45c, 0x069d21f0,
                                0x06a611d4, 0x047a3e74]),
    EnemyData("$25", "Global", [0x043c3616, 0x044917e6, 0x0455cc66, 0x045e99be, 0x0467755e,
                                0x048fb15a, 0x049d3a2a, 0x04aa1a46, 0x04b68aee, 0x04c328f2, 0x04cfbd32, 0x04da573a,
                                0x04e327d6, 0x04ee3302, 0x04f86076, 0x0505094a, 0x050f8e76, 0x051ade8a, 0x0526c726,
                                0x053f646a, 0x054b2912, 0x05573db6, 0x0560fbe6, 0x056be92a, 0x0575197e, 0x057e077e,
                                0x05883f4e, 0x0590361e, 0x059bca0a, 0x05a6ee9e, 0x05af32aa, 0x0606f0de, 0x060fdd12,
                                0x061a7796, 0x0624789e, 0x0630618e, 0x063aafe6, 0x06471a0e, 0x065094c2, 0x065918be,
                                0x06621d0e, 0x066b4096, 0x06742eae, 0x067d0d0a, 0x0686205a, 0x0692c462, 0x069d21f6,
                                0x06a611da, 0x047a3faa]),
    EnemyData("$25", "Global", [0x043c3618, 0x044917e8, 0x0455cc68, 0x045e99c0, 0x04677560,
                                0x048fb15c, 0x049d3a2c, 0x04aa1a48, 0x04b68af0, 0x04c328f4, 0x04cfbd34, 0x04da573c,
                                0x04e327d8, 0x04ee3304, 0x04f86078, 0x0505094c, 0x050f8e78, 0x051ade8c, 0x0526c728,
                                0x053f646c, 0x054b2914, 0x05573db8, 0x0560fbe8, 0x056be92c, 0x05751980, 0x057e0780,
                                0x05883f50, 0x05903620, 0x059bca0c, 0x05a6eea0, 0x05af32ac, 0x0606f0e0, 0x060fdd14,
                                0x061a7798, 0x062478a0, 0x06306190, 0x063aafe8, 0x06471a10, 0x065094c4, 0x065918c0,
                                0x06621d10, 0x066b4098, 0x06742eb0, 0x067d0d0c, 0x0686205c, 0x0692c464, 0x069d21f8,
                                0x06a611dc, 0x047a3fac]),
    EnemyData("$25", "Global", [0x043c361a, 0x044917ea, 0x0455cc6a, 0x045e99c2, 0x04677562,
                                0x048fb15e, 0x049d3a2e, 0x04aa1a4a, 0x04b68af2, 0x04c328f6, 0x04cfbd36, 0x04da573e,
                                0x04e327da, 0x04ee3306, 0x04f8607a, 0x0505094e, 0x050f8e7a, 0x051ade8e, 0x0526c72a,
                                0x053f646e, 0x054b2916, 0x05573dba, 0x0560fbea, 0x056be92e, 0x05751982, 0x057e0782,
                                0x05883f52, 0x05903622, 0x059bca0e, 0x05a6eea2, 0x05af32ae, 0x0606f0e2, 0x060fdd16,
                                0x061a779a, 0x062478a2, 0x06306192, 0x063aafea, 0x06471a12, 0x065094c6, 0x065918c2,
                                0x06621d12, 0x066b409a, 0x06742eb2, 0x067d0d0e, 0x0686205e, 0x0692c466, 0x069d21fa,
                                0x06a611de, 0x047a3fae]),
    EnemyData("$25", "Global", [0x043c361c, 0x044917ec, 0x0455cc6c, 0x045e99c4, 0x04677564,
                                0x048fb160, 0x049d3a30, 0x04aa1a4c, 0x04b68af4, 0x04c328f8, 0x04cfbd38, 0x04da5740,
                                0x04e327dc, 0x04ee3308, 0x04f8607c, 0x05050950, 0x050f8e7c, 0x051ade90, 0x0526c72c,
                                0x053f6470, 0x054b2918, 0x05573dbc, 0x0560fbec, 0x056be930, 0x05751984, 0x057e0784,
                                0x05883f54, 0x05903624, 0x059bca10, 0x05a6eea4, 0x05af32b0, 0x0606f0e4, 0x060fdd18,
                                0x061a779c, 0x062478a4, 0x06306194, 0x063aafec, 0x06471a14, 0x065094c8, 0x065918c4,
                                0x06621d14, 0x066b409c, 0x06742eb4, 0x067d0d10, 0x06862060, 0x0692c468, 0x069d21fc,
                                0x06a611e0, 0x047a3fb0]),
    EnemyData("$25", "Global", [0x043c361e, 0x044917ee, 0x0455cc6e, 0x045e99c6, 0x04677566,
                                0x048fb162, 0x049d3a32, 0x04aa1a4e, 0x04b68af6, 0x04c328fa, 0x04cfbd3a, 0x04da5742,
                                0x04e327de, 0x04ee330a, 0x04f8607e, 0x05050952, 0x050f8e7e, 0x051ade92, 0x0526c72e,
                                0x053f6472, 0x054b291a, 0x05573dbe, 0x0560fbee, 0x056be932, 0x05751986, 0x057e0786,
                                0x05883f56, 0x05903626, 0x059bca12, 0x05a6eea6, 0x05af32b2, 0x0606f0e6, 0x060fdd1a,
                                0x061a779e, 0x062478a6, 0x06306196, 0x063aafee, 0x06471a16, 0x065094ca, 0x065918c6,
                                0x06621d16, 0x066b409e, 0x06742eb6, 0x067d0d12, 0x06862062, 0x0692c46a, 0x069d21fe,
                                0x06a611e2, 0x047a3fb2]),
    EnemyData("$25", "Global", [0x043c3620, 0x044917f0, 0x0455cc70, 0x045e99c8, 0x04677568,
                                0x048fb164, 0x049d3a34, 0x04aa1a50, 0x04b68af8, 0x04c328fc, 0x04cfbd3c, 0x04da5744,
                                0x04e327e0, 0x04ee330c, 0x04f86080, 0x05050954, 0x050f8e80, 0x051ade94, 0x0526c730,
                                0x053f6474, 0x054b291c, 0x05573dc0, 0x0560fbf0, 0x056be934, 0x05751988, 0x057e0788,
                                0x05883f58, 0x05903628, 0x059bca14, 0x05a6eea8, 0x05af32b4, 0x0606f0e8, 0x060fdd1c,
                                0x061a77a0, 0x062478a8, 0x06306198, 0x063aaff0, 0x06471a18, 0x065094cc, 0x065918c8,
                                0x06621d18, 0x066b40a0, 0x06742eb8, 0x067d0d14, 0x06862064, 0x0692c46c, 0x069d2200,
                                0x06a611e4, 0x047a3fb4]),
    EnemyData("$50", "Global", [0x043c3622, 0x044917f2, 0x0455cc72, 0x045e99ca, 0x0467756a,
                                0x048fb166, 0x049d3a36, 0x04aa1a52, 0x04b68afa, 0x04c328fe, 0x04cfbd3e, 0x04da5746,
                                0x04e327e2, 0x04ee330e, 0x04f86082, 0x05050956, 0x050f8e82, 0x051ade96, 0x0526c732,
                                0x053f6476, 0x054b291e, 0x05573dc2, 0x0560fbf2, 0x056be936, 0x0575198a, 0x057e078a,
                                0x05883f5a, 0x0590362a, 0x059bca16, 0x05a6eeaa, 0x05af32b6, 0x0606f0ea, 0x060fdd1e,
                                0x061a77a2, 0x062478aa, 0x0630619a, 0x063aaff2, 0x06471a1a, 0x065094ce, 0x065918ca,
                                0x06621d1a, 0x066b40a2, 0x06742eba, 0x067d0d16, 0x06862066, 0x0692c46e, 0x069d2202,
                                0x06a611e6, 0x047a3fb6]),
    EnemyData("$50", "Global", [0x043c3624, 0x044917f4, 0x0455cc74, 0x045e99cc, 0x0467756c,
                                0x048fb168, 0x049d3a38, 0x04aa1a54, 0x04b68afc, 0x04c32900, 0x04cfbd40, 0x04da5748,
                                0x04e327e4, 0x04ee3310, 0x04f86084, 0x05050958, 0x050f8e84, 0x051ade98, 0x0526c734,
                                0x053f6478, 0x054b2920, 0x05573dc4, 0x0560fbf4, 0x056be938, 0x0575198c, 0x057e078c,
                                0x05883f5c, 0x0590362c, 0x059bca18, 0x05a6eeac, 0x05af32b8, 0x0606f0ec, 0x060fdd20,
                                0x061a77a4, 0x062478ac, 0x0630619c, 0x063aaff4, 0x06471a1c, 0x065094d0, 0x065918cc,
                                0x06621d1c, 0x066b40a4, 0x06742ebc, 0x067d0d18, 0x06862068, 0x0692c470, 0x069d2204,
                                0x06a611e8, 0x047a3fb8]),
    EnemyData("$50", "Global", [0x043c3626, 0x044917f6, 0x0455cc76, 0x045e99ce, 0x0467756e,
                                0x048fb16a, 0x049d3a3a, 0x04aa1a56, 0x04b68afe, 0x04c32902, 0x04cfbd42, 0x04da574a,
                                0x04e327e6, 0x04ee3312, 0x04f86086, 0x0505095a, 0x050f8e86, 0x051ade9a, 0x0526c736,
                                0x053f647a, 0x054b2922, 0x05573dc6, 0x0560fbf6, 0x056be93a, 0x0575198e, 0x057e078e,
                                0x05883f5e, 0x0590362e, 0x059bca1a, 0x05a6eeae, 0x05af32ba, 0x0606f0ee, 0x060fdd22,
                                0x061a77a6, 0x062478ae, 0x0630619e, 0x063aaff6, 0x06471a1e, 0x065094d2, 0x065918ce,
                                0x06621d1e, 0x066b40a6, 0x06742ebe, 0x067d0d1a, 0x0686206a, 0x0692c472, 0x069d2206,
                                0x06a611ea, 0x047a3fba]),
    EnemyData("$50", "Global", [0x043c3628, 0x044917f8, 0x0455cc78, 0x045e99d0, 0x04677570,
                                0x048fb16c, 0x049d3a3c, 0x04aa1a58, 0x04b68b00, 0x04c32904, 0x04cfbd44, 0x04da574c,
                                0x04e327e8, 0x04ee3314, 0x04f86088, 0x0505095c, 0x050f8e88, 0x051ade9c, 0x0526c738,
                                0x053f647c, 0x054b2924, 0x05573dc8, 0x0560fbf8, 0x056be93c, 0x05751990, 0x057e0790,
                                0x05883f60, 0x05903630, 0x059bca1c, 0x05a6eeb0, 0x05af32bc, 0x0606f0f0, 0x060fdd24,
                                0x061a77a8, 0x062478b0, 0x063061a0, 0x063aaff8, 0x06471a20, 0x065094d4, 0x065918d0,
                                0x06621d20, 0x066b40a8, 0x06742ec0, 0x067d0d1c, 0x0686206c, 0x0692c474, 0x069d2208,
                                0x06a611ec, 0x047a3fbc]),
    EnemyData("$100", "Global", [0x043c362a, 0x044917fa, 0x0455cc7a, 0x045e99d2, 0x04677572,
                                 0x048fb16e, 0x049d3a3e, 0x04aa1a5a, 0x04b68b02, 0x04c32906, 0x04cfbd46, 0x04da574e,
                                 0x04e327ea, 0x04ee3316, 0x04f8608a, 0x0505095e, 0x050f8e8a, 0x051ade9e, 0x0526c73a,
                                 0x053f647e, 0x054b2926, 0x05573dca, 0x0560fbfa, 0x056be93e, 0x05751992, 0x057e0792,
                                 0x05883f62, 0x05903632, 0x059bca1e, 0x05a6eeb2, 0x05af32be, 0x0606f0f2, 0x060fdd26,
                                 0x061a77aa, 0x062478b2, 0x063061a2, 0x063aaffa, 0x06471a22, 0x065094d6, 0x065918d2,
                                 0x06621d22, 0x066b40aa, 0x06742ec2, 0x067d0d1e, 0x0686206e, 0x0692c476, 0x069d220a,
                                 0x06a611ee, 0x047a3fbe]),
    EnemyData("$100", "Global", [0x043c362c, 0x044917fc, 0x0455cc7c, 0x045e99d4, 0x04677574,
                                 0x048fb170, 0x049d3a40, 0x04aa1a5c, 0x04b68b04, 0x04c32908, 0x04cfbd48, 0x04da5750,
                                 0x04e327ec, 0x04ee3318, 0x04f8608c, 0x05050960, 0x050f8e8c, 0x051adea0, 0x0526c73c,
                                 0x053f6480, 0x054b2928, 0x05573dcc, 0x0560fbfc, 0x056be940, 0x05751994, 0x057e0794,
                                 0x05883f64, 0x05903634, 0x059bca20, 0x05a6eeb4, 0x05af32c0, 0x0606f0f4, 0x060fdd28,
                                 0x061a77ac, 0x062478b4, 0x063061a4, 0x063aaffc, 0x06471a24, 0x065094d8, 0x065918d4,
                                 0x06621d24, 0x066b40ac, 0x06742ec4, 0x067d0d20, 0x06862070, 0x0692c478, 0x069d220c,
                                 0x06a611f0, 0x047a3fc0]),
    EnemyData("$100", "Zombie", [0x0b6c04]),
    EnemyData("$250", "Global", [0x043c364a, 0x0449181a, 0x0455cc9a, 0x045e99f2, 0x04677592,
                                 0x048fb18e, 0x049d3a5e, 0x04aa1a7a, 0x04b68b22, 0x04c32926, 0x04cfbd66, 0x04da576e,
                                 0x04e3280a, 0x04ee3336, 0x04f860aa, 0x0505097e, 0x050f8eaa, 0x051adebe, 0x0526c75a,
                                 0x053f649e, 0x054b2946, 0x05573dea, 0x0560fc1a, 0x056be95e, 0x057519b2, 0x057e07b2,
                                 0x05883f82, 0x05903652, 0x059bca3e, 0x05a6eed2, 0x05af32de, 0x0606f112, 0x060fdd46,
                                 0x061a77ca, 0x062478d2, 0x063061c2, 0x063ab01a, 0x06471a42, 0x065094f6, 0x065918f2,
                                 0x06621d42, 0x066b40ca, 0x06742ee2, 0x067d0d3e, 0x0686208e, 0x0692c496, 0x069d222a,
                                 0x06a6120e, 0x047a3fde]),
    EnemyData("$400", "Global", [0x043c364c, 0x0449181c, 0x0455cc9c, 0x045e99f4, 0x04677594,
                                 0x048fb190, 0x049d3a60, 0x04aa1a7c, 0x04b68b24, 0x04c32928, 0x04cfbd68, 0x04da5770,
                                 0x04e3280c, 0x04ee3338, 0x04f860ac, 0x05050980, 0x050f8eac, 0x051adec0, 0x0526c75c,
                                 0x053f64a0, 0x054b2948, 0x05573dec, 0x0560fc1c, 0x056be960, 0x057519b4, 0x057e07b4,
                                 0x05883f84, 0x05903654, 0x059bca40, 0x05a6eed4, 0x05af32e0, 0x0606f114, 0x060fdd48,
                                 0x061a77cc, 0x062478d4, 0x063061c4, 0x063ab01c, 0x06471a44, 0x065094f8, 0x065918f4,
                                 0x06621d44, 0x066b40cc, 0x06742ee4, 0x067d0d40, 0x06862090, 0x0692c498, 0x069d222c,
                                 0x06a61210, 0x047a3fe0]),
    EnemyData("$400", "Ghost", [0x0b7464]),
    EnemyData("$400", "Blade Soldier", [0x0b6e34]),
    EnemyData("$400", "Bone Archer", [0x0b6bb4]),
    EnemyData("$1000", "Spellbook", [0x0b859c]),
    EnemyData("Axe", "Axe Knight", [0x0b83a4]),
    EnemyData("Axe", "Axe Knight", [0x0b5964]),
    EnemyData("Monster vial 1", "Merman", [0x0b5caa]),
    EnemyData("Monster vial 1", "Merman", [0x0b5cfa]),
    EnemyData("Monster vial 2", "Bat", [0x0b63a2]),
    EnemyData("Monster vial 3", "Skeleton",[0x0b655a]),
    EnemyData("Monster vial 3", "Bone Ark", [0x0b60ac]),
    EnemyData("Monster vial 3", "Yorick", [0x0b6d94]),
    EnemyData("Monster vial 3", "Nova Skeleton", [0x0b6e84]),
    EnemyData("Leather shield", "Slinger", [0x0b77d4]),
    EnemyData("Leather shield", "Stone Rose", [0x0b66ec]),
    EnemyData("Knight shield", "Slinger", [0x0b77d2]),
    EnemyData("Knight shield", "Shield", [0x0b70b4]),
    EnemyData("Iron shield", "Winged Guard", [0x0b6ed4]),
    EnemyData("AxeLord shield", "Axe Knight", [0x0b5962]),
    EnemyData("Dark shield", "Malachi", [0x0b8214]),
    EnemyData("Medusa shield", "Medusa Head", [0x0b8eea]),
    EnemyData("Medusa shield", "Medusa Head", [0x0b8f12]),
    EnemyData("Skull shield", "Skull Lord", [0x0b872a]),
    EnemyData("Skull shield", "Bone Ark", [0x0b60aa]),
    EnemyData("Skull shield", "Yorick", [0x0b6d92]),
    EnemyData("Fire shield", "Fire Demon", [0x0b65fc]),
    EnemyData("Basilard", "Bloody Zombie", [0x0b5a7a]),
    EnemyData("Short sword", "Bone Scimitar", [0x0b6b3c]),
    EnemyData("Combat knife", "Gurkha", [0x0b7964]),
    EnemyData("Were bane", "Hunting Girl", [0x0b80ac]),
    EnemyData("Rapier", "Armor Lord", [0x0b5dc4]),
    EnemyData("Rapier", "Dhuron", [0x0b71a2]),
    EnemyData("Karma coin", "Orobourous", [0x0b70dc]),
    EnemyData("Karma coin", "Fire Warg", [0x0b7322]),
    EnemyData("Magic missile", "Bone Musket", [0x0b6ac4]),
    EnemyData("Magic missile", "Bone Archer", [0x0b6bb2]),
    EnemyData("Magic missile", "Sniper of Goth", [0x0b7a7c]),
    EnemyData("Red rust", "Bone Scimitar", [0x0b6b3a]),
    EnemyData("Takemitsu", "Flea Man", [0x0b5eb4]),
    EnemyData("Takemitsu", "Puppet sword", [0x0b703c]),
    EnemyData("Shotel", "Blade Master", [0x0b6de4]),
    EnemyData("Apple", "Harpy", [0x0b828c]),
    EnemyData("Banana", "Skeleton Ape", [0x0b669c]),
    EnemyData("Grapes", "Thornweed", [0x0b748c]),
    EnemyData("Strawberry", "Thornweed", [0x0b748a]),
    EnemyData("Cheesecake", "Hunting Girl", [0x0b80aa]),
    EnemyData("Shortcake", "Salem Witch", [0x0b7fba]),
    EnemyData("Tart", "Diplocephalus", [0x0b5af2]),
    EnemyData("Ice cream", "Frozen Shade", [0x0b6a4a]),
    EnemyData("Frankfurter", "Flying Zombie", [0x0b5aa2]),
    EnemyData("Pizza", "Toad", [0x0b6b62]),
    EnemyData("Pizza", "Frog", [0x0b6b8a]),
    EnemyData("Cheese", "Flea Man", [0x0b5eb2]),
    EnemyData("Ham and eggs", "Flea Rider", [0x0b6122]),
    EnemyData("Ham and eggs", "Bone Halberd", [0x0b6d42]),
    EnemyData("Morning set", "Ouija Table", [0x0b7a2a]),
    EnemyData("Lunch A", "Tin man", [0x0b87a4]),
    EnemyData("Barley tea", "Ouija Table", [0x0b7a2c]),
    EnemyData("Green tea", "Tombstone", [0x0b6c7a]),
    EnemyData("Green tea", "Dark Octopus", [0x0b5e62]),
    EnemyData("Natou", "Grave Keeper", [0x0b6c2a]),
    EnemyData("Ramen", "Schmoo", [0x0b920c]),
    EnemyData("Miso soup", "Grave Keeper", [0x0b6c2c]),
    EnemyData("Sushi", "Killer Fish", [0x0b9642]),
    EnemyData("Sushi", "Dark Octopus", [0x0b5e64]),
    EnemyData("Pork bun", "Blue Raven", [0x0b6ca2]),
    EnemyData("Red bean bun", "Black Crow", [0x0b6cca]),
    EnemyData("Pot roast", "Flail Guard", [0x0b6442]),
    EnemyData("Sirloin", "Lossoth", [0x0b6f4c]),
    EnemyData("Sirloin", "Minotaur", [0x0b9d14]),
    EnemyData("Turkey", "Flea Rider", [0x0b6124]),
    EnemyData("Meal ticket", "Global", [0x043c364e, 0x0449181e, 0x0455cc9e, 0x045e99f6,
                                        0x04677596, 0x048fb192, 0x049d3a62, 0x04aa1a7e, 0x04b68b26, 0x04c3292a,
                                        0x04cfbd6a, 0x04da5772, 0x04e3280e, 0x04ee333a, 0x04f860ae, 0x05050982,
                                        0x050f8eae, 0x051adec2, 0x0526c75e, 0x053f64a2, 0x054b294a, 0x05573dee,
                                        0x0560fc1e, 0x056be962, 0x057519b6, 0x057e07b6, 0x05883f86, 0x05903656,
                                        0x059bca42, 0x05a6eed6, 0x05af32e2, 0x0606f116, 0x060fdd4a, 0x061a77ce,
                                        0x062478d6, 0x063061c6, 0x063ab01e, 0x06471a46, 0x065094fa, 0x065918f6,
                                        0x06621d46, 0x066b40ce, 0x06742ee6, 0x067d0d42, 0x06862092, 0x0692c49a,
                                        0x069d222e, 0x06a61212, 0x047a3fe2]),
    EnemyData("Meal ticket", "Stone Rose", [0x0b66ea]),
    EnemyData("Meal ticket", "Black Panther", [0x0b5e3c]),
    EnemyData("Neutron bomb", "Plate Lord", [0x0b69fa]),
    EnemyData("Neutron bomb", "Cave Troll", [0x0b73ec]),
    EnemyData("Pentagram", "Diplocephalus", [0x0b5af4]),
    EnemyData("Pentagram", "Ctulhu", [0x0b819c]),
    EnemyData("Pentagram", "Spellbook", [0x0b83ca]),
    EnemyData("Bat pentagram", "Ctulhu", [0x0b819a]),
    EnemyData("Shuriken", "Flying Zombie", [0x0b5aa4]),
    EnemyData("Shuriken", "Jack O'Bones", [0x0b6cf4]),
    EnemyData("Cross shuriken", "Blade Master", [0x0b6de2]),
    EnemyData("Buffalo star", "Ghost Dancer", [0x0b7ef4]),
    EnemyData("Flame star", "Jack O'Bones", [0x0b6cf2]),
    EnemyData("TNT", "Skeleton Ape", [0x0b669a]),
    EnemyData("TNT", "Bomb Knight", [0x0b75cc]),
    EnemyData("Bwaka knife", "Poltergeist", [0x0b6f24]),
    EnemyData("Boomerang", "Skelerang", [0x0b5a2c]),
    EnemyData("Javelin", "Spear Guard", [0x0b682c]),
    EnemyData("Javelin", "Winged Guard", [0x0b6ed2]),
    EnemyData("Javelin", "Bone Halberd", [0x0b6d44]),
    EnemyData("Javelin", "Scarecrow", [0x0b91e4]),
    EnemyData("Javelin", "Spear", [0x0b708c]),
    EnemyData("Namakura", "Blade Soldier", [0x0b6e32]),
    EnemyData("Knuckle duster", "Frog", [0x0b6b8c]),
    EnemyData("Scimitar", "Skull Lord", [0x0b872c]),
    EnemyData("Cutlass", "Sword Lord", [0x0b59dc]),
    EnemyData("Cutlass", "Corner Guard", [0x0b7824]),
    EnemyData("Cutlass", "Owl Knight", [0x0b5b94]),
    EnemyData("Saber", "Armor Lord", [0x0b5dc2]),
    EnemyData("Saber", "Magic Tome", [0x0b859a]),
    EnemyData("Broadsword", "Spectral Sword", [0x0b6efc]),
    EnemyData("Broadsword", "Spectral Sword", [0x0b7014]),
    EnemyData("Bekatowa", "Sword Lord", [0x0b59da]),
    EnemyData("Damascus sword", "Corner Guard", [0x0b7822]),
    EnemyData("Hunter sword", "Blade", [0x0b79b4]),
    EnemyData("Estoc", "Valhalla Knight", [0x0b6f9c]),
    EnemyData("Bastard sword", "Spectral Sword", [0x0b6efa]),
    EnemyData("Bastard sword", "Spectral Sword", [0x0b7012]),
    EnemyData("Jewel knuckles", "Rock Knight", [0x0b761c]),
    EnemyData("Claymore", "Valhalla Knight", [0x0b6f9a]),
    EnemyData("Katana", "Tombstone", [0x0b6c7c]),
    EnemyData("Flamberge", "Cloaked knight", [0x0b88bc]),
    EnemyData("Iron fist", "Werewolf", [0x0b9d8c]),
    EnemyData("Zwei hander", "Blue Venus Weed", [0x0b9e04, 0x0b9e2c]),
    EnemyData("Obsidian sword", "Lesser Demon", [0x0b5c0c]),
    EnemyData("Jewel sword", "Discus Lord", [0x0b65aa]),
    EnemyData("Firebrand", "Lossoth", [0x0b6f4a]),
    EnemyData("Icebrand", "Fishhead", [0x0b89aa]),
    EnemyData("Stone sword", "Gorgon", [0x0b5d4a]),
    EnemyData("Holy sword", "Vandal Sword", [0x0b80d4]),
    EnemyData("Terminus est", "Nova Skeleton", [0x0b6e82]),
    EnemyData("Marsil", "Fire Demon", [0x0b65fa]),
    EnemyData("Heaven sword", "Cloaked knight", [0x0b88ba]),
    EnemyData("Fist of tulkas", "Lion", [0x0b8752]),
    EnemyData("Gurthang", "Spectral Sword", [0x0b7064]),
    EnemyData("Mourneblade", "Azaghal", [0x0b8032]),
    EnemyData("Mablung sword", "Spectral Sword", [0x0b7062]),
    EnemyData("Great sword", "Guardian", [0x0b9ea4]),
    EnemyData("Morningstar", "Flail Guard", [0x0b6444]),
    EnemyData("Chakram", "Discus Lord", [0x0b65ac]),
    EnemyData("Fire boomerang", "Skelerang", [0x0b5a2a]),
    EnemyData("Iron ball", "Plate Lord", [0x0b69fc]),
    EnemyData("Iron ball", "Ball", [0x0b6dbc]),
    EnemyData("Holbein dagger", "Lesser Demon", [0x0b5c0a]),
    EnemyData("Blue knuckles", "Toad", [0x0b6b64]),
    EnemyData("Dynamite", "Bomb Knight", [0x0b75ca]),
    EnemyData("Masamune", "Black Panther", [0x0b5e3a]),
    EnemyData("Muramasa", "Vandal Sword", [0x0b80d2]),
    EnemyData("Muramasa", "Scarecrow", [0x0b91e2]),
    EnemyData("Heart refresh", "Venus Weed", [0x0b752a]),
    EnemyData("Heart refresh", "Archer", [0x0b8f3c]),
    EnemyData("Heart refresh", "Blue Venus Weed", [0x0b9e02, 0x0b9e2a]),
    EnemyData("Runesword", "Dodo Bird", [0x0b6b12]),
    EnemyData("Antivenom", "Ghost", [0x0b7462]),
    EnemyData("Antivenom", "Bone Pillar", [0x0b789c]),
    EnemyData("Antivenom", "Corpseweed", [0x0b74b4]),
    EnemyData("Uncurse", "Ectoplasm", [0x0b6764]),
    EnemyData("Life apple", "Harpy", [0x0b828a]),
    EnemyData("Hammer", "Hammer", [0x0b7914]),
    EnemyData("Hammer", "Gorgon", [0x0b5d4c]),
    EnemyData("Str. potion", "Wereskeleton", [0x0b632c]),
    EnemyData("Luck potion", "Bitterfly", [0x0b7874]),
    EnemyData("Luck potion", "Imp", [0x0b8ac4]),
    EnemyData("Smart potion", "Marionette", [0x0b614c]),
    EnemyData("Shield potion", "Skeleton", [0x0b655c]),
    EnemyData("Resist fire", "Gremlin", [0x0b805c]),
    EnemyData("Resist ice", "Fishhead", [0x0b89ac]),
    EnemyData("Resist stone", "Medusa Head", [0x0b8eec]),
    EnemyData("Resist stone", "Medusa Head", [0x0b8f14]),
    EnemyData("Resist dark", "Phantom Skull", [0x0b641a]),
    EnemyData("Resist dark", "Karasuman", [0x0b8a24]),
    EnemyData("Potion", "Bat", [0x0b63a4]),
    EnemyData("Potion", "Corpseweed", [0x0b74b2]),
    EnemyData("High potion", "Flea Armor", [0x0b5edc]),
    EnemyData("Manna prism", "Ectoplasm", [0x0b6762]),
    EnemyData("Manna prism", "Salome", [0x0b80fa]),
    EnemyData("Vorpal blade", "Archer", [0x0b8f3a]),
    EnemyData("Crissaegrim", "Schmoo", [0x0b920a]),
    EnemyData("Yasutsuna", "Werewolf", [0x0b9d8a]),
    EnemyData("Cloth tunic", "Bloody Zombie", [0x0b5a7c]),
    EnemyData("Hide cuirass", "Dhuron", [0x0b71a4]),
    EnemyData("Bronze cuirass", "Axe Knight", [0x0b83a2]),
    EnemyData("Iron cuirass", "Spear Guard", [0x0b682a]),
    EnemyData("Iron cuirass", "Flea Armor", [0x0b5eda]),
    EnemyData("Gold plate", "Blade", [0x0b79b2]),
    EnemyData("Gold plate", "Gurkha", [0x0b7962]),
    EnemyData("Gold plate", "Hammer", [0x0b7912]),
    EnemyData("Platinum mail", "Rock Knight", [0x0b761a]),
    EnemyData("Fire mail", "Gremlin", [0x0b805a]),
    EnemyData("Fire mail", "Hellfire Beast", [0x0b64ba]),
    EnemyData("Lightning mail", "Hellfire Beast", [0x0b64bc]),
    EnemyData("Ice mail", "Frozen Shade", [0x0b6a4c]),
    EnemyData("Dark armor", "Malachi", [0x0b8212]),
    EnemyData("Brilliant mail", "Sniper of Goth", [0x0b7a7a]),
    EnemyData("Mojo mail", "Tin man", [0x0b87a2]),
    EnemyData("Fury plate", "Minotaur", [0x0b9d12]),
    EnemyData("God's Garb", "Guardian", [0x0b9ea2]),
    EnemyData("Ballroom mask", "Bone Pillar", [0x0b789a]),
    EnemyData("Felt hat", "Phantom Skull", [0x0b641c]),
    EnemyData("Stone mask", "Ghost Dancer", [0x0b7ef2]),
    EnemyData("Circlet", "Marionette", [0x0b614a]),
    EnemyData("Gold circlet", "Salem Witch", [0x0b7fbc]),
    EnemyData("Opal circlet", "Frozen Half", [0x0b7f1a]),
    EnemyData("Coral circlet", "Venus Weed", [0x0b752c]),
    EnemyData("Wizard hat", "Salome", [0x0b80fc]),
    EnemyData("Zircon", "Merman", [0x0b5cac]),
    EnemyData("Zircon", "Merman", [0x0b5cfc]),
    EnemyData("Zircon", "Blue Raven", [0x0b6ca4]),
    EnemyData("Aquamarine", "Black Crow", [0x0b6ccc]),
    EnemyData("Aquamarine", "Killer Fish", [0x0b9644]),
    EnemyData("Turquoise", "Fire Warg", [0x0b7324]),
    EnemyData("Turquoise", "Ball", [0x0b6dba]),
    EnemyData("Garnet", "Wereskeleton", [0x0b632a]),
    EnemyData("Lapis lazuli", "Orobourous", [0x0b70da]),
    EnemyData("Ring of varda", "Paranthropus", [0x0b7e2a]),
    EnemyData("Mystic pendant", "Bitterfly", [0x0b7872]),
    EnemyData("Heart broach", "Dodo Bird", [0x0b6b14]),
    EnemyData("Necklace of j", "Frozen Half", [0x0b7f1c]),
    EnemyData("Gauntlet", "Paranthropus", [0x0b7e2c]),
    EnemyData("Gauntlet", "Lion", [0x0b8754]),
    EnemyData("Ring of feanor", "Karasuman", [0x0b8a22]),
    EnemyData("Medal", "Owl Knight", [0x0b5b92]),
    EnemyData("Talisman", "Bone Musket", [0x0b6ac2]),
    EnemyData("King's stone", "Imp", [0x0b8ac2]),
    EnemyData("Covenant stone", "Azaghal", [0x0b8034]),
    EnemyData("Nauglamir", "Cave Troll", [0x0b73ea]),
]