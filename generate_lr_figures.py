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

# ##########################################################################################################################################################
# #Single Target Distractor Shape Plots
# ##########################################################################################################################################################


#RT as a function of # distractors with the same shapes (1 or 2), collapsed cross the distractor shapes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Number of Distractors With Matching Shapes,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(500,700); ax1.set_yticks(arange(550,701,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax1.set_xticklabels(['1','2']); 
colors=['blue'];
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,0)],color=colors[0],width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,1)],color=colors[0],width=0.4);
if id=='agg':
    ax1.errorbar(1,['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'b',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'b',1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'b',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'b',1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top-down task plot
ax2.set_ylim(500,700); ax2.set_yticks(arange(550,701,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax2.set_xticklabels(['1','2']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,0)],color=colors[0],width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,1)],color=colors[0],width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'t',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'t',1,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'t',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_rt_bsems'%(id,'t',1,1)]]],color='black',lw=6.0);
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
# ax2.set_ylabel(''); ax1.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();


#PC as a function of # distractors with the same shapes (1 or 2), collapsed cross the distractor shapes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Proportion Correct By Number of Distractors With Matching Shapes,\n Single Target Trials,Left-Right Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(0.8,1.0); ax1.set_yticks(arange(0.85,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax1.set_xticklabels(['1','2']); 
colors=['blue'];
ax1.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,0)],color=colors[0], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'b',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'b',1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'b',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'b',1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top-down task plot
ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of distractors with matching shape to target',size=18); #,labelpad=40
ax2.set_xticklabels(['1','2']); 
ax2.bar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,0)],color=colors[0],alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,1)],color=colors[0],alpha = 0.6, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,0)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'t',1,0)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'t',1,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_LR_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,1)],yerr=[[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'t',1,1)]],[db['%s_LR_%s_%s_targets_%s_5thdmatch_pc_bsems'%(id,'t',1,1)]]],color='black',lw=6.0);
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
# ax2.set_ylabel(''); ax1.set_xlabel('');
# filename = '';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
show();





