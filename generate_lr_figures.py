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

datapath = '/Users/james/Documents/MATLAB/data/response_conflict/'; #'/Users/jameswilmott/Documents/MATLAB/data/response_conflict/'; #
shelvepath = '/Users/james/Documents/Python/response_conflict/data/';  #'/Users/jameswilmott/Documents/Python/response_conflict/data/'; # 
savepath = '/Users/james/Documents/Python/response_conflict/figures/'; #'/Users/jameswilmott/Documents/Python/response_conflict/figures/'; #

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'rc_data');
individ_subject_data = shelve.open(shelvepath+'individ_rc_data');

ids=['jpw'];

id = raw_input('ID for plotting (agg for all subjects): ');

if id=='agg':
    db = subject_data;
else:
    db = individ_subject_data

#set parameters for plots
matplotlib.rcParams['ytick.labelsize']=20; matplotlib.rcParams['xtick.labelsize']=20; #30;
matplotlib.rcParams['xtick.major.width']=2.0; matplotlib.rcParams['ytick.major.width']=2.0;
matplotlib.rcParams['xtick.major.size']=10.0; matplotlib.rcParams['ytick.major.size']=10.0; #increase the length of the ticks
matplotlib.rcParams['hatch.linewidth'] = 9.0; #set the hatch width to larger than the default case
matplotlib.rcParams['hatch.color'] = 'black';
matplotlib.pyplot.rc('font',weight='bold');

##########################################################################################################################################################
#Single Target Distractor Shape Plots
# As a function of DISTRACTOR SHAPE
##########################################################################################################################################################


#single target RT broken down by target shape
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('One Target Trials, For Each Shape, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]);
ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,1)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,2)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,3)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,4)],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,1)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);    
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,2)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,2)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,2)]]],color='black',lw=6.0);     
    ax1.errorbar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,3)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,3)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,3)]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,4)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,4)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,4)]]],color='black',lw=6.0); 
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
ax2.set_ylim(400,950); ax2.set_yticks(arange(450,951,50)); ax2.set_xlim([0.7,3.1]); ax2.set_xticks([1,1.6,2.2,2.8]);
ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax2.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,1)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,2)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,3)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,4)],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,1)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);    
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,2)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,2)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,2)]]],color='black',lw=6.0);     
    ax2.errorbar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,3)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,3)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,3)]]],color='black',lw=6.0);
    ax2.errorbar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,4)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,4)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,4)]]],color='black',lw=6.0); 
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
show();  
 
 
 
#single target PC broken down by target shape
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('One Target Trials, For Each Shape, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(0.75,1.0); ax1.set_yticks(arange(0.8,1.01,0.05)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]);
ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,1)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,2)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,3)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,4)],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,1)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);    
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,2)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,2)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,2)]]],color='black',lw=6.0);     
    ax1.errorbar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,3)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,3)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,3)]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,4)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,4)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,4)]]],color='black',lw=6.0); 
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
ax2.set_ylim(0.75,1.0); ax2.set_yticks(arange(0.75, 1.01, 0.05)); ax2.set_xlim([0.7,3.1]); ax2.set_xticks([1,1.6,2.2,2.8]);
ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax2.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,1)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,2)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,3)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,4)],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,1)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);    
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,2)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,2)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,2)]]],color='black',lw=6.0);     
    ax2.errorbar(2.2,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,3)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,3)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,3)]]],color='black',lw=6.0);
    ax2.errorbar(2.8,db['%s_LR_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,4)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,4)]],
        [db['%s_LR_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,4)]]],color='black',lw=6.0); 
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
show();



#RT as a function of # distractors with the same shapes (1 or 2), collapsed cross the distractor shapes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Number of Distractors With Matching Shapes,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(400,900); ax1.set_yticks(arange(450,901,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
colors = ['gray','gray'];
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,0)],color=colors[0],width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,1)],color=colors[0],width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top-down task plot
ax2.set_ylim(400,900); ax2.set_yticks(arange(450,901,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,0)],color=colors[1],width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,1)],color=colors[1],width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


