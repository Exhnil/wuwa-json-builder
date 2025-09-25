import streamlit as st
from character import build_character_json
from weapon import build_weapon_json
import datetime
import json
import streamlit.web.cli as stcli
import sys
import os
from items_data import ENEMY_DROP, FORGERY_DROP, BOSS_DROP, WEEKLY_DROP, LOCAL_MATERIAL
from character_data import ATTRIBUTE, CLASS, NATION, WEAPON
from weapons_data import SUB_STAT

st.set_page_config(page_title="Wuthering Waves API GUI")
st.title("Wuthering Waves JSON builder")


def save_file(file_json, folder):
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"{file_json['id']}.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(file_json, f, ensure_ascii=False, indent=4)

    st.success(f"File saved as {path}")
    return path


if "page" not in st.session_state:
    st.session_state.page = None

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Character Form"):
        st.session_state.page = "character"

with col2:
    if st.button("Weapon Form"):
        st.session_state.page = "weapon"

with col3:
    if st.button("Item Form"):
        st.session_state.page = "item"

if st.session_state.page == "character":
    st.subheader("Character Form")

    with st.expander("Basic Informations", expanded=True):
        cols = st.columns(3)
        with cols[0]:
            name = st.text_input("Name")
        with cols[1]:
            gender = st.selectbox("Gender", ["Male", "Female"])
        with cols[2]:
            weapon = st.selectbox("Weapon", WEAPON)
        cols = st.columns(2)
        with cols[0]:
            rarity = st.selectbox("Rarity", [4, 5])
        with cols[1]:
            element = st.selectbox("Element", ATTRIBUTE)
        cols = st.columns(3)
        with cols[0]:
            nation = st.selectbox("Nation", NATION)
        with cols[1]:
            char_class = st.selectbox("Class", CLASS)
        with cols[2]:
            release_date = st.date_input(
                "Release Date",
                value=datetime.date.today(),
                min_value=datetime.date(2024, 1, 1),
                max_value=datetime.date.today(),
            )
            release_date_str = release_date.strftime("%Y-%m-%d")

    with st.expander("Ascension Materials", expanded=True):
        cols = st.columns(3)
        with cols[0]:
            enemy_drop_base = st.selectbox(
                "Common", [mat["base"] for mat in ENEMY_DROP]
            )
            enemy_drop = next(
                mat for mat in ENEMY_DROP if mat["base"] == enemy_drop_base
            )
        with cols[1]:
            weekly_boss = st.selectbox("Weekly", WEEKLY_DROP)
        with cols[2]:
            forgery_drop_base = st.selectbox(
                "Forgery", [mat["base"] for mat in FORGERY_DROP]
            )
            forgery_drop = next(
                mat for mat in FORGERY_DROP if mat["base"] == forgery_drop_base
            )
        cols = st.columns(2)
        with cols[0]:
            boss_drop = st.selectbox("Boss", BOSS_DROP)
        with cols[1]:
            local_mat = st.selectbox("Local", LOCAL_MATERIAL)

    if st.button("Save"):
        character_data = {
            "id": name.strip().lower(),
            "name": name.strip(),
            "element": element,
            "weapon": weapon,
            "rarity": rarity,
            "gender": gender,
            "nation": nation,
            "class": char_class,
            "release": release_date_str,
            "enemy_drop": enemy_drop,
            "weekly_drop": weekly_boss,
            "forgery_drop": forgery_drop,
            "boss_drop": boss_drop,
            "local_drop": local_mat,
        }
        character_json = build_character_json(character_data)
        save_file(character_json, "characters")

elif st.session_state.page == "weapon":
    st.subheader("Weapon Form")

    name = st.text_input("Name")

    cols = st.columns(2)
    with cols[0]:
        weapon_type = st.selectbox("Type", WEAPON)
    with cols[1]:
        rarity = st.selectbox("Rarity", [4, 5])

    cols = st.columns(3)
    with cols[0]:
        base_attack = st.number_input("Base Attack", min_value=0, step=1)
    with cols[1]:
        sub_stat = st.selectbox("Sub Stat", SUB_STAT)
    with cols[2]:
        base_sub = st.number_input("Base Sub Stat", min_value=1.0, step=0.1)

    enemy_drop_base = st.selectbox("Common", [mat["base"] for mat in ENEMY_DROP])
    enemy_drop = next(mat for mat in ENEMY_DROP if mat["base"] == enemy_drop_base)

    if st.button("Save"):
        weapon_data = {
            "name": name.strip(),
            "id": name.lower().replace(" ", "-").replace("'", "-"),
            "type": weapon_type,
            "rarity": rarity,
            "base_attack": base_attack,
            "sub_stat": sub_stat,
            "base_sub": base_sub,
            "enemy_drop": enemy_drop,
            "forgery_drop": "",
        }
        weapon_json = build_weapon_json(weapon_data)
        save_file(weapon_json, "weapons")
        st.json(weapon_json)

elif st.session_state.page == "item":

    SOURCES = ["enemies", "forgery", "boss", "weekly", "local"]
    st.subheader("Item Form")

    name = st.text_input("Name")
    rarity = st.selectbox("Rarity", [1, 2, 3, 4, 5])
    source = st.selectbox("Source", SOURCES)

    if st.button("Save"):
        item_data = {
            "name": name.strip(),
            "id": name.strip().lower().replace(" ", "-"),
            "rarity": rarity,
            "source": source,
        }

        save_file(item_data, "items")
        st.json(item_data)
