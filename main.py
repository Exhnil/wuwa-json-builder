import streamlit as st
from character import build_character_json
from weapon import build_weapon_json
import datetime
import json
from items_data import ENEMY_DROP, FORGERY_DROP, BOSS_DROP, WEEKLY_DROP, LOCAL_MATERIAL
from character_data import ATTRIBUTE, CLASS, NATION, WEAPON
from weapons_data import SUB_STAT

st.set_page_config(page_title="Wuthering Waves API GUI")
st.title("Wuthering Waves JSON builder")


def get_mat_by_type(domain_type: str):
    if domain_type == "Forgery Challenge":
        return [m["base"] for m in FORGERY_DROP]
    elif domain_type == "Overlord Class":
        return BOSS_DROP
    elif domain_type == "Weekly Challenge":
        return WEEKLY_DROP
    return []


def get_forgery_values():
    # Raretés 2 → 5
    return [6.4, 8.0, 1.682, 0.206]


if "page" not in st.session_state:
    st.session_state.page = None

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Character Form"):
        st.session_state.page = "character"

with col2:
    if st.button("Weapon Form"):
        st.session_state.page = "weapon"

with col3:
    if st.button("Item Form"):
        st.session_state.page = "item"

with col4:
    if st.button("Domain Form"):
        st.session_state.page = "domain"

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
            attribute = st.selectbox("Attribute", ATTRIBUTE)
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

    character_data = {
        "id": name.strip().lower(),
        "name": name.strip(),
        "attribute": attribute,
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

    file_name = f"{character_json['id']}.json"
    if st.download_button(
        label="Save",
        data=json.dumps(character_json, ensure_ascii=False, indent=4),
        file_name=file_name,
        mime="application/json",
    ):
        st.success(f"Saved successfully as {file_name}")
        st.json(character_json)

elif st.session_state.page == "weapon":
    st.subheader("Weapon Form")

    name = st.text_input("Name")

    cols = st.columns(2)
    with cols[0]:
        weapon_type = st.selectbox("Type", WEAPON)
    with cols[1]:
        rarity = st.selectbox("Rarity", [3, 4, 5])

    cols = st.columns(3)
    with cols[0]:
        base_attack = st.number_input("Base Attack", min_value=0, step=1)
    with cols[1]:
        sub_stat = st.selectbox("Sub Stat", SUB_STAT)
    with cols[2]:
        base_sub = st.number_input("Base Sub Stat", min_value=1.0, step=0.1)

    enemy_drop_base = st.selectbox("Common", [mat["base"] for mat in ENEMY_DROP])
    enemy_drop = next(mat for mat in ENEMY_DROP if mat["base"] == enemy_drop_base)

    weapon_data = {
        "name": name.strip(),
        "id": name.lower().replace(" ", "-").replace("'", "-"),
        "type": weapon_type,
        "rarity": rarity,
        "base_attack": base_attack,
        "sub_stat": sub_stat,
        "base_sub": base_sub,
        "enemy_drop": enemy_drop,
    }

    weapon_json = build_weapon_json(weapon_data)
    file_name = f"{weapon_json['id']}.json"
    if st.download_button(
        label="Save",
        data=json.dumps(weapon_json, ensure_ascii=False, indent=4),
        file_name=file_name,
        mime="application/json",
    ):
        st.success(f"Saved successfully as {file_name}")
        st.json(weapon_json)

elif st.session_state.page == "item":

    SOURCES = ["enemies", "forgery", "boss", "weekly", "local"]
    TYPES = [
        "Resonator Ascension Material",
        "Ascension Material",
        "Weapon and Skill Material",
        "Skill Upgrade Material",
    ]
    st.subheader("Item Form")

    name = st.text_input("Name")
    rarity = st.selectbox("Rarity", [1, 2, 3, 4, 5])
    type = st.selectbox("Type", TYPES)
    source = st.selectbox("Source", SOURCES)

    item_data = {
        "name": name.strip(),
        "id": name.strip().lower().replace(" ", "-").replace("'","-"),
        "type": type,
        "rarity": rarity,
        "source": source,
    }

    file_name = f"{item_data['id']}.json"
    if st.download_button(
        label="Save",
        data=json.dumps(item_data, ensure_ascii=False, indent=4),
        file_name=file_name,
        mime="application/json",
    ):
        st.success(f"Saved successfully as {file_name}")
        st.json(item_data)


elif st.session_state.page == "domain":

    st.subheader("Domain Form")
    name = st.text_input("Name")
    type = st.selectbox(
        "Type", ["Forgery Challenge", "Weekly Challenge", "Overlord Class"]
    )
    cost = st.number_input("Cost", min_value=0, step=1)

    st.divider()

    st.subheader("Materials")

    available_materials = get_mat_by_type(type)
    base_material = st.selectbox("Select material", available_materials)

    add_button = st.button("Add Material")

    if "domain_materials" not in st.session_state:
        st.session_state.domain_materials = []

    if add_button and base_material:
        if type == "Forgery Challenge":
            drop_rates = [6.4, 8, 1.682, 0.206]
            variants = next(
                (m["variants"] for m in FORGERY_DROP if m["base"] == base_material), []
            )
            for i, v in enumerate(variants):
                drop_rate = drop_rates[i] if i < len(drop_rates) else None
                st.session_state.domain_materials.append(
                    {
                        "name": v,
                        "id": v.lower().replace(" ", "-").replace("'", "-"),
                        "value": drop_rate,
                    }
                )
        else:
            drop_rate = (
                3
                if type == "Weekly Challenge"
                else 4.1 if type == "Overlord Class" else None
            )
            st.session_state.domain_materials.append(
                {
                    "name": base_material,
                    "id": base_material.lower().replace(" ", "-").replace("'", "-"),
                    "value": drop_rate,
                }
            )

    if st.session_state.domain_materials:
        st.table(st.session_state.domain_materials)

    st.divider()

    data = {
        "name": name.strip(),
        "id": name.strip().lower().replace(" ", "-").replace("'", "-"),
        "type": type,
        "cost": cost,
        "materials": st.session_state.domain_materials,
    }

    file_name = f"{data['id']}.json"

    if st.download_button(
        label="Save",
        data=json.dumps(data, ensure_ascii=False, indent=4),
        file_name=file_name,
        mime="application/json",
    ):

        st.success(f"saved successfully")
        st.json(data)
        st.session_state.domain_materials = []
