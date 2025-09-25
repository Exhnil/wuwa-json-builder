
def buildJson(character_data):

    def ascension_template():
        return {
            "20": [
                {"name": "Shell Credit", "value": 5000},
                {"name": character_data["forgery_drop"], "value": 4},
            ],
            "40": [
                {"name": "Shell Credit", "value": 10000},
                {"name": character_data["local_drop"], "value": 4},
                {"name": character_data["forgery_drop"], "value": 4},
                {"name": character_data["boss_drop"], "value": 3},
            ],
            "50": [
                {"name": "Shell Credit", "value": 15000},
                {"name": character_data["local_drop"], "value": 8},
                {"name": character_data["forgery_drop"], "value": 8},
                {"name": character_data["boss_drop"], "value": 6},
            ],
            "60": [
                {"name": "Shell Credit", "value": 20000},
                {"name": character_data["local_drop"], "value": 12},
                {"name": character_data["forgery_drop"], "value": 4},
                {"name": character_data["boss_drop"], "value": 9},
            ],
            "70": [
                {"name": "Shell Credit", "value": 40000},
                {"name": character_data["local_drop"], "value": 16},
                {"name": character_data["forgery_drop"], "value": 8},
                {"name": character_data["boss_drop"], "value": 12},
            ],
            "80": [
                {"name": "Shell Credit", "value": 80000},
                {"name": character_data["local_drop"], "value": 20},
                {"name": character_data["forgery_drop"], "value": 4},
                {"name": character_data["boss_drop"], "value": 16},
            ],
        }

    def skill_template():
        return {
            "2": [
                {"name": "Shell Credit", "value": 1500},
                {"name": character_data["enemy_drop"], "value": 2},
                {"name": character_data["forgery_drop"], "value": 2},
            ],
            "3": [
                {"name": "Shell Credit", "value": 2000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
            ],
            "4": [
                {"name": "Shell Credit", "value": 4500},
                {"name": character_data["enemy_drop"], "value": 2},
                {"name": character_data["forgery_drop"], "value": 2},
            ],
            "5": [
                {"name": "Shell Credit", "value": 6000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
            ],
            "6": [
                {"name": "Shell Credit", "value": 16000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 2},
            ],
            "7": [
                {"name": "Shell Credit", "value": 30000},
                {"name": character_data["enemy_drop"], "value": 5},
                {"name": character_data["forgery_drop"], "value": 3},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
            "8": [
                {"name": "Shell Credit", "value": 50000},
                {"name": character_data["enemy_drop"], "value": 2},
                {"name": character_data["forgery_drop"], "value": 2},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
            "9": [
                {"name": "Shell Credit", "value": 70000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
            "10": [
                {"name": "Shell Credit", "value": 100000},
                {"name": character_data["enemy_drop"], "value": 6},
                {"name": character_data["forgery_drop"], "value": 4},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
        }

    def stats_bonus_template():
        return {
            "rank_1": [
                {"name": "Shell Credit", "value": 50000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
            ],
            "rank_2": [
                {"name": "Shell Credit", "value": 100000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
        }

    def inherent_skill_template():
        return {
            "skill_1": [
                {"name": "Shell Credit", "value": 10000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
            "skill_2": [
                {"name": "Shell Credit", "value": 20000},
                {"name": character_data["enemy_drop"], "value": 3},
                {"name": character_data["forgery_drop"], "value": 3},
                {"name": character_data["weekly_drop"], "value": 1},
            ],
        }

    character_json = {
        "id": character_data["id"],
        "name": character_data["name"],
        "element": character_data["element"],
        "weapon": character_data["weapon"],
        "gender": character_data["gender"],
        "nation": character_data["nation"],
        "class": character_data["class"],
        "rarity": character_data["rarity"],
        "ascension_materials": ascension_template(),
        "skill_materials": skill_template(),
        "stats_bonus_materials": stats_bonus_template(),
        "inherent_skill_materials": inherent_skill_template(),
    }

    return character_json
