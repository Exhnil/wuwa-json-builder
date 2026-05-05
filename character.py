import re


def to_kebab(s: str) -> str:
    s = s.lower()
    s = s.replace("'", "-")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def get_variant(item, level):
    return to_kebab(item["variants"][level])


def build_character_json(character_data):

    def ascension_template():
        return {
            "1": [
                {"id": "shell-credit", "value": 5000},
                {"id": get_variant(character_data["enemy_drop"], 0), "value": 4},
            ],
            "2": [
                {"id": "shell-credit", "value": 10000},
                {"id": character_data["local_drop"], "value": 4},
                {"id": get_variant(character_data["enemy_drop"], 1), "value": 4},
                {"id": character_data["boss_drop"], "value": 3},
            ],
            "3": [
                {"id": "shell-credit", "value": 15000},
                {"id": character_data["local_drop"], "value": 8},
                {"id": get_variant(character_data["enemy_drop"], 1), "value": 8},
                {"id": character_data["boss_drop"], "value": 6},
            ],
            "4": [
                {"id": "shell-credit", "value": 20000},
                {"id": character_data["local_drop"], "value": 12},
                {"id": get_variant(character_data["enemy_drop"], 2), "value": 4},
                {"id": character_data["boss_drop"], "value": 9},
            ],
            "5": [
                {"id": "shell-credit", "value": 40000},
                {"id": character_data["local_drop"], "value": 16},
                {"id": get_variant(character_data["enemy_drop"], 2), "value": 8},
                {"id": character_data["boss_drop"], "value": 12},
            ],
            "6": [
                {"id": "shell-credit", "value": 80000},
                {"id": character_data["local_drop"], "value": 20},
                {"id": get_variant(character_data["enemy_drop"], 3), "value": 4},
                {"id": character_data["boss_drop"], "value": 16},
            ],
        }

    def skill_template():
        return {
            "2": [
                {"id": "shell-credit", "value": 1500},
                {"id": get_variant(character_data["forgery_drop"], 0), "value": 2},
                {"id": get_variant(character_data["enemy_drop"], 0), "value": 2},
            ],
            "3": [
                {"id": "shell-credit", "value": 2000},
                {"id": get_variant(character_data["forgery_drop"], 0), "value": 3},
                {"id": get_variant(character_data["enemy_drop"], 0), "value": 3},
            ],
            "4": [
                {"id": "shell-credit", "value": 4500},
                {"id": get_variant(character_data["forgery_drop"], 1), "value": 2},
                {"id": get_variant(character_data["enemy_drop"], 1), "value": 2},
            ],
            "5": [
                {"id": "shell-credit", "value": 6000},
                {"id": get_variant(character_data["forgery_drop"], 1), "value": 3},
                {"id": get_variant(character_data["enemy_drop"], 1), "value": 3},
            ],
            "6": [
                {"id": "shell-credit", "value": 16000},
                {"id": get_variant(character_data["forgery_drop"], 2), "value": 3},
                {"id": get_variant(character_data["enemy_drop"], 2), "value": 2},
            ],
            "7": [
                {"id": "shell-credit", "value": 30000},
                {"id": get_variant(character_data["forgery_drop"], 2), "value": 5},
                {"id": get_variant(character_data["enemy_drop"], 2), "value": 3},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
            "8": [
                {"id": "shell-credit", "value": 50000},
                {"id": get_variant(character_data["forgery_drop"], 3), "value": 2},
                {"id": get_variant(character_data["enemy_drop"], 3), "value": 2},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
            "9": [
                {"id": "shell-credit", "value": 70000},
                {"id": get_variant(character_data["forgery_drop"], 3), "value": 3},
                {"id": get_variant(character_data["enemy_drop"], 3), "value": 3},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
            "10": [
                {"id": "shell-credit", "value": 100000},
                {"id": get_variant(character_data["forgery_drop"], 3), "value": 6},
                {"id": get_variant(character_data["enemy_drop"], 3), "value": 4},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
        }

    def stats_bonus_template():
        return {
            "rank_1": [
                {"id": "shell-credit", "value": 50000},
                {"id": get_variant(character_data["enemy_drop"], 2), "value": 3},
                {"id": get_variant(character_data["forgery_drop"], 2), "value": 3},
            ],
            "rank_2": [
                {"id": "shell-credit", "value": 100000},
                {"id": get_variant(character_data["enemy_drop"], 3), "value": 3},
                {"id": get_variant(character_data["forgery_drop"], 3), "value": 3},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
        }

    def inherent_skill_template():
        return {
            "skill_1": [
                {"id": "shell-credit", "value": 10000},
                {"id": get_variant(character_data["enemy_drop"], 1), "value": 3},
                {"id": get_variant(character_data["forgery_drop"], 1), "value": 3},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
            "skill_2": [
                {"id": "shell-credit", "value": 20000},
                {"id": get_variant(character_data["enemy_drop"], 2), "value": 3},
                {"id": get_variant(character_data["forgery_drop"], 2), "value": 3},
                {"id": character_data["weekly_drop"], "value": 1},
            ],
        }

    character_json = {
        "id": to_kebab(character_data["id"]),
        "name": character_data["name"],
        "attribute": character_data["attribute"],
        "weapon": character_data["weapon"],
        "gender": character_data["gender"],
        "nation": character_data["nation"],
        "class": character_data["class"],
        "rarity": character_data["rarity"],
        "release": character_data["release"],
        "ascension_materials": ascension_template(),
        "skill_materials": skill_template(),
        "stats_bonus_materials": stats_bonus_template(),
        "inherent_skill_materials": inherent_skill_template(),
    }

    return character_json
