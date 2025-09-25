import streamlit as st
from character import buildJson
from items_data import ENEMY_DROP, FORGERY_DROP, BOSS_DROP, WEEKLY_DROP, LOCAL_MATERIAL

st.set_page_config(page_title="Wuthering Waves API GUI")
st.title("Wuthering Waves JSON builder")

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
        weapon = st.selectbox(
            "Element", ["Sword", "Gauntlets", "Pistol", "Broadblade", "Rectifier"]
        )

    cols = st.columns(2)
    with cols[0]:
        rarity = st.selectbox("Element", [4, 5])
    with cols[1]:
        element = st.selectbox(
            "Element", ["Aero", "Electro", "Fusion", "Glacio", "Havoc", "Spectro"]
        )
    cols = st.columns(2)
    with cols[0]:
        nation = st.text_input("Nation")
    with cols[1]:
        char_class = st.text_input("Class")

    st.markdown("### Materials")

    cols = st.columns(5)
    with cols[0]:
        enemy_drop = st.selectbox("Common", ENEMY_DROP)
    with cols[1]:
        weekly_boss = st.selectbox("Weekly", WEEKLY_DROP)
    with cols[2]:
        forgery_drop = st.selectbox("Rare", FORGERY_DROP)
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
            "enemy_drop": enemy_drop,
            "weekly_drop": weekly_boss,
            "forgery_drop": forgery_drop,
            "boss_drop": boss_drop,
            "local_drop": local_mat,
        }
        character_json = buildJson(character_data)
        st.json(character_json)

elif st.session_state.page == "weapon":
    st.subheader("Weapon Form (WIP)")
    st.write("To do later")


elif st.session_state.page == "item":
    st.subheader("Item Form (WIP)")
    st.write("To do later")
