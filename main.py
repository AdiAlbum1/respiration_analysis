from resperation_analyzer import ResperationAnalyzer
import time
from signal_generator import generate_signal
from my_states import SUMMARIZE_EVENTS

from matplotlib import pyplot as plt

from config import *

def aux_plot(signal, summarized_events, sample_rate):
	X = [i / sample_rate for i in range(len(signal))]

	plt.plot(X, signal)
	for event in summarized_events:
		plt.axvline(x=event)

	plt.show()

if __name__ == "__main__":

	# Generating Signal...
	signal = generate_signal(SAMPLE_RATE, AMPLITUDE, FREQ, T, NOISE_SIGMA)

	# Initialize resperation analyzer object
	resperation_analyzer = ResperationAnalyzer(SAMPLE_RATE)

	# Analyze each new sample
	for sample_index in range(T * SAMPLE_RATE):
		time.sleep(SLEEP_TIME)
		curr_sample = signal[sample_index]
		resperation_analyzer.on_event(curr_sample, sample_index)


	print("DONE!!!!!")

	# Summarize...
	aux_plot(signal, SUMMARIZE_EVENTS, SAMPLE_RATE)