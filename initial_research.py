import numpy as np
import scipy.fftpack as fftpack
from scipy.signal import butter,filtfilt
from scipy.stats import linregress
from matplotlib import pyplot as plt
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

def determine_derivative_sign(signal, window_size, sample_rate, epsilon=10**-8):
	half_window_size = int((window_size-1)/2)
	linear_regression_result = np.zeros(len(signal))
	derivative_signs = np.zeros(len(signal))

	for i in range(half_window_size,len(signal)-half_window_size):

		# CURRENT WINDOW
		X = [i/sample_rate for i in range(-half_window_size,half_window_size+1)]
		Y = signal[i-half_window_size: i+half_window_size+1]		

		# Linear regression
		linear_regression_result[i] = linregress(X, Y).slope

		# Sign
		if linear_regression_result[i] > epsilon:
			derivative_signs[i] = 1
		elif linear_regression_result[i] < -epsilon:
			derivative_signs[i] = -1
		else:
			derivative_signs[i] = 0

	return derivative_signs

if __name__ == "__main__":
	AMPLITUDE = 10
	SAMPLE_RATE = 50
	FREQ = 0.4
	T = 10

	NOISE_SIGMA = 0.05
	WINDOW_SIZE = 21

	my_signal = create_sin_signal(SAMPLE_RATE, AMPLITUDE, FREQ, T)
	my_signal = truncate_signal(my_signal)
	my_signal = add_noise_to_signal(my_signal, NOISE_SIGMA)

	derivative_sign = determine_derivative_sign(my_signal, WINDOW_SIZE, SAMPLE_RATE, epsilon=0.5)

	## PLOT
	x_axis = [i/SAMPLE_RATE for i in range(len(my_signal))]

	plt.subplot(2, 1, 1)
	plt.plot(x_axis, my_signal)
	plt.title("Signal")

	plt.subplot(2, 1, 2)
	plt.plot(x_axis, derivative_sign)
	plt.title("Linear Regression - Derivative sign")

	plt.show()