from state import State
from config import *

SUMMARIZE_EVENTS = []

class Inhale(State):
    def on_event(self, slope, event_time):
        if slope < PRESSURE_DECREASE_THRESHOLD:
            print("TIME: " + str(event_time))
            print("\tINHALE --> EXHALE")
            SUMMARIZE_EVENTS.append(event_time)
            return Exhale()
        else:
            print("Inhaling...")
            return Inhale()


class Exhale(State):
    def on_event(self, slope, event_time):
        if abs(slope) < PRESSURE_PLATEAU_THRESHOLD:
            print("TIME: " + str(event_time))
            print("\tEXHALE --> PLATEAU")
            SUMMARIZE_EVENTS.append(event_time)
            return Peep()
        else:
            print("Exhaling...")
            return Exhale()

class Peep(State):
    def on_event(self, slope, event_time):
        if slope > PRESSURE_INCREASE_THRESHOLD:
            print("TIME: " + str(event_time))
            print("\tPEEP --> INHALE")
            SUMMARIZE_EVENTS.append(event_time)
            return Inhale()
        else:
            print("PEEP...")
            return Peep()