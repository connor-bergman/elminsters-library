import streamlit as st
from streamlit import session_state as ss
import reference as ref

# SORCERER

class Sorcerer:
    
    def __init__(self):
        
        self.subclass = None
        self.level = None


    def __repr__(self):
        return "Sorcerer"


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


    def __repr__(self):
        return "Barbarian"
    

# WARLOCK

class Warlock:

    def __init__(self):
        
        self.subclass = None
        self.level = None


    def __repr__(self):
        return "Warlock"
    

# TRACKING IMPLEMENTED CLASSES AND SUBCLASSES

classes = {"Barbarian": Barbarian,
           "Sorcerer": Sorcerer,
           "Warlock": Warlock}

subclasses = {}