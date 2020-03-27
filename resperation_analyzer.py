from my_states import Peep
import numpy as np
from scipy.stats import linregress

from config import *

class ResperationAnalyzer(object):
    def __init__(self, sample_rate, window_size=WINDOW_SIZE):
        self.state = Peep()
        self.window_size = window_size
        self.window = [0 for i in range(WINDOW_SIZE)]
        self.is_window_full = False
        self.curr_window_index = 0
        self.sample_rate = sample_rate

    def on_event(self, curr_sample, sample_index):
        if(not self.is_window_full):
            # Set new sample in window
            self.window[self.curr_window_index] = curr_sample
            self.curr_window_index += 1

            # Check if window is full
            if self.curr_window_index >= self.window_size:
                self.is_window_full = True

        else:
            # Update window
            self.window.append(curr_sample)
            self.window.pop(0)

            # Use linear regression to asses slope
            half_window_size = int((self.window_size-1)/2)
            X = [i/self.sample_rate for i in range(-half_window_size,half_window_size+1)]
            slope = linregress(X, self.window).slope

            self.state = self.state.on_event(slope, sample_index, self.sample_rate)