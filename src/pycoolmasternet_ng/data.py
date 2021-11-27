from .constants import LineType, Mode

# TODO: are wireless devices supported on all lines or L5 only?
# TODO: is M1M2 on all lines or on L1 only? - I suspect L1 only on CoolPlug

LINES_TO_POSSIBLE_TYPES = {
    1: [
        LineType.DAIKIN,
        LineType.MITSUBISHI_ELECTRIC,
        LineType.MITSUBISHI_ELECTRIC_M1M2,
        LineType.SANYO,
        LineType.TOSHIBA,
        LineType.PANASONIC,
        LineType.HITACHI,
        LineType.HAIER,
    ],
    2: [
        LineType.DAIKIN,
        LineType.MITSUBISHI_ELECTRIC,
        LineType.SANYO,
        LineType.TOSHIBA,
        LineType.PANASONIC,
        LineType.HITACHI,
        LineType.HAIER,
    ],
    3: [
        LineType.LG,
        LineType.MITSUBISHI_HEAVY_INDUSTRIES,
        LineType.GREE,
        LineType.MIDEA,
        LineType.KENTATSU,
        LineType.TRANE,
        LineType.CHIGO,
        LineType.SAMSUNG,
        LineType.TADIRAN_INVERTER,
        LineType.MEITAV,
        LineType.BLUESTAR,
        LineType.KNX,
        LineType.PLUGBUS,
        LineType.PLUGBUS_WIRELESS,
        LineType.HDL,
        LineType.MODBUS_COOLGATE4,
        LineType.MODBUS_COOLGATE5,
    ],
    4: [
        LineType.LG,
        LineType.MITSUBISHI_HEAVY_INDUSTRIES,
        LineType.GREE,
        LineType.MIDEA,
        LineType.KENTATSU,
        LineType.TRANE,
        LineType.CHIGO,
        LineType.SAMSUNG,
        LineType.TADIRAN_INVERTER,
        LineType.MEITAV,
        LineType.BLUESTAR,
        LineType.HDL,
        LineType.MODBUS_COOLGATE4,
        LineType.MODBUS_COOLGATE5,
    ],
    5: [
        LineType.LG,
        LineType.MITSUBISHI_HEAVY_INDUSTRIES,
        LineType.GREE,
        LineType.MIDEA,
        LineType.KENTATSU,
        LineType.TRANE,
        LineType.CHIGO,
        LineType.SAMSUNG,
        LineType.TADIRAN_INVERTER,
        LineType.MEITAV,
        LineType.BLUESTAR,
        LineType.PLUGBUS,
        LineType.PLUGBUS_WIRELESS,
        LineType.HDL,
        LineType.MODBUS_COOLGATE4,
        LineType.MODBUS_COOLGATE5,
    ],
    6: [
        LineType.LG,
        LineType.MITSUBISHI_HEAVY_INDUSTRIES,
        LineType.GREE,
        LineType.MIDEA,
        LineType.KENTATSU,
        LineType.TRANE,
        LineType.CHIGO,
        LineType.SAMSUNG,
        LineType.TADIRAN_INVERTER,
        LineType.MEITAV,
        LineType.BLUESTAR,
        LineType.HDL,
        LineType.MODBUS_COOLGATE4,
        LineType.MODBUS_COOLGATE5,
    ],
    7: [
        LineType.LG,
        LineType.MITSUBISHI_HEAVY_INDUSTRIES,
        LineType.GREE,
        LineType.MIDEA,
        LineType.KENTATSU,
        LineType.TRANE,
        LineType.CHIGO,
        LineType.SAMSUNG,
        LineType.TADIRAN_INVERTER,
        LineType.MEITAV,
        LineType.BLUESTAR,
        LineType.HDL,
        LineType.MODBUS_COOLGATE4,
        LineType.MODBUS_COOLGATE5,
    ],
    8: [LineType.FUJITSU],
}

LINE_TYPE_TO_MODE_TEMP_RANGE = {
    LineType.MITSUBISHI_ELECTRIC: {
        Mode.COOL: range(19, 27),
        Mode.HEAT: range(17, 25),
        Mode.AUTO: range(17, 27),
        Mode.DRY: range(19, 27),
    },
    LineType.MITSUBISHI_ELECTRIC_M1M2: {
        Mode.COOL: range(19, 27),
        Mode.HEAT: range(17, 25),
        Mode.AUTO: range(17, 27),
        Mode.DRY: range(19, 27),
    },
}

LINE_TYPE_TO_BRAND_NAME = {
    LineType.DAIKIN: "Daikin",
    LineType.MITSUBISHI_ELECTRIC: "Mitsubishi Electric",
    LineType.MITSUBISHI_ELECTRIC_M1M2: "Mitsubishi Electric",
    LineType.SANYO: "Sanyo",
    LineType.TOSHIBA: "Toshiba",
    LineType.PANASONIC: "Panasonic",
    LineType.HITACHI: "Hitachi",
    LineType.LG: "LG",
    LineType.MITSUBISHI_HEAVY_INDUSTRIES: "Mitsubishi Heavy Industries",
    # all-caps on official website: https://gree.uk.com
    LineType.GREE: "GREE",
    LineType.MIDEA: "Midea",
    # all-caps on official website: https://kentatsu.eu/about-us/?lang=en
    LineType.KENTATSU: "KENTATSU",
    LineType.TRANE: "Trane",
    LineType.CHIGO: "Chigo",
    LineType.FUJITSU: "Fujitsu",
    LineType.SAMSUNG: "Samsung",
    LineType.TADIRAN_INVERTER: "Tadiran",
    LineType.MEITAV: "Meitav-tec",
    LineType.HAIER: "Haier",
    LineType.BLUESTAR: "Blue Star",
}
