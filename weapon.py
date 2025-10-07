from items_data import ENEMY_DROP, FORGERY_DROP

FORGERY_BY_TYPE = {
    "Swords": FORGERY_DROP[0],
    "Gauntlets": FORGERY_DROP[4],
    "Pistols": FORGERY_DROP[1],
    "Broadblades": FORGERY_DROP[3],
    "Rectifiers": FORGERY_DROP[2],
}


def ascension_template_5(weapon_data):
    forgery_drop = FORGERY_BY_TYPE[weapon_data["type"]]
    return {
        "20": [
            {"name": "Shell Credit", "value": 10000},
            {"name": get_variant(weapon_data["enemy_drop"], 0), "value": 6},
        ],
        "40": [
            {"name": "Shell Credit", "value": 20000},
            {"name": get_variant(weapon_data["enemy_drop"], 1), "value": 6},
            {"name": get_variant(forgery_drop, 0), "value": 6},
        ],
        "50": [
            {"name": "Shell Credit", "value": 40000},
            {"name": get_variant(weapon_data["enemy_drop"], 2), "value": 4},
            {"name": get_variant(forgery_drop, 1), "value": 8},
        ],
        "60": [
            {"name": "Shell Credit", "value": 60000},
            {"name": get_variant(weapon_data["enemy_drop"], 2), "value": 6},
            {"name": get_variant(forgery_drop, 2), "value": 6},
        ],
        "70": [
            {"name": "Shell Credit", "value": 80000},
            {"name": get_variant(weapon_data["enemy_drop"], 3), "value": 4},
            {"name": get_variant(forgery_drop, 3), "value": 8},
        ],
        "80": [
            {"name": "Shell Credit", "value": 12000},
            {"name": get_variant(weapon_data["enemy_drop"], 3), "value": 8},
            {"name": get_variant(forgery_drop, 3), "value": 12},
        ],
    }


def ascension_template_4(weapon_data):
    forgery_drop = FORGERY_BY_TYPE[weapon_data["type"]]
    return {
        "20": [
            {"name": "Shell Credit", "value": 8000},
            {"name": get_variant(weapon_data["enemy_drop"], 0), "value": 5},
        ],
        "40": [
            {"name": "Shell Credit", "value": 16000},
            {"name": get_variant(weapon_data["enemy_drop"], 1), "value": 5},
            {"name": get_variant(forgery_drop, 0), "value": 5},
        ],
        "50": [
            {"name": "Shell Credit", "value": 32000},
            {"name": get_variant(weapon_data["enemy_drop"], 2), "value": 4},
            {"name": get_variant(forgery_drop, 1), "value": 7},
        ],
        "60": [
            {"name": "Shell Credit", "value": 48000},
            {"name": get_variant(weapon_data["enemy_drop"], 2), "value": 5},
            {"name": get_variant(forgery_drop, 2), "value": 5},
        ],
        "70": [
            {"name": "Shell Credit", "value": 64000},
            {"name": get_variant(weapon_data["enemy_drop"], 3), "value": 4},
            {"name": get_variant(forgery_drop, 3), "value": 7},
        ],
        "80": [
            {"name": "Shell Credit", "value": 96000},
            {"name": get_variant(weapon_data["enemy_drop"], 3), "value": 7},
            {"name": get_variant(forgery_drop, 3), "value": 10},
        ],
    }


def ascension_template_3(weapon_data):
    forgery_drop = FORGERY_BY_TYPE[weapon_data["type"]]
    return {
        "20": [
            {"name": "Shell Credit", "value": 6000},
            {"name": get_variant(weapon_data["enemy_drop"], 0), "value": 4},
        ],
        "40": [
            {"name": "Shell Credit", "value": 12000},
            {"name": get_variant(weapon_data["enemy_drop"], 1), "value": 4},
            {"name": get_variant(forgery_drop, 0), "value": 4},
        ],
        "50": [
            {"name": "Shell Credit", "value": 24000},
            {"name": get_variant(weapon_data["enemy_drop"], 2), "value": 3},
            {"name": get_variant(forgery_drop, 1), "value": 5},
        ],
        "60": [
            {"name": "Shell Credit", "value": 36000},
            {"name": get_variant(weapon_data["enemy_drop"], 2), "value": 4},
            {"name": get_variant(forgery_drop, 2), "value": 4},
        ],
        "70": [
            {"name": "Shell Credit", "value": 48000},
            {"name": get_variant(weapon_data["enemy_drop"], 3), "value": 3},
            {"name": get_variant(forgery_drop, 3), "value": 5},
        ],
        "80": [
            {"name": "Shell Credit", "value": 72000},
            {"name": get_variant(weapon_data["enemy_drop"], 3), "value": 5},
            {"name": get_variant(forgery_drop, 3), "value": 8},
        ],
    }


ASCENSION_TEMPLATES = {
    3: ascension_template_3,
    4: ascension_template_4,
    5: ascension_template_5,
}


def get_variant(item, level):
    return item["variants"][level]


def build_weapon_json(weapon_data):
    template = ASCENSION_TEMPLATES.get(weapon_data["rarity"])
    ascension_mats = template(weapon_data) if template else {}

    weapon_json = {
        "name": weapon_data["name"],
        "id": weapon_data["id"],
        "type": weapon_data["type"],
        "rarity": weapon_data["rarity"],
        "base_attack": weapon_data["base_attack"],
        "sub_stat": weapon_data["sub_stat"],
        "sub_stat_base": weapon_data["base_sub"],
        "ascension_materials": ascension_mats,
    }

    return weapon_json
