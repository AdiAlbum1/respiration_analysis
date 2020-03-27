import numpy as np
import math

def create_sin_signal(sample_rate, amplitude, freq, t):	
	num_samples = int(sample_rate * t)
	signal = [amplitude * math.sin(2 * np.pi * i * freq / sample_rate) for i in range(num_samples)]
	return signal

def add_noise_to_signal(signal, sigma):
	for i in range(len(signal)):
		signal[i] += np.random.normal(scale=sigma)
	return signal

def truncate_signal(signal):
	truncate_signal = [max(sample, 0) for sample in signal]
	return truncate_signal

def generate_signal(sample_rate, amplitude, freq, t, sigma):
	my_signal = create_sin_signal(sample_rate, amplitude, freq, t)
	my_signal = truncate_signal(my_signal)
	my_signal = add_noise_to_signal(my_signal, sigma)

	return my_signal