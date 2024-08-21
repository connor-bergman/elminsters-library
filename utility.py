import streamlit as st
from streamlit import session_state as ss


def display_spell():
    pass


def remove_states(state_list):
    for state in state_list:
        if state in ss:
            del ss[state]


def reassign_states(states_to_reassign):
    for target, source in states_to_reassign:
        if source in ss: 
            if target in ss:  
                del ss[target]
            ss[target] = ss[source]


def initialize_states(state_list):
    for state in state_list:
        if state not in ss:
            ss[state] = None


def update_index(key, index, options):
    if key in ss:
        selection = ss[key]
        if selection in options:
            ss[index] = options.index(selection)
        else:
            ss[index] = None


def count_other_levels(classes, ix_to_ignore):
    lvl_count = 0
    for c in classes:
        if c != ix_to_ignore and f"class_{c}_level" in ss and ss[f"class_{c}_level"] is not None:
            lvl_count += ss[f"class_{c}_level"]
    return lvl_count


def limit_options(default_options, num_choices, template):
    for i in range(1, num_choices+1):
        ss[f"{template}{i}_options"] = default_options.copy()
        for j in range(1, num_choices+1):
            if i != j and f"{template}{j}" in ss:
                ss[f"{template}{i}_options"] = [ablty for ablty in ss[f"{template}{i}_options"] if ablty != ss[f"{template}{j}"]]


def dependent_selectboxes(template, num_boxes, default_options, placeholder, object, object_key):
    for i in range(1,num_boxes+1):
        limit_options(default_options, num_boxes, template)
        update_index(f'{template}{i}', f'{template}{i}_ix', ss[f"{template}{i}_options"])
        object.choices[f'{object_key}{i}'] = st.selectbox(label=template, options=ss[f"{template}{i}_options"], key=f'{template}{i}',
                                                 index=ss[f'{template}{i}_ix'], placeholder=placeholder, label_visibility="collapsed",
                                                 on_change=update_index, args=(f'{template}{i}', f'{template}{i}_ix', ss[f"{template}{i}_options"]))