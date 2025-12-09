from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSelectDelivery(Action):
    def name(self) -> Text:
        return "action_select_delivery"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        car_model = tracker.get_slot("car_model")
        color = tracker.get_slot("color")
        delivery_date = tracker.get_slot("delivery_date")

        if not (car_model and color and delivery_date):
            dispatcher.utter_message(text="Please provide all details: model, color, and delivery date.")
            return []

        message = f"✅ Thank you {name}! Your {color} {car_model} is scheduled for delivery on {delivery_date}."
        dispatcher.utter_message(text=message)

        return [SlotSet("car_model", car_model),
                SlotSet("color", color),
                SlotSet("delivery_date", delivery_date)]

class ActionRescheduleDelivery(Action):
    def name(self) -> Text:
        return "action_reschedule_delivery"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new_date = tracker.get_slot("delivery_date")
        dispatcher.utter_message(
            text=f"✅ Your delivery has been rescheduled to {new_date}. We’ll send a confirmation message soon!"
        )
        return []

class ActionCheckStatus(Action):
    def name(self) -> Text:
        return "action_check_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        car_model = tracker.get_slot("car_model") or "your car"
        delivery_date = tracker.get_slot("delivery_date") or "soon"
        dispatcher.utter_message(
            text=f"🚗 The {car_model} is being prepared for delivery. Expected date: {delivery_date}."
        )
        return []
class ActionFeeInfo(Action):
    def name(self) -> str:
        return "utter_fee_info"  # same as your story/rule reference

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict):

        course = tracker.get_slot("course")

        # Example fee structure
        fee_data = {
            "btech": "₹1,50,000 per year",
            "mba": "₹2,00,000 per year",
            "bba": "₹1,20,000 per year",
            "mbbs": "₹15,00,000 per year"
        }

        if course and course.lower() in fee_data:
            message = f"The fee for {course.upper()} is {fee_data[course.lower()]}."
        else:
            message = "Fees vary by course. Please specify your course name (e.g., B.Tech, MBA) to get details."

        dispatcher.utter_message(text=message)