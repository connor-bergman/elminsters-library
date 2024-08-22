import streamlit as st
import reference as ref
import utility as util
from streamlit import session_state as ss
        

# HUMANS
        
class Human:

    def __init__(self):

        self.attributes = {"size": "Medium",
                            "speed": {"Walk": 30},
                            "languages": ["Common"]}
        
        self.choices = {"language": None}
        
        self.subrace = None

        self.subrace_list = {"Basic Human": BasicHuman,
                             "Variant Human": VariantHuman}
        
    
    def __repr__(self):
        return "Human"
    

    def traitText(self):

        util.initialize_states(['human_language_ix'])

        st.markdown("### Human Traits")
        st.markdown("""It’s hard to make generalizations about humans, but your human character has these traits.""")
        st.markdown("#### Age")
        st.markdown("""Humans reach adulthood in their late teens and live less than a century.""")
        st.markdown("#### Size")
        st.markdown("""Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. 
                    Regardless of your position in that range, your size is Medium.""")
        st.markdown("#### Speed")
        st.markdown("""Your base walking speed is 30 feet.""")
        st.markdown("#### Languages")
        st.markdown("""You can speak, read, and write Common and one extra language of your choice. Humans typically 
                    learn the languages of other peoples they deal with, including obscure dialects. They are fond 
                    of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical 
                    expressions, Dwarvish military phrases, and so on.""")
        langs_to_choose = [lang for lang in ref.languages if lang != "Common"]
        self.choices["language"] = st.selectbox("Extra Language", langs_to_choose, key='human_language',
                                   index=ss.human_language_ix, placeholder="Choose a language", label_visibility="collapsed",
                                   on_change=util.update_index, args=('human_language', 'human_language_ix', langs_to_choose))

    
    def chooseSubrace(self):

        util.initialize_states(['human_subrace_ix'])

        st.markdown("## Subrace")
        sr_choice = st.selectbox("Subrace", self.subrace_list.keys(), key = 'human_subrace',
                                 index=ss.human_subrace_ix, placeholder="Choose a subrace", label_visibility="collapsed",
                                 on_change=util.update_index, args=('human_subrace', 'human_subrace_ix', list(self.subrace_list.keys())))
        
        if sr_choice is not None:
            self.subrace = self.subrace_list[sr_choice]()
            self.subrace.traitText()
        

class BasicHuman:
    
    def __init__(self):

        self.attributes = {"asi": {key: 1 for key in ref.abilities}}

        self.choices = {}


    def __repr__(self):
        return "Basic Human"

    
    def traitText(self):

        st.markdown("### Basic Human Traits")
        st.markdown("#### Ability Score Increase")
        st.markdown("""Your ability scores each increase by 1.""")


class VariantHuman:
    
    def __init__(self):

        self.attributes = {}
        
        self.choices = {'asi1': None,
                        'asi2': None,
                        'skill_prof': None,
                        'feat': None}


    def __repr__(self):
            return "Variant Human"


    def traitText(self):

        util.initialize_states(['vhuman_asi1_ix', 'vhuman_asi2_ix', 'vhuman_skill_prof_ix', 'vhuman_feat_ix'])
        
        st.markdown("### Variant Human Traits")
        st.markdown("#### Ability Score Increase")
        st.markdown("""Two different ability scores of your choice increase by 1.""")
        util.dependent_selectboxes(template='vhuman_asi', num_boxes=2, default_options=ref.abilities,
                                   placeholder="Choose an ability", object=self, object_key="asi")
        st.markdown("#### Skills")
        st.markdown("""You gain proficiency in one skill of your choice.""")
        self.choices['skill_prof'] = st.selectbox("Skill Proficiency", ref.skills, key='vhuman_skill_prof',
                                         index=ss.vhuman_skill_prof_ix, placeholder="Choose a skill", label_visibility="collapsed",
                                         on_change=util.update_index, args=('vhuman_skill_prof', 'vhuman_skill_prof_ix', ref.skills))
        st.markdown("#### Feat")
        st.markdown("""You gain one feat of your choice.""")
        self.choices['feat'] = st.selectbox("Feat", ref.feats, key='vhuman_feat',
                                   index=ss.vhuman_feat_ix, placeholder="Choose a feat", label_visibility="collapsed",
                                   on_change=util.update_index, args=('vhuman_feat', 'vhuman_feat_ix', ref.feats))



# ELVES

