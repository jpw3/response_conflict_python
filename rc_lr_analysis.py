#Response Conflict Data Analysis code
#Author: James Wilmott, Winter 2018

#Designed to import et_mt data and analyze it

from pylab import *
import shelve #for database writing and reading
from scipy.io import loadmat #used to load .mat files in as dictionaries
from scipy import stats
from glob import glob #for use in searching for/ finding data files
import random #general purpose
import pandas as pd
pc = lambda x:sum(x)/float(len(x)); #create a percent correct lambda function

datapath = '/Users/jameswilmott/Documents/MATLAB/data/response_conflict/'; 
shelvepath =  '/Users/jameswilmott/Documents/Python/response_conflict/data/'; 
savepath = '/Users/jameswilmott/Documents/Python/response_conflict/data/';

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'rc_data');
individ_subject_data = shelve.open(shelvepath+'individ_rc_data');

ids=['jpw'];

## Data Analysis Methods ####################################################################################################





## Data Importation Functions

#define a function to import individual .mat data files
def loadBlock(subid,block_nr):
	#returns a single Block object corresponding to the block number and subject id
	#block type should be a string corresponding to the task type(e.g. 'Discrim')
	filename = glob(datapath+'%s'%subid+'/'+'*_%s_%d.mat'%(subid,block_nr)); #block_type,
	matdata = loadmat(filename[0],struct_as_record=False,squeeze_me=True)['block']; #use scipy loadmat() to load in the files
	block=Block(matdata); #here, create Block object with dictionary of trial data in matdata
	return block;

#define a function to import all .mat data files for a given subject
def loadAllBlocks(subid):
    filenames = glob(datapath+'%s'%subid+'/'+'*_%s_[1-9].mat'%subid); #got to check that this regex works here
    blocks = []; #empty list to hold loaded blocks
    for filename in filenames:
        matdata=loadmat(filename,struct_as_record=False,squeeze_me=True)['block'];
        block=Block(matdata);
        blocks.append(block);
    return blocks #return the loaded blocks as a list for later purposes..

#define functions to get subject specific blocks and aggregate blocks together for analysis, respectively
def getAllSubjectBlocks():
    blocks = [[] for i in range(len(ids))]; #create a list of empty lists to append the individual blocks to
    for i,sub_id in enumerate(ids):
        blocks[i] = loadAllBlocks(sub_id);
        #print "Imported data for subject %s\n"%sub_id;
    #print "Done getting all subject blocks..\n";
    return blocks;

def getTrials(all_blocks):
    # segment the trials all together
	trial_matrix = [[t for b in blocks for t in b.trials] for blocks in all_blocks];
	print "Done getting trials together..\n"
	return trial_matrix; #trial matrix will be a n by m, n is the number of trials for a subject and m is the number of subjects


## Data Structures ###############################################################################################################

#define a Block object that will hold the Trials for each block along with relevant data (e.g. date)
class Block(object):
	#object being passed into this class should be a scipy mat_structure of data from the block
	def __init__(self, matStructure=None):
		self.block_nr= matStructure.block_nr;
		self.date = str(matStructure.date);
		self.sub_id = str(matStructure.sub_id);
		self.block_type = str(matStructure.type);
		self.nr_invalids = matStructure.nr_invalids;
		self.sp = matStructure.sp;
		self.dp = matStructure.dp;
		self.trials = [Trial(trialData) for trialData in  matStructure.trial_data];
        
#define a Trial object that will hold the individual trial data for discrimination tasks
class Trial(object):
	#object being passed into this Trial instance should be a dictionary corresponding to the trial data for this given trial
	def __init__(self, trialData):
		self.sub_id = trialData.sub_id;
		self.block_type = str(trialData.block_type); #b for bottom up, of t for top down
		self.block_nr = trialData.block_nr;
		self.trial_type = trialData.trial_type;
		self.nr_targets = trialData.nr_targets;
		self.target_shapes = trialData.target_shapes; #1,2,3, or 4
		self.target_types = array([str(type) for type in trialData.target_types]); #left or right
		self.targets_same_response = trialData.targets_same_response;
		self.same_hf = trialData.same_hf;
		self.target_coors = trialData.target_coors;
		self.target_distances = trialData.target_distances;
		self.nr_distractors = trialData.nr_distractors;
		self.distractor_shapes = trialData.dist_shapes;
		self.distractor_types = array([str(type) for type in trialData.dist_types]); #left or right
		self.distractor_coors = trialData.dist_coors;
		self.distractor_distances = trialData.distractor_distances;
		self.trial_times = trialData.trial_times
		self.response_time = self.trial_times.response_time*1000; #ms
		self.response = trialData.response;
		self.result = trialData.result;
		self.selected_type = trialData.selected_type;
		self.drift_shift = trialData.drift_shift;
        
        
        
        
        
        
        