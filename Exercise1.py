import matplotlib.pyplot as plt
import numpy
from sys import stdin
from scipy.misc import factorial


def draw_functions(ran, scale = "linear"):
	"""A function that, given an integer used as an upper limit and a 
	valid argument for matplotlib.pyplot.yscale, plots a maximum of ten 
	points ranging from one to the given upper limit using the given 
	scale on the y-axis"""
	x = numpy.arange(1, ran, max(ran//10, 1))
	y_factorial = factorial(x)
	y_exponential = numpy.power([2]*len(x),x)
	y_quadratic = numpy.power(x,2)
	y_linear = x
	y_square_root = numpy.power(x,0.5)
	y_log = numpy.log(x)
	
	#print(y_exponential, y_factorial)
	
	plt.plot(x, y_factorial, label="factorial")
	plt.plot(x, y_exponential, label="exponential")
	plt.plot(x, y_quadratic, label="quadratic")
	plt.plot(x, y_linear, label="linear")
	plt.plot(x, y_square_root, label="square root")
	plt.plot(x, y_log, label="log")
	plt.yscale(scale)
	#plt.ylim(1000)
	plt.legend()
	plt.show()

if __name__=="__main__":
	valid_plt_scales = ["linear", "log", "symlog", "logit"]
	scale = ""
	print("\n\nHi, which scale shall we use for our plots today?" +
	"\n\nAvailable options include linear, log, symlog, and logit\n")
	scale = stdin.readline().strip()
	while(scale not in valid_plt_scales):
		print("\nSorry, " + scale + 
		"is not one of the is not one of the available scales\n" +
		"Available options include linear, log, symlog, and logit\n")
		scale = stdin.readline().strip()
	print("\nUp to which number do you want me to plot?\n")
	while 1:
		try:
			ran = int(stdin.readline().strip())
			break
		except:
			print("\nPlot limits must be integers; please enter a " +
			"valid value.\n")
	draw_functions(ran, scale)