class Elf:

    def __init__(self):

        self.attributes = {"size": "Medium",
                           "speed": {"Walk": 30},
                           "skill_profs": ["Perception"],
                           "languages": ["Common", "Elvish"],
                           "asi": {"Dexterity": 2}}
        
        self.choices = {}
        
        self.subrace = None

        self.subrace_list = {"Drow": Drow, 
                             "Eladrin": Eladrin, 
                             "High Elf": HighElf}

    
    def __repr__(self):
        return "Elf"
    

    def traitText(self):
        st.markdown("### Elf Traits")
        st.markdown("""Your elf character has a variety of natural abilities, the result of thousands of years 
                    of elven refinement.""")
        st.markdown("#### Ability Score Increase")
        st.markdown("Your Dexterity score increases by 2.")
        st.markdown("#### Age")
        st.markdown("""Although elves reach physical maturity at about the same age as humans, 
                    the elven understanding of adulthood goes beyond physical growth to encompass worldly 
                    experience. An elf typically claims adulthood and an adult name around the age of 100 and 
                    can live to be 750 years old.""")
        st.markdown("#### Size")
        st.markdown("""Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.""")
        st.markdown("#### Speed")
        st.markdown("""Your base walking speed is 30 feet.""")
        st.markdown("#### Darkvision")
        st.markdown("""Accustomed to twilit forests and the night sky, you have superior vision in dark and 
                    dim conditions. You can see in dim light within 60 feet of you as if it were bright 
                    light, and in darkness as if it were dim light. You can’t discern color in darkness, 
                    only shades of gray.""")
        st.markdown("#### Keen Senses")
        st.markdown("""You have proficiency in the Perception skill.""")
        st.markdown("#### Fey Ancestry")
        st.markdown("""You have advantage on saving throws against being charmed, and magic can’t put you to sleep.""")
        st.markdown("#### Trance")
        st.markdown("""Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 
                    hours a day. (The Common word for such meditation is “trance.”) While meditating, you can 
                    dream after a fashion; such dreams are actually mental exercises that have become reflexive 
                    through years of practice. After resting in this way, you gain the same benefit that a 
                    human does from 8 hours of sleep.""")
        st.markdown("#### Languages")
        st.markdown("""You can speak, read, and write Common and Elvish. Elvish is fluid, with subtle intonations 
                    and intricate grammar. Elven literature is rich and varied, and their songs and poems are 
                    famous among other races. Many bards learn their language so they can add Elvish ballads 
                    to their repertoires.""")
    

    def chooseSubrace(self):
        
        util.initialize_states(['elf_subrace_ix'])

        sr_choice = st.selectbox("Subrace", self.subrace_list.keys(), key = 'elf_subrace',
                                 index=ss.elf_subrace_ix, placeholder="Choose a subrace", label_visibility="collapsed",
                                 on_change=util.update_index, args=('elf_subrace', 'elf_subrace_ix', list(self.subrace_list.keys())))
        
        if sr_choice is not None:
            self.subrace = self.subrace_list[sr_choice]()
            self.subrace.traitText()


class Drow:
    pass


class Eladrin:
    pass


class HighElf:
    pass



# HALF-ELVES

class HalfElf:

    def __init__(self):

        self.attributes = {"size": "Medium",
                           "speed": {"Walk": 30},
                           "languages": ["Common", "Elvish"],
                           "asi": {"Charisma": 2}}
        
        self.choices = {"asi1": None,
                        "asi2": None,
                        "skill_prof1": None,
                        "skill_prof2": None,
                        "language": None}

    
    def __repr__(self):
        return "Half-Elf"
    

    def traitText(self):

        util.initialize_states(['halfelf_asi1_ix', 'halfelf_asi2_ix', 'halfelf_skill_prof1_ix', 'halfelf_skill_prof2_ix', 'halfelf_language_ix'])

        st.markdown("### Half-Elf Traits")
        st.markdown("""Your half-elf character has some qualities in common with elves and some that 
                    are unique to half-elves.""")
        st.markdown("#### Ability Score Increase")
        st.markdown("""Your Charisma score increases by 2, and two other ability scores of your choice increase by 1.""")
        util.dependent_selectboxes(template='halfelf_asi', num_boxes=2, default_options=ref.abilities,
                                   placeholder="Choose an ability", object=self, object_key="asi")
        st.markdown("#### Age")
        st.markdown("""Half-elves mature at the same rate humans do and reach adulthood around the age of 20. 
                    They live much longer than humans, however, often exceeding 180 years.""")
        st.markdown("#### Size")
        st.markdown("""Half-elves are about the same size as humans, ranging from 5 to 6 feet tall. 
                    Your size is Medium.""")
        st.markdown("#### Speed")
        st.markdown("""Your base walking speed is 30 feet.""")
        st.markdown("#### Darkvision")
        st.markdown("""Thanks to your elf blood, you have superior vision in dark and dim conditions. 
                    You can see in dim light within 60 feet of you as if it were bright light, 
                    and in darkness as if it were dim light. You can’t discern color in darkness, 
                    only shades of gray.""")
        st.markdown("#### Fey Ancestry")
        st.markdown("""You have advantage on saving throws against being charmed, and magic can’t put you to sleep.""")
        st.markdown("#### Skill Versatility")
        st.markdown("""You gain proficiency in two skills of your choice.""")
        util.dependent_selectboxes(template="halfelf_skill_prof", num_boxes=2, default_options=ref.skills,
                                   placeholder="Choose a skill", object=self, object_key="skill_prof")
        st.markdown("#### Languages")
        st.markdown("""You can speak, read, and write Common, Elvish, and one extra language of your choice.""")
        langs_to_choose = [lang for lang in ref.languages if lang not in ["Common", "Elvish"]]
        self.choices["language"] = st.selectbox("Extra Language", langs_to_choose, key='halfelf_language',
                                   index=ss.halfelf_language_ix, placeholder="Choose a language", label_visibility="collapsed",
                                   on_change=util.update_index, args=('halfelf_language', 'halfelf_language_ix', langs_to_choose))




# TRACKING IMPLEMENTED RACES AND SUBRACES

races = {"Elf": Elf,
         'Half-Elf': HalfElf,
         "Human": Human}