#PC as a function of # distractors with the same shapes (1 or 2), collapsed cross the distractor shapes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Proportion Correct By Number of Distractors With Matching Shapes,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(0.8,1.0); ax1.set_yticks(arange(0.85,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
colors = ['gray','gray'];
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,0)],color=colors[0], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top-down task plot
ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,0)],color=colors[1], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,1)],color=colors[1], alpha = 0.6, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


#RT as a function of # distractors with the same shapes (1 or 2), pulled out for different target shapes, Bottom up task
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up Response Time By Number of Distractors With Matching Shapes For Each Shape,\n Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray'];
#ax1 is the top left shape 
ax1.set_ylim(400,800); ax1.set_yticks(arange(450,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,0)],color=colors[0], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(400,800); ax2.set_yticks(arange(450,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,0)],color=colors[0], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(400,800); ax3.set_yticks(arange(450,801,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,0)],color=colors[0], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(400,800); ax4.set_yticks(arange(450,801,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,0)],color=colors[0], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,1)]]],color='black',lw=6.0);
ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# labels = [item.get_text() for item in ax3.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax3.set_xticklabels(labels);
# ax3.set_yticklabels(['','','','','','','','','','','','','','']);
# ax3.set_ylabel(''); ax3.set_xlabel('');
# labels = [item.get_text() for item in ax4.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax4.set_xticklabels(labels);
# ax4.set_yticklabels(['','','','','','','','','','','','','','']);
# ax4.set_ylabel(''); ax4.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


#RT as a function of # distractors with the same shapes (1 or 2), pulled out for different target shapes, Top down task
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Top-Down Response Time By Number of Distractors With Matching Shapes \n  For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray'];
#ax1 is the top left shape 
ax1.set_ylim(400,800); ax1.set_yticks(arange(450,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,0)],color=colors[1], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(400,800); ax2.set_yticks(arange(450,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,0)],color=colors[1], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(400,800); ax3.set_yticks(arange(450,801,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,0)],color=colors[1], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(400,800); ax4.set_yticks(arange(450,801,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,0)],color=colors[1], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,1)]]],color='black',lw=6.0);
ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# labels = [item.get_text() for item in ax3.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax3.set_xticklabels(labels);
# ax3.set_yticklabels(['','','','','','','','','','','','','','']);
# ax3.set_ylabel(''); ax3.set_xlabel('');
# labels = [item.get_text() for item in ax4.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax4.set_xticklabels(labels);
# ax4.set_yticklabels(['','','','','','','','','','','','','','']);
# ax4.set_ylabel(''); ax4.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


#PC as a function of # distractors with the same shapes (1 or 2), pulled out for different target shapes, Bottom up task
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up Proportion Correct By Number of Distractors With Matching Shapes\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray'];
#ax1 is the top left shape 
ax1.set_ylim(0.8,1.0); ax1.set_yticks(arange(0.85,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,0)],color=colors[0], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,0)],color=colors[0], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Proportion correct',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,0)],color=colors[0], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(0.8,1.0); ax4.set_yticks(arange(0.85,1.01,0.05)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,0)],color=colors[0], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,1)]]],color='black',lw=6.0);
ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# labels = [item.get_text() for item in ax3.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax3.set_xticklabels(labels);
# ax3.set_yticklabels(['','','','','','','','','','','','','','']);
# ax3.set_ylabel(''); ax3.set_xlabel('');
# labels = [item.get_text() for item in ax4.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax4.set_xticklabels(labels);
# ax4.set_yticklabels(['','','','','','','','','','','','','','']);
# ax4.set_ylabel(''); ax4.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


