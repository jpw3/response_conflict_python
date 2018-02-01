#MResponse conflict plotting code
#Author: James Wilmott, Winter 2018

#Designed to plot data from a persistent database
from pylab import *
from matplotlib import patches
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.lines as mlines
import shelve #for database writing and reading

matplotlib.rcParams.update(matplotlib.rcParamsDefault); #restore the default matplotlib styles

datapath = '/Users/jameswilmott/Documents/MATLAB/data/response_conflict/'; 
shelvepath =  '/Users/jameswilmott/Documents/Python/response_conflict/data/'; 
savepath = '/Users/jameswilmott/Documents/Python/response_conflict/figures/';