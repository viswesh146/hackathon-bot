from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from pandas import read_sql
from dbutil import cnx


class ActionSearchConcerts(Action):
    def name(self):
        return "action_search_concerts"

    def run(self, dispatcher, tracker, domain):
        concerts = [
            {"artist": "Foo Fighters", "reviews": 4.5},
            {"artist": "Katy Perry", "reviews": 5.0},
        ]
        description = ", ".join([c["artist"] for c in concerts])
        dispatcher.utter_message(text=f"{description}")
        return [SlotSet("concerts", concerts)]


class ActionSearchVenues(Action):
    def name(self):
        return "action_search_venues"

    def run(self, dispatcher, tracker, domain):
        venues = [
            {"name": "Big Arena", "reviews": 4.5},
            {"name": "Rock Cellar", "reviews": 5.0},
        ]
        dispatcher.utter_message(text="here are some venues I found")
        description = ", ".join([c["name"] for c in venues])
        dispatcher.utter_message(text=f"{description}")
        return [SlotSet("venues", venues)]


class ActionShowConcertReviews(Action):
    def name(self):
        return "action_show_concert_reviews"

    def run(self, dispatcher, tracker, domain):
        concerts = tracker.get_slot("concerts")
        dispatcher.utter_message(text=f"concerts from slots: {concerts}")
        return []


class ActionShowVenueReviews(Action):
    def name(self):
        return "action_show_venue_reviews"

    def run(self, dispatcher, tracker, domain):
        venues = tracker.get_slot("venues")
        dispatcher.utter_message(text=f"venues from slots: {venues}")
        return []


class ActionSetMusicPreference(Action):
    def name(self):
        return "action_set_music_preference"

    def run(self, dispatcher, tracker, domain):
        """Sets the slot 'likes_music' to true/false dependent on whether the user
        likes music"""
        intent = tracker.latest_message["intent"].get("name")

        if intent == "affirm":
            return [SlotSet("likes_music", True)]
        elif intent == "deny":
            return [SlotSet("likes_music", False)]
        return []

class ActionFindDomainDetails(Action):
    def name(self):
        return "action_find_domain_details"

    def run(self, dispatcher, tracker, domain):
        """Sets the slot 'likes_music' to true/false dependent on whether the user
        likes music"""
        intent = tracker.latest_message["intent"].get("name")
        alexa_score = 20
        dispatcher.utter_message(text=f"Alexa score is: {alexa_score}")
        return []

class ActionFindCompanyRevenue(Action):
    def name(self):
        return "action_find_company_revenue"

    def run(self, dispatcher, tracker, domain):
        """Sets the slot 'likes_music' to true/false dependent on whether the user
        likes music"""
        intent = tracker.latest_message["intent"].get("name")
        alexa_score = 20
        dispatcher.utter_message(text=f"Alexa score is: {alexa_score}")
        return []

class ActionFindEmployeeCount(Action):
    def name(self):
        return "action_find_employee_count"

    def run(self, dispatcher, tracker, domain):
        """Sets the slot 'likes_music' to true/false dependent on whether the user
        likes music"""
        intent = tracker.latest_message["intent"].get("name")
        alexa_score = 20
        dispatcher.utter_message(text=f"Alexa score is: {alexa_score}")
        return []

class ActionFindCompanyScore(Action):
    def name(self):
        return "action_find_company_score"

    def run(self, dispatcher, tracker, domain):
        """Sets the slot 'likes_music' to true/false dependent on whether the user
        likes music"""

        intent = tracker.latest_message["intent"].get("name")
        entities = tracker.latest_message.get("entities")
        if len(entities)>0:
            print(entities)
            domain_name = entities[0].get('value')
            query = "select cy from appcache.company where website = " \
                    f"'{domain_name}'"
            dispatcher.utter_message("Fetching your data, please wait")
            df = read_sql(query, cnx)
            try:
                cyence_score = int(df['cy'])
            except:
                cyence_score = 0

            dispatcher.utter_message(text=f"Cyence score is: {cyence_score}")
        else:
            dispatcher.utter_message("No domains found")
        return []