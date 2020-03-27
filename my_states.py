from state import State
from config import *

SUMMARIZE_EVENTS = []

class Inhale(State):
    def on_event(self, slope, sample_index, sample_rate):
        if slope < PRESSURE_DECREASE_THRESHOLD:
            print("TIME: " + str(sample_index / sample_rate))
            print("\tINHALE --> EXHALE")
            SUMMARIZE_EVENTS.append(sample_index/sample_rate)
            return Exhale()
        else:
            print("Inhaling...")
            return Inhale()


class Exhale(State):
    def on_event(self, slope, sample_index, sample_rate):
        if abs(slope) < PRESSURE_PLATEAU_THRESHOLD:
            print("TIME: " + str(sample_index / sample_rate))
            print("\tEXHALE --> PLATEAU")
            SUMMARIZE_EVENTS.append(sample_index/sample_rate)
            return Peep()
        else:
            print("Exhaling...")
            return Exhale()

class Peep(State):
    def on_event(self, slope, sample_index, sample_rate):
        if slope > PRESSURE_INCREASE_THRESHOLD:
            print("TIME: " + str(sample_index / sample_rate))
            print("\tPEEP --> INHALE")
            SUMMARIZE_EVENTS.append(sample_index/sample_rate)
            return Inhale()
        else:
            print("PEEP...")
            return Peep()