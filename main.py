from resperation_analyzer import ResperationAnalyzer
import time
from signal_generator import generate_signal
from my_states import SUMMARIZE_EVENTS

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from config import *

def aux_plot(signal, summarized_events, sample_rate):
	X = [i / sample_rate for i in range(len(signal))]

	inhale_events = summarized_events[::3]
	exhale_events = summarized_events[1::3]
	PEEP_events = summarized_events[2::3]

	plt.plot(X, signal)
	for event in inhale_events:
		plt.axvline(x=event, color='r')

	for event in exhale_events:
		plt.axvline(x=event, color='g')

	for event in PEEP_events:
		plt.axvline(x=event, color='b')

	red_patch = mpatches.Patch(color='red', label='PEEP --> Inhale')
	green_patch = mpatches.Patch(color='green', label='Inhale --> Exhale')
	blue_patch = mpatches.Patch(color='blue', label='Exhale --> PEEP')
	plt.legend(handles=[red_patch, green_patch, blue_patch])

	plt.ylabel("Pressure(cmH2O)")
	plt.xlabel("t(s)")

	plt.xlim(left=2.3)

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