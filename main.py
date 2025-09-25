import streamlit as st
from character import buildJson
import datetime
import json
import os
from items_data import ENEMY_DROP, FORGERY_DROP, BOSS_DROP, WEEKLY_DROP, LOCAL_MATERIAL
from character_data import ATTRIBUTE, CLASS, NATION, WEAPON

st.set_page_config(page_title="Wuthering Waves API GUI")
st.title("Wuthering Waves JSON builder")


def save_character(character_json, folder="characters"):
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"{character_json['id']}.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(character_json, f, ensure_ascii=False, indent=4)

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

    st.markdown("### Basic Informations")

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

    st.markdown("### Materials")

    cols = st.columns(5)
    with cols[0]:
        enemy_drop_base = st.selectbox("Common", [mat["base"] for mat in ENEMY_DROP])
        enemy_drop = next(mat for mat in ENEMY_DROP if mat["base"] == enemy_drop_base)
    with cols[1]:
        weekly_boss = st.selectbox("Weekly", WEEKLY_DROP)
    with cols[2]:
        forgery_drop_base = st.selectbox(
            "Forgery", [mat["base"] for mat in FORGERY_DROP]
        )
        forgery_drop = next(
            mat for mat in FORGERY_DROP if mat["base"] == forgery_drop_base
        )
    with cols[3]:
        boss_drop = st.selectbox("Boss", BOSS_DROP)
    with cols[4]:
        local_mat = st.selectbox("Local", LOCAL_MATERIAL)

    if st.button("Save"):
        character_data = {
            "id": name.lower(),
            "name": name,
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
        character_json = buildJson(character_data)
        save_character(character_json)

elif st.session_state.page == "weapon":
    st.subheader("Weapon Form (WIP)")
    st.write("To do later")


elif st.session_state.page == "item":
    st.subheader("Item Form (WIP)")
    st.write("To do later")
