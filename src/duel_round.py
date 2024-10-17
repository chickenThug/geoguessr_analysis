from datetime import datetime
from location import Location
import pycountry

class DuelRound:
    def __init__(self, round_number, duel_id, timestamp, oliver_guess, viggo_guess, us_score, 
                 best_opponent_guess, opponent_score, country_code, round_location, state):
        self.round_number = round_number
        self.duel_id = duel_id
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        self.oliver_guess = tuple(oliver_guess.split(", "))
        self.viggo_guess = tuple(viggo_guess.split(", "))
        self.us_score = us_score
        self.best_opponent_guess = tuple(best_opponent_guess.split(", "))
        self.opponent_score = opponent_score
        self.country_code = country_code
        self.round_location = tuple(round_location.split(", "))
        self.game_mode = state

        # Initialize Location objects for all coordinates
        self.round_location = Location(*round_location.split(", "))
        self.oliver_location = Location(*oliver_guess.split(", "))
        self.viggo_location = Location(*viggo_guess.split(", "))
        self.opponent_location = Location(*best_opponent_guess.split(", "))

        # Extract country and state details from locations
        self.oliver_country = self.oliver_location.get_country_name()
        self.viggo_country = self.viggo_location.get_country_name()
        self.opponent_country = self.opponent_location.get_country_name()
        self.round_country = self.round_location.get_country_name()

        self.oliver_state = self.oliver_location.get_state()
        self.viggo_state = self.viggo_location.get_state()
        self.opponent_state = self.opponent_location.get_state()
        self.round_state = self.round_location.get_state()

        # Sanity check for round location country match
        self.country_match = (self.round_location.get_country_code() == self.country_code)
