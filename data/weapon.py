from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class Weapon:
    def __init__(self, name, die, element):
        self.name = name
        self.die = die
        self.element = element

class Character:
    def __init__(self, id, name, strength, armor, weapon):
        self.id = id
        self.name = name
        self.strength = strength
        self.armor = armor
        self.weapon = weapon

    def attack(self):
        return True

    @staticmethod
    def createCharacter():
        character = Character

        return character