#PC as a function of # distractors with the same shapes (1 or 2), pulled out for different target shapes, Top down task
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Top-Down Response Time By Number of Distractors With Matching Shapes\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray'];
#ax1 is the top left shape 
ax1.set_ylim(0.8,1.0); ax1.set_yticks(arange(0.85,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,0)],color=colors[1], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,0)],color=colors[1], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(0.7,1.0); ax3.set_yticks(arange(0.75,1.01,0.05)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Proportion correct',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,0)],color=colors[1], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(0.8,1.0); ax4.set_yticks(arange(0.85,1.01,0.05)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,0)],color=colors[1], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,0)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,1)]],[db['%s_LR_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,1)]]],color='black',lw=6.0);
ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# labels = [item.get_text() for item in ax3.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax3.set_xticklabels(labels);
# ax3.set_yticklabels(['','','','','','','','','','','','','','']);
# ax3.set_ylabel(''); ax3.set_xlabel('');
# labels = [item.get_text() for item in ax4.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax4.set_xticklabels(labels);
# ax4.set_yticklabels(['','','','','','','','','','','','','','']);
# ax4.set_ylabel(''); ax4.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


# ##########################################################################################################################################################
# #Single Target Distractor Shape Plots
# # As a function of DISTRACTOR RESPONSE
# ##########################################################################################################################################################
# 
# #RT as a function of # distractors with the same RESPONSE, separated by response and number of matching distractors
# fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Distractor Matching RESPONSE, Response Time,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
# ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
# colors = ['gray','gray'];
# #ax1 is the bottom up left response
# ax1.set_ylim(400,800); ax1.set_yticks(arange(450,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task, LEFT Response', size = 18, position = (.5, 0.9));
# #ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax1.set_xticklabels(['3','4']); 
# ax1.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'left',2)],color=colors[0],width=0.4);
# ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'left',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'left',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'left',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'left',2)]]],color='black',lw=6.0);
#     ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'left',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'left',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'left',3)]]],color='black',lw=6.0);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# #ax2 is bottom up right response
# ax2.set_ylim(400,800); ax2.set_yticks(arange(450,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Bottom Up Task, RIGHT Response', size = 18, position = (.5, 0.9));
# #ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax2.set_xticklabels(['3','4']); 
# colors = ['gray','gray'];
# ax2.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'right',2)],color=colors[0],width=0.4);
# ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'left',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'right',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'right',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'right',2)]]],color='black',lw=6.0);
#     ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'right',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'right',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'right',3)]]],color='black',lw=6.0);
# ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
# ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
# ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# #ax3 is the top down left response
# ax3.set_ylim(400,800); ax3.set_yticks(arange(450,801,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Top Down Task, LEFT Response', size = 18, position = (.5, 0.9));
# ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of distractors with matching RESPONSE to target',size=18); #,labelpad=40
# ax3.set_xticklabels(['3','4']); 
# ax3.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'left',2)],color=colors[1],width=0.4);
# ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'left',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'left',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'left',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'left',2)]]],color='black',lw=6.0);
#     ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'left',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'left',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'left',3)]]],color='black',lw=6.0);
# ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
# ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
# ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
# #ax4 is the top down right response
# ax4.set_ylim(400,800); ax4.set_yticks(arange(450,801,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Top Down Task, LEFT Response', size = 18, position = (.5, 0.9));
# #ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax4.set_xticklabels(['3','4']); 
# ax4.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'right',2)],color=colors[1],width=0.4);
# ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'right',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'right',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'right',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'right',2)]]],color='black',lw=6.0);
#     ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'right',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'right',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'right',3)]]],color='black',lw=6.0);
# ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
# ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
# ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
# #save the labeled figure as a .png	
# # filename = '';
# # savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# # ax2.set_xticklabels(labels);
# # ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax2.set_ylabel(''); ax2.set_xlabel('');
# # filename = '';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# show();
# 
# 
# #PC as a function of # distractors with the same RESPONSE, separated by response and number of matching distractors
# fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Distractor Matching RESPONSE, Proportion Correct,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
# ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
# colors = ['gray','gray'];
# #ax1 is the bottom up left response
# ax1.set_ylim(0.8,1.0); ax1.set_yticks(arange(0.85,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task, LEFT Response', size = 18, position = (.5, 0.9));
# #ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax1.set_xticklabels(['3','4']); 
# ax1.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'left',2)],color=colors[0],width=0.4);
# ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'left',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'left',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'left',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'left',2)]]],color='black',lw=6.0);
#     ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'left',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'left',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'left',3)]]],color='black',lw=6.0);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# #ax2 is bottom up right response
# ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Bottom Up Task, RIGHT Response', size = 18, position = (.5, 0.9));
# #ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax2.set_xticklabels(['3','4']); 
# colors = ['gray','gray'];
# ax2.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'right',2)],color=colors[0],width=0.4);
# ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'left',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'right',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'right',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'right',2)]]],color='black',lw=6.0);
#     ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'right',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'right',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'right',3)]]],color='black',lw=6.0);
# ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
# ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
# ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# #ax3 is the top down left response
# ax3.set_ylim(0.8,1.0); ax3.set_yticks(arange(0.85,1.01,0.05)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Top Down Task, LEFT Response', size = 18, position = (.5, 0.9));
# ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax3.set_xticklabels(['3','4']); 
# ax3.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'left',2)],color=colors[1],width=0.4);
# ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'left',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'left',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'left',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'left',2)]]],color='black',lw=6.0);
#     ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'left',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'left',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'left',3)]]],color='black',lw=6.0);
# ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
# ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
# ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
# #ax4 is the top down right response
# ax4.set_ylim(0.8,1.0); ax4.set_yticks(arange(0.85,1.01,0.05)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Top Down Task, LEFT Response', size = 18, position = (.5, 0.9));
# #ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax4.set_xticklabels(['3','4']); 
# ax4.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'right',2)],color=colors[1],width=0.4);
# ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'right',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'right',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'right',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'right',2)]]],color='black',lw=6.0);
#     ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'right',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'right',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'right',3)]]],color='black',lw=6.0);
# ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
# ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
# ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
# #save the labeled figure as a .png	
# # filename = '';
# # savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# # ax2.set_xticklabels(labels);
# # ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax2.set_ylabel(''); ax2.set_xlabel('');
# # filename = '';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# show();
# 
# 
# #########################################################################################################################################################
# ##Single Target Distractor Shape Plots
# ##DISTRACTOR RESPONSE, cutting out the same shape conditions!
# ######################################################################################################################################################
# 
# #RT as a function of # distractors with the same RESPONSE, separated by response and number of matching distractors
# fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('No 5th Distractor Same Shape, Matching RESPONSE, Response Time,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
# ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
# colors = ['gray','gray'];
# #ax1 is the bottom up left response
# ax1.set_ylim(400,800); ax1.set_yticks(arange(450,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task, LEFT Response', size = 18, position = (.5, 0.9));
# #ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax1.set_xticklabels(['3','4']); 
# ax1.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'left',2)],color=colors[0],width=0.4);
# ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'left',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax1.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'left',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'left',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'left',2)]]],color='black',lw=6.0);
#     ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'left',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'left',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'left',3)]]],color='black',lw=6.0);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# #ax2 is bottom up right response
# ax2.set_ylim(400,800); ax2.set_yticks(arange(450,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Bottom Up Task, RIGHT Response', size = 18, position = (.5, 0.9));
# #ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax2.set_xticklabels(['3','4']); 
# colors = ['gray','gray'];
# ax2.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'right',2)],color=colors[0],width=0.4);
# ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'left',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'right',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'right',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'right',2)]]],color='black',lw=6.0);
#     ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'right',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'right',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'right',3)]]],color='black',lw=6.0);
# ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
# ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
# ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# #ax3 is the top down left response
# ax3.set_ylim(400,800); ax3.set_yticks(arange(450,801,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Top Down Task, LEFT Response', size = 18, position = (.5, 0.9));
# ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax3.set_xticklabels(['3','4']); 
# ax3.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'left',2)],color=colors[1],width=0.4);
# ax3.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'left',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax3.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'left',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'left',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'left',2)]]],color='black',lw=6.0);
#     ax3.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'left',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'left',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'left',3)]]],color='black',lw=6.0);
# ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
# ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
# ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
# #ax4 is the top down right response
# ax4.set_ylim(400,800); ax4.set_yticks(arange(450,801,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Top Down Task, LEFT Response', size = 18, position = (.5, 0.9));
# #ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax4.set_xticklabels(['3','4']); 
# ax4.bar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'right',2)],color=colors[1],width=0.4);
# ax4.bar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'right',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax4.errorbar(1,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'right',2)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'right',2)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'right',2)]]],color='black',lw=6.0);
#     ax4.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'right',3)],yerr=[[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'right',3)]],[db['%s_LR_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'right',3)]]],color='black',lw=6.0);
# ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
# ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
# ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
# #save the labeled figure as a .png	
# # filename = '';
# # savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# # ax2.set_xticklabels(labels);
# # ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax2.set_ylabel(''); ax2.set_xlabel('');
# # filename = '';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# show();



