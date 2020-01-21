from typing import Dict, Text, Any, List, Union

import discord
from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class CharacterCreationForm(FormAction):

    def name(self):
        print('test')
        return "character_form"

    def required_slots(self, tracker) -> List[Text]:
        # return ["id", "name", "strength", "armor", "weapon"]
        return ["name"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": [
                self.from_text(),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(custom=tracker)
        dispatcher.utter_message(template="utter_submit_buy")
        return []
