import plotly.plotly as py
import math
def expand(x):
    yield x.name
    while x.payload:
        x = x.payload
        yield x.name
'''
Encapsulation of division for clarification
'''
def P(x, total):
	return x/float(total)

'''
Given a probability of a symbol returns the information of the symbol 
'''
def I(p):
	return -math.log(p, 2)

'''
Symbol entropy
'''
def Ei(x, total):
	pi = P(x, total)
	return pi*I(pi)

'''
Plots figure into the file named <plot_name>_<input_file_name> 
'''
def saveFigure(figure, input_file_name):
    name = figure.name()+"_" + input_file_name.replace('pcap', 'png') 
    py.image.save_as(figure.figure, filename=name)