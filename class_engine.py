import streamlit as st
from streamlit import session_state as ss
import reference as ref

# SORCERER

class Sorcerer:
    
    def __init__(self):
        
        self.subclass = None
        self.level = None

        self.choices = {}

        self.subclass_list = ["Aberrant Mind"]


    def __repr__(self):
        return "Sorcerer"


    def featureText(self):
        if self.level is None:
            return
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

        self.choices = {}

        self.subclass_list = ["Path of Wild Magic"]


    def __repr__(self):
        return "Barbarian"
    

    def featureText(self):
        if self.level is None:
            return
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

        self.choices = {}

        self.subclass_list = ["The Hexblade"]


    def __repr__(self):
        return "Warlock"
    

    def featureText(self):
        if self.level is None:
            return
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

classes = {"Barbarian": Barbarian,
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

subclasses = {""}