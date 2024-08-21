import race_engine as re
import class_engine as ce
import json

class Character:

    def __init__(self, json=None):

        if json is not None:
            pass
        else:
            self.reset()

    
    def export(self):
        pass


    def reset(self):    

        self.name = None
        self.race = None
        self.subrace = None
        self.classes = {}

        self.prof_bonus = 2
        self.speed = {}
        self.armor_class = 10
        self.hp_current = 0
        self.hp_max = 0

        self.base_abilities = {"Strength": 8,
                          "Dexterity": 8,
                          "Constitution": 8,
                          "Intelligence": 8,
                          "Wisdom": 8,
                          "Charisma": 8}
        
        self.skill_profs = {"Acrobatics": 0,
                            "Animal Handling": 0,
                            "Arcana": 0,
                            "Athletics": 0,
                            "Deception": 0,
                            "History": 0,
                            "Insight": 0,
                            "Intimidation": 0,
                            "Investigation": 0,
                            "Medicine": 0,
                            "Nature": 0,
                            "Perception": 0,
                            "Performance": 0,
                            "Persuasion": 0,
                            "Religion": 0,
                            "Sleight of Hand": 0,
                            "Stealth": 0,
                            "Survival": 0}
        
        self.feats = []
        self.armor_profs = []
        self.weapon_profs = []
        self.tool_profs = []
        self.languages = {}
        self.size = ""

        self.spells = {}


    def score_to_mod(score):
        return int(score/2) - 5

    
    def apply_modifiers(self):
        pass

