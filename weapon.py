import re


def ascension_template_5(weapon_data):
    return {
        "1": [
            {"id": "shell-credit", "value": 10000},
            {"id": get_variant(weapon_data["enemy_drop"], 0), "value": 6},
        ],
        "2": [
            {"id": "shell-credit", "value": 20000},
            {"id": get_variant(weapon_data["enemy_drop"], 1), "value": 6},
            {"id": get_variant(weapon_data["forgery_drop"], 0), "value": 6},
        ],
        "3": [
            {"id": "shell-credit", "value": 40000},
            {"id": get_variant(weapon_data["enemy_drop"], 2), "value": 4},
            {"id": get_variant(weapon_data["forgery_drop"], 1), "value": 8},
        ],
        "4": [
            {"id": "shell-credit", "value": 60000},
            {"id": get_variant(weapon_data["enemy_drop"], 2), "value": 6},
            {"id": get_variant(weapon_data["forgery_drop"], 2), "value": 6},
        ],
        "5": [
            {"id": "shell-credit", "value": 80000},
            {"id": get_variant(weapon_data["enemy_drop"], 3), "value": 4},
            {"id": get_variant(weapon_data["forgery_drop"], 3), "value": 8},
        ],
        "6": [
            {"id": "shell-credit", "value": 12000},
            {"id": get_variant(weapon_data["enemy_drop"], 3), "value": 8},
            {"id": get_variant(weapon_data["forgery_drop"], 3), "value": 12},
        ],
    }


def ascension_template_4(weapon_data):
    return {
        "1": [
            {"id": "shell-credit", "value": 8000},
            {"id": get_variant(weapon_data["enemy_drop"], 0), "value": 5},
        ],
        "2": [
            {"id": "shell-credit", "value": 16000},
            {"id": get_variant(weapon_data["enemy_drop"], 1), "value": 5},
            {"id": get_variant(weapon_data["forgery_drop"], 0), "value": 5},
        ],
        "3": [
            {"id": "shell-credit", "value": 32000},
            {"id": get_variant(weapon_data["enemy_drop"], 2), "value": 4},
            {"id": get_variant(weapon_data["forgery_drop"], 1), "value": 7},
        ],
        "4": [
            {"id": "shell-credit", "value": 48000},
            {"id": get_variant(weapon_data["enemy_drop"], 2), "value": 5},
            {"id": get_variant(weapon_data["forgery_drop"], 2), "value": 5},
        ],
        "5": [
            {"id": "shell-credit", "value": 64000},
            {"id": get_variant(weapon_data["enemy_drop"], 3), "value": 4},
            {"id": get_variant(weapon_data["forgery_drop"], 3), "value": 7},
        ],
        "6": [
            {"id": "shell-credit", "value": 96000},
            {"id": get_variant(weapon_data["enemy_drop"], 3), "value": 7},
            {"id": get_variant(weapon_data["forgery_drop"], 3), "value": 10},
        ],
    }


def ascension_template_3(weapon_data):
    return {
        "1": [
            {"id": "shell-credit", "value": 6000},
            {"id": get_variant(weapon_data["enemy_drop"], 0), "value": 4},
        ],
        "2": [
            {"id": "shell-credit", "value": 12000},
            {"id": get_variant(weapon_data["enemy_drop"], 1), "value": 4},
            {"id": get_variant(weapon_data["forgery_drop"], 0), "value": 4},
        ],
        "3": [
            {"id": "shell-credit", "value": 24000},
            {"id": get_variant(weapon_data["enemy_drop"], 2), "value": 3},
            {"id": get_variant(weapon_data["forgery_drop"], 1), "value": 5},
        ],
        "4": [
            {"id": "shell-credit", "value": 36000},
            {"id": get_variant(weapon_data["enemy_drop"], 2), "value": 4},
            {"id": get_variant(weapon_data["forgery_drop"], 2), "value": 4},
        ],
        "5": [
            {"id": "shell-credit", "value": 48000},
            {"id": get_variant(weapon_data["enemy_drop"], 3), "value": 3},
            {"id": get_variant(weapon_data["forgery_drop"], 3), "value": 5},
        ],
        "6": [
            {"id": "shell-credit", "value": 72000},
            {"id": get_variant(weapon_data["enemy_drop"], 3), "value": 5},
            {"id": get_variant(weapon_data["forgery_drop"], 3), "value": 8},
        ],
    }


ASCENSION_TEMPLATES = {
    3: ascension_template_3,
    4: ascension_template_4,
    5: ascension_template_5,
}


def to_kebab(s: str) -> str:
    s = s.lower()
    s = s.replace("'", "-")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def get_variant(item, level):
    return to_kebab(item["variants"][level])


def build_weapon_json(weapon_data):
    template = ASCENSION_TEMPLATES.get(weapon_data["rarity"])
    ascension_mats = template(weapon_data) if template else {}

    weapon_json = {
        "name": weapon_data["name"],
        "id": to_kebab(weapon_data["id"]),
        "type": weapon_data["type"],
        "rarity": weapon_data["rarity"],
        "base_attack": weapon_data["base_attack"],
        "sub_stat": weapon_data["sub_stat"],
        "sub_stat_base": weapon_data["base_sub"],
        "ascension_materials": ascension_mats,
    }

    return weapon_json