##########################################################################################################################################################
# Number of Targets comparison, 1 vs. 2
##########################################################################################################################################################

#do the bottom up and top down plots on separate subaxes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Number of Targets,\n Left-Right Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(400,900); ax1.set_yticks(arange(450,901,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of targets',size=18); #,labelpad=40
ax1.set_xticklabels(['1','2']); 
ax1.bar(1,db['%s_LR_%s_%s_targets_mean_rt'%(id,'b',1)],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_mean_rt'%(id,'b',2)],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_%s_targets_mean_rt'%(id,'b',1)],yerr=[[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'b',1)]],[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'b',1)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_%s_targets_mean_rt'%(id,'b',2)],yerr=[[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'b',2)]],[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'b',2)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top down version of the task
ax2.set_ylim(400,900); ax2.set_yticks(arange(450,901,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of targets',size=18); #,labelpad=40
ax2.set_xticklabels(['1','2']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_mean_rt'%(id,'t',1)],color='gray', alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_mean_rt'%(id,'t',2)],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_mean_rt'%(id,'t',1)],yerr=[[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'t',1)]],[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'t',1)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_mean_rt'%(id,'t',2)],yerr=[[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'t',2)]],[db['%s_LR_%s_%s_targets_rt_bs_sems'%(id,'t',2)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();

##########################################################################################################################################################
# Congruency Comparisons
##########################################################################################################################################################

#do the bottom up and top down plots on separate subaxes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Congruency Conditions,\n Left-Right Task, Subject %s'%id, size = 22);
ax1.set_ylim(400,900); ax1.set_yticks(arange(450,901,50)); ax1.set_xlim([0.7,2.5]); ax1.set_xticks([1,1.6,2.2]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['CP/CR','IP/CR','IP/IR']); #['Congruent Percept\nCongruent Response','Incongruent Percept\nCongruent Response','Incongruent Percept\nIncongruent Response']
ax1.bar(1,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'b','cong_per_cong_resp')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_cong_resp')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_incong_resp')],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'b','cong_per_cong_resp')],yerr=[[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp')]],[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_cong_resp')],yerr=[[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp')]],[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_incong_resp')],yerr=[[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp')]],[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top down version of the task
ax2.set_ylim(400,900); ax2.set_yticks(arange(450,901,50)); ax2.set_xlim([0.7,2.5]); ax2.set_xticks([1,1.6,2.2]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Condition',size=18);
ax2.set_xticklabels(['CP/CR','IP/CR','IP/IR']);
ax2.bar(1,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'t','cong_per_cong_resp')],color='gray', alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_cong_resp')],color='gray', alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_incong_resp')],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'t','cong_per_cong_resp')],yerr=[[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp')]],[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp')]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_cong_resp')],yerr=[[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp')]],[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp')]]],color='black',lw=6.0);
    ax2.errorbar(2.2,db['%s_LR_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_incong_resp')],yerr=[[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp')]],[db['%s_LR_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp')]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#save the labeled figure as a .png	
# filename = '';
# savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax2.get_xticklabels()]; labels[0]=''; labels[1]=''; #labels[2]=''; #have to do this to center the x ticks on correct spot without incurring ticks at every spot
# ax2.set_xticklabels(labels);
# ax2.set_yticklabels(['','','','','','','','','','','','','','']);
# ax2.set_ylabel(''); ax2.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();



#run the congruency comparison, searating out the different shapes
#first separate out the bottom up congruenct percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up RT for Congruent Percept/Congruent Response Trials\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top_left','bottom_left','top_right','bottom_right']); 
ax1.bar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_left')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_left')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_right')],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_left')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_left')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_left')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_left')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_left')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_right')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#next separate out the incongruent percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up RT for Congruent Percept/Incongruent Response Trials\n For Each Type, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['both_left_responses','both_right_responses']); 
ax1.bar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_left_responses')],color='gray', alpha = 1.0, width=0.2);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_right_responses')],color='gray', alpha = 1.0, width=0.2);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_left_responses')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_left_responses')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_left_responses')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_right_responses')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_right_responses')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_right_responses')]]],color='black',lw=6.0);   
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#finally check out the incongruent percept/incongreutn response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up RT for Inongruent Percept/Inongruent Response Trials\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['top_left\ntop_right','top_left\nbottom_right','bottom_left\ntop_right','bottom_left\nbottom_right']);
ax1.bar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_top_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_bottom_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','bottom_left_top_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','bottom_left_bottom_right')],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_top_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_top_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_bottom_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_bottom_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_bottom_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','bottom_left_top_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','bottom_left_top_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','bottom_left_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','bottom_left_bottom_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','bottom_left_bottom_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','bottom_left_bottom_right')]]],color='black',lw=6.0);    
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();    
    
   
#now the top down congruency data
#run the congruency comparison, searating out the different shapes
#first separate out the bottom up congruenct percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-Down RT for Congruent Percept/Congruent Response Trials\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top_left','bottom_left','top_right','bottom_right']); 
ax1.bar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_left')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_left')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_right')],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_left')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_left')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_left')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_left')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_left')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_right')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#next separate out the incongruent percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-Down RT for Congruent Percept/Incongruent Response Trials\n For Each Type, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['both_left_responses','both_right_responses']); 
ax1.bar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_left_responses')],color='gray', alpha = 1.0, width=0.2);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_right_responses')],color='gray', alpha = 1.0, width=0.2);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_left_responses')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_left_responses')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_left_responses')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_right_responses')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_right_responses')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_right_responses')]]],color='black',lw=6.0);   
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#finally check out the incongruent percept/incongreutn response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-Down RT for Inongruent Percept/Inongruent Response Trials\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
colors = ['gray','gray'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['top_left\ntop_right','top_left\nbottom_right','bottom_left\ntop_right','bottom_left\nbottom_right']);
ax1.bar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_top_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_bottom_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','bottom_left_top_right')],color='gray', alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','bottom_left_bottom_right')],color='gray', alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_top_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_top_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_bottom_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_bottom_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_bottom_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','bottom_left_top_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','bottom_left_top_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','bottom_left_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_LR_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','bottom_left_bottom_right')],yerr=[[db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','bottom_left_bottom_right')]],
        [db['%s_LR_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','bottom_left_bottom_right')]]],color='black',lw=6.0);    
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();   
    
 
    
