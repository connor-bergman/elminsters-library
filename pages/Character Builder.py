import streamlit as st
import race_engine as re
import class_engine as ce
import reference as ref
import utility as util
import numpy as np
from streamlit import session_state as ss
from character import Character

if 'section_id' not in ss:
    ss.section_id = 1
if 'num_of_classes' not in ss:
    ss.num_of_classes = 1
if 'classes' not in ss:
    ss.classes = {}
if 'total_levels' not in ss:
    ss.total_levels = 0


def next():
    ss.section_id += 1


def back():
    ss.section_id -= 1


def failed_next():
    st.write(":red[Please fill in all fields before continuing.]")


def add_class():
    ss.num_of_classes += 1


def remove_class(class_ix):
    for i in range(class_ix, ss.num_of_classes+1):
        if i == ss.num_of_classes:
            util.remove_states([f"class_{i}_ix", f"class_{i}_level_ix", f"class_{i}_col1", f"class_{i}_col2",
                                f"class_{i}_options", f"class_{i}", f"class_{i}_level_failed",
                                f"class_{i}_add_col", f"class_{i}_remove_col", f"class_{i}_api"])
            if i in ss.classes:
                del ss.classes[i]
        else:
            util.reassign_states([(f"class_{i}_ix", f"class_{i+1}_ix"),
                                 (f"class_{i}_level_ix", f"class_{i+1}_level_ix"),
                                 (f"class_{i}_col1", f"class_{i+1}_col1"),
                                 (f"class_{i}_col2", f"class_{i+1}_col2"),
                                 (f"class_{i}_options", f"class_{i+1}_options"),
                                 (f"class_{i}", f"class_{i+1}"),
                                 (f"class_{i}_level_failed", f"class_{i+1}_level_failed"),
                                 (f"class_{i}_add_col", f"class_{i+1}_add_col"),
                                 (f"class_{i}_remove_col", f"class_{i+1}_remove_col")])
            if i+1 in ss.classes:
                ss.classes[i] = ss.classes[i+1]
    if ss.num_of_classes > 1:
        ss.num_of_classes -= 1
    


def save_character():

    character = Character()
    
    character.name = ss.name
    character.race = ss.race
    character.classes = {}

    character.export()


def identity_section():

    st.markdown("## Name")

    util.initialize_states(['name', 'race', 'race_ix'])
    has_subraces = False

    ss.name = st.text_input("Name", placeholder="Choose a name", label_visibility="collapsed", value=ss.name)

    st.markdown("## Race")
    st.selectbox("Race", options=re.races.keys(), key='race_choice',
                        index=ss.race_ix, placeholder="Choose a race", label_visibility="collapsed",
                        on_change=util.update_index, args=('race_choice', 'race_ix', list(re.races.keys())))
    
    if ss.race_choice is not None:
        ss.race = re.races[ss.race_choice]()
        ss.race.traitText()
        if hasattr(ss.race, "chooseSubrace"):
            has_subraces = True
            ss.race.chooseSubrace()

    identity_col1, identity_col2, identity_col3 = st.columns((4,1,4))

    with identity_col2:
        if ss.name == "" or ss.race_choice is None or (ss.race_choice is not None and None in list(ss.race.choices.values())) or (has_subraces and (ss.race.subrace is None or None in list(ss.race.subrace.choices.values()))):   
            if st.button("Next", type='primary', on_click=failed_next):
                pass
        else:
            if st.button("Next", type='primary', on_click=next):
                pass

