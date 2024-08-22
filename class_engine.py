import streamlit as st
from streamlit import session_state as ss
import reference as ref

# SORCERER

class Sorcerer:
    
    def __init__(self):
        
        self.subclass = None
        self.level = None

        self.attributes = {"hit_dice": 6,
                           "weapon_profs": ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
                           "saving_throws": ["Constitution", "Charisma"]}

        self.choices = {"lvl0_skill_prof1": None,
                        "lvl0_skill_prof2": None}

        self.subclass_list = {"Aberrant Mind": AberrantMind}


    def __repr__(self):
        return "Sorcerer"


    def featureText(self):
        if self.level is None or self.level >= 1:
            st.markdown("""Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, 
                        or exposure to unknown cosmic forces. One can’t study sorcery as one learns a language, any more than one can 
                        learn to live a legendary life. No one chooses sorcery; the power chooses the sorcerer.""")
        if self.level is not None:
            if self.level >= 1:
                pass
            if self.level >= 2:
                pass
            if self.level >= 3:
                pass
            if self.level >= 4:
                pass
            if self.level >= 5:
                pass
            if self.level >= 6:
                pass
            if self.level >= 7:
                pass
            if self.level >= 8:
                pass
            if self.level >= 9:
                pass
            if self.level >= 10:
                pass
            if self.level >= 11:
                pass
            if self.level >= 12:
                pass
            if self.level >= 13:
                pass
            if self.level >= 14:
                pass
            if self.level >= 15:
                pass
            if self.level >= 16:
                pass
            if self.level >= 17:
                pass
            if self.level >= 18:
                pass
            if self.level >= 19:
                pass
            if self.level == 20:
                pass


class AberrantMind:

    def __init__(self):
        pass


    def __repr__(self):
        return "Aberrant Mind"
    

# BARBARIAN

class Barbarian:

    def __init__(self):
        
        self.subclass = None
        self.level = None

        self.attributes = {}

        self.choices = {}

        self.subclass_list = {"Path of Wild Magic": PathOfWildMagic}


    def __repr__(self):
        return "Barbarian"
    

    def featureText(self):
        if self.level is None or self.level >= 1:
            st.write("""For some barbarians, their rage springs from a communion with fierce animal spirits. Others draw from a roiling 
                     reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a 
                     battle frenzy but also uncanny reflexes, resilience, and feats of strength.""")
        if self.level is not None:
            if self.level >= 1:
                pass
            if self.level >= 2:
                pass
            if self.level >= 3:
                pass
            if self.level >= 4:
                pass
            if self.level >= 5:
                pass
            if self.level >= 6:
                pass
            if self.level >= 7:
                pass
            if self.level >= 8:
                pass
            if self.level >= 9:
                pass
            if self.level >= 10:
                pass
            if self.level >= 11:
                pass
            if self.level >= 12:
                pass
            if self.level >= 13:
                pass
            if self.level >= 14:
                pass
            if self.level >= 15:
                pass
            if self.level >= 16:
                pass
            if self.level >= 17:
                pass
            if self.level >= 18:
                pass
            if self.level >= 19:
                pass
            if self.level == 20:
                pass


class PathOfWildMagic:

    def __init__(self):
        pass


    def __repr__(self):
        return "Path of Wild Magic"
    

# WARLOCK

class Warlock:

    def __init__(self):
        
        self.subclass = None
        self.level = None

        self.attributes = {}

        self.choices = {}

        self.subclass_list = {"The Hexblade": TheHexblade}


    def __repr__(self):
        return "Warlock"
    

    def featureText(self):
        if self.level is None or self.level >= 1:
            st.write("""Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse. Through pacts 
                     made with mysterious beings of supernatural power, warlocks unlock magical effects both subtle and spectacular. 
                     Drawing on the ancient knowledge of beings such as fey nobles, demons, devils, hags, and alien entities of the 
                     Far Realm, warlocks piece together arcane secrets to bolster their own power.""")
        if self.level is not None:
            if self.level >= 1:
                pass
            if self.level >= 2:
                pass
            if self.level >= 3:
                pass
            if self.level >= 4:
                pass
            if self.level >= 5:
                pass
            if self.level >= 6:
                pass
            if self.level >= 7:
                pass
            if self.level >= 8:
                pass
            if self.level >= 9:
                pass
            if self.level >= 10:
                pass
            if self.level >= 11:
                pass
            if self.level >= 12:
                pass
            if self.level >= 13:
                pass
            if self.level >= 14:
                pass
            if self.level >= 15:
                pass
            if self.level >= 16:
                pass
            if self.level >= 17:
                pass
            if self.level >= 18:
                pass
            if self.level >= 19:
                pass
            if self.level == 20:
                pass


class TheHexblade:

    def __init__(self):
        pass


    def __repr__(self):
        return "The Hexblade"
    

# TRACKING IMPLEMENTED CLASSES AND SUBCLASSES

classes = {# "Artificer": Artificer
           "Barbarian": Barbarian,
           # "Bard": Bard,
           # "Cleric": Cleric,
           # "Druid": Druid,
           # "Fighter": Fighter,
           # "Monk": Monk,
           # "Paladin": Paladin,
           # "Ranger": Ranger,
           # "Rogue": Rogue,
           "Sorcerer": Sorcerer,
           "Warlock": Warlock,
           # "Wizard": Wizard 
           }