def class_section():

    st.markdown("## Class")

    for n in range(ss.num_of_classes):
        c = n+1

        class_ix = f"class_{c}_ix"
        util.initialize_states([class_ix])
        if f"class_{c}_level_ix" not in ss:
            ss[f"class_{c}_level_ix"] = 0
        # class_level_ix = f"class_{c}_level_ix"
        # util.initialize_states([class_ix, class_level_ix])
        ss[f"class_{c}_col1"], ss[f"class_{c}_col2"] = st.columns((7,2))

        util.limit_options(default_options=list(ce.classes.keys()), num_choices=ss.num_of_classes, template="class_")
        util.update_index(f'class_{c}_api', f"class_{c}_ix", ss[f"class_{c}_options"])
        with ss[f"class_{c}_col1"]:
            st.selectbox("Class", ss[f"class_{c}_options"], key=f'class_{c}_api',
                                index=ss[f"class_{c}_ix"], placeholder="Choose a class", label_visibility="collapsed",
                                on_change=util.update_index, args=(f'class_{c}_api', f"class_{c}_ix", ss[f"class_{c}_options"], 
                                                                   {"key": f"class_{c}_level_ix", "value": 0}))
        ss[f'class_{c}'] = ss[f'class_{c}_api']
            
        if ss[f'class_{c}'] is not None:
            ss.classes[c] = ce.classes[ss[f'class_{c}']]()
            with ss[f"class_{c}_col2"]:
                ss[f"class_{c}_level_options"] = list(np.arange(1, 21 - util.count_other_levels(ss.classes, c)))
                ss.classes[c].level = st.selectbox("Level", ss[f"class_{c}_level_options"], key=f"class_{c}_level",
                                index=ss[f"class_{c}_level_ix"], placeholder="Level", label_visibility="collapsed",
                                on_change=util.update_index, args=(f"class_{c}_level", f"class_{c}_level_ix", ss[f"class_{c}_level_options"]))
            ss.classes[c].featureText()
        else:
            with ss[f"class_{c}_col2"]:
                st.selectbox("Level", [], key=f"class_{c}_level_failed", index=None, placeholder="Level", label_visibility="collapsed")
        ss[f"class_{c}_add_col"], ss[f"class_{c}_remove_col"] = st.columns((8,2))
        with ss[f"class_{c}_add_col"]:
            if c in ss.classes and ss.classes[c].level is not None and c == ss.num_of_classes and util.count_other_levels(ss.classes, -1) < 20 and c < len(ce.classes):
                if st.button("Add Class", type="secondary", on_click=add_class):
                    pass
        with ss[f"class_{c}_remove_col"]:
            if c != 1 or (ss[f'class_{c}_api'] is not None and ss[f"class_{c}_level"] is not None):
                if st.button(f"Remove Class", type="secondary", key=f"class_{c}_remove_button", on_click=remove_class, args=[c]):
                    pass


    class_col1, class_col2, class_col3, class_col4, class_col5 = st.columns((2,1,2,1,2))

    with class_col2:
        if st.button("Back", type='primary', on_click=back):
            pass

    with class_col4:
        if ss[f"class_{ss.num_of_classes}_ix"] is None or ss[f"class_{ss.num_of_classes}_level_ix"] is None:
            if st.button("Next", type='primary', on_click=failed_next):
                pass
        else:    
            if st.button("Next", type='primary', on_click=next):
                pass


def scores_section():

    """
    Scores code here
    """

    scores_col1, scores_col2, scores_col3, scores_col4, scores_col5 = st.columns((2,1,2,1,2))

    with scores_col2:
        if st.button("Back", type='primary', on_click=back):
            pass

    with scores_col4:
        if st.button("Next", type='primary', on_click=next):
            pass


def save_section():

    save_col1, save_col2, save_col3, save_col4, save_col5 = st.columns((2,1,2,1,2))

    with save_col2:
        if st.button("Back", type='primary', on_click=back):
            pass

    with save_col4:
        if st.button("Save", type='primary', on_click=save_character):
            pass


if 'section_dict' not in ss:
    ss.section_dict = {1: identity_section,
                       2: class_section,
                       3: scores_section,
                       4: save_section}


def display():

    st.title("Character Builder")
    st.divider()

    ss.section_dict[ss.section_id]()


display()

