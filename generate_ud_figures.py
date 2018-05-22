#MResponse conflict plotting code
# UP/DOWN response mapping code
#Author: James Wilmott, Winter 2018

#Designed to plot data from a persistent database
from pylab import *
from matplotlib import patches
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.lines as mlines
import shelve #for database writing and reading

matplotlib.rcParams.update(matplotlib.rcParamsDefault); #restore the default matplotlib styles

datapath = '/Users/jameswilmott/Documents/MATLAB/data/response_conflict/'; #'/Users/james/Documents/MATLAB/data/response_conflict/'; #
shelvepath =  '/Users/jameswilmott/Documents/Python/response_conflict/data/'; #'/Users/james/Documents/Python/response_conflict/data/';  #
savepath = '/Users/jameswilmott/Documents/Python/response_conflict/figures/'; # '/Users/james/Documents/Python/response_conflict/figures/'; #

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'rc_ud_data');
individ_subject_data = shelve.open(shelvepath+'individ_rc_ud_data');


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
# ## Previous trial type by response repetition, DIFFERENECS BETWEEN BU-TD ##
# ##########################################################################################################################################################
# 
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Previous trial type analysis, [BOTTOM-UP - TOP-DOWN], subject %s'%id, size = 22);
# colors = ['dodgerblue',(75/255.0,0/255.0,130/255.0),(105/255.0,84/255.0,184/255.0),(186/255.0,85/255.0,212/255.0)];
# ax1.set_xlim([0.5,4.5]); ax1.set_xticks([1.0, 2.0, 3.0, 4.0]); ax1.set_ylim(-25,270); ax1.set_yticks(arange(-0,251,50));
# #single target case first
# ax1.set_ylabel('Response time',size=18); #ax1.set_xlabel('Current Trial Type ',size=18);
# ax1.set_xticklabels(['One target','Same/\nSame','Different/\nSame','Different/\nDifferent']);
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [0.7, 0.9, 1.1, 1.3]):
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'congruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'incongruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #next do the same/same trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [1.7, 1.9, 2.1, 2.3]):  
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'congruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'congruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'incongruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'incongruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #differen/same trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [2.7, 2.9, 3.1, 3.3]):  
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'congruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'congruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'incongruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'incongruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #different/different trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [3.7, 3.9, 4.1, 4.3]):  
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'congruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'incongruent')], yerr = [[db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]],
#             [db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='One target'); ssline=mlines.Line2D([],[],color=(75/255.0,0/255.0,130/255.0),lw=6,label='Same/Same');
# dsline=mlines.Line2D([],[],color=(105/255.0,84/255.0,184/255.0),lw=6,label='Different/Same'); ddline=mlines.Line2D([],[],color=(186/255.0,85/255.0,212/255.0),lw=6,label='Different/Different');
# #congline=mlines.Line2D([],[],color='black',lw=6,label='Congruent previous trial response', alpha = 1.0); incongline=mlines.Line2D([],[],color='black',lw=6,label='Incongruent previous trial response', alpha = 0.3);
# ax1.legend(handles=[oneline,ssline,dsline,ddline],loc = 2, ncol=2, fontsize = 18);
# show();
# 
# 1/0
# ##########################################################################################################################################################
# ## Previous trial type by response repetition ##
# ##########################################################################################################################################################
# 
# #Bottomup
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-up previous trial type analysis, UP-DOWN task, subject %s'%id, size = 22);
# colors = ['dodgerblue',(75/255.0,0/255.0,130/255.0),(105/255.0,84/255.0,184/255.0),(186/255.0,85/255.0,212/255.0)];
# ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,4.5]); ax1.set_xticks([1.0, 2.0, 3.0, 4.0]); #0.7, 0.9, 1.1, 1.3, 1.7, 1.9, 2.1, 2.3, 2.7, 2.9, 3.1, 3.3, 3.7, 3.9, 4.1, 4.3
# #single target case first
# ax1.set_ylabel('Response time',size=18); #ax1.set_xlabel('Current Trial Type ',size=18);
# ax1.set_xticklabels(['One target','Same/\nSame','Different/\nSame','Different/\nDifferent']);
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [0.7, 0.9, 1.1, 1.3]):  
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'congruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'incongruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #next do the same/same trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [1.7, 1.9, 2.1, 2.3]):  
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'congruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'congruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'incongruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'incongruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #differen/same trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [2.7, 2.9, 3.1, 3.3]):  
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'congruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'congruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'incongruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'incongruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #different/different trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [3.7, 3.9, 4.1, 4.3]):  
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'congruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'incongruent')], yerr = [[db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]],
#             [db['%s_UD_b_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='One target'); ssline=mlines.Line2D([],[],color=(75/255.0,0/255.0,130/255.0),lw=6,label='Same/Same');
# dsline=mlines.Line2D([],[],color=(105/255.0,84/255.0,184/255.0),lw=6,label='Different/Same'); ddline=mlines.Line2D([],[],color=(186/255.0,85/255.0,212/255.0),lw=6,label='Different/Different');
# #congline=mlines.Line2D([],[],color='black',lw=6,label='Congruent previous trial response', alpha = 1.0); incongline=mlines.Line2D([],[],color='black',lw=6,label='Incongruent previous trial response', alpha = 0.3);
# ax1.legend(handles=[oneline,ssline,dsline,ddline],loc = 2, ncol=2, fontsize = 18);
# show();
# 
# 
# #topdown
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-down previous trial type analysis, UP-DOWN task, subject %s'%id, size = 22);
# colors = ['dodgerblue',(75/255.0,0/255.0,130/255.0),(105/255.0,84/255.0,184/255.0),(186/255.0,85/255.0,212/255.0)];
# ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,4.5]); ax1.set_xticks([1.0, 2.0, 3.0, 4.0]); #0.7, 0.9, 1.1, 1.3, 1.7, 1.9, 2.1, 2.3, 2.7, 2.9, 3.1, 3.3, 3.7, 3.9, 4.1, 4.3
# #single target case first
# ax1.set_ylabel('Response time',size=18); #ax1.set_xlabel('Current Trial Type ',size=18);
# ax1.set_xticklabels(['One target','Same/\nSame','Different/\nSame','Different/\nDifferent']);
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [0.7, 0.9, 1.1, 1.3]):  
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'congruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'single_target',type,'incongruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'congruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'single_target',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #next do the same/same trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [1.7, 1.9, 2.1, 2.3]):  
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'congruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'congruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_per_cong_resp',type,'incongruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'incongruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_per_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #differen/same trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [2.7, 2.9, 3.1, 3.3]):  
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'congruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'congruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_cong_resp',type,'incongruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'incongruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #different/different trials
# for type, c, ex in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors, [3.7, 3.9, 4.1, 4.3]):  
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'congruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_per_incong_resp',type,'incongruent')], yerr = [[db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'congruent')]],
#             [db['%s_UD_t_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_per_incong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='One target'); ssline=mlines.Line2D([],[],color=(75/255.0,0/255.0,130/255.0),lw=6,label='Same/Same');
# dsline=mlines.Line2D([],[],color=(105/255.0,84/255.0,184/255.0),lw=6,label='Different/Same'); ddline=mlines.Line2D([],[],color=(186/255.0,85/255.0,212/255.0),lw=6,label='Different/Different');
# #congline=mlines.Line2D([],[],color='black',lw=6,label='Congruent previous trial response', alpha = 1.0); incongline=mlines.Line2D([],[],color='black',lw=6,label='Incongruent previous trial response', alpha = 0.3);
# ax1.legend(handles=[oneline,ssline,dsline,ddline],loc = 2, ncol=2, fontsize = 18);
# show();



##########################################################################################################################################################
## Plot each two target trial given whether they have the same response or different response and if the previous trial had the same response or different response (e.g., both associated with up, or not)
##########################################################################################################################################################
# 
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle(' Previous trial congruence of compatibility of responses from current trial\n bottom-up two target trials, subject %s'%id, size = 22);
# ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,1.3]); ax1.set_xticks([0.7,1.1]);
# ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Current trial potential responses',size=18);
# ax1.set_xticklabels(['Same response','Different response']);
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_response','same_response')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_response','same_response')]],
#     color = 'black', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_response','same_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_response','same_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_response','same_response')]]],color='black',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_response','same_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_response','same_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_response','same_response')]]],color='black',lw=6.0,capsize = 12); 
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_response','different_response')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_response','different_response')]],
#     color = 'gray', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_response','different_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_response','different_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_response','different_response')]]],color='gray',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_response','different_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_response','different_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_response','different_response')]]],color='gray',lw=6.0,capsize = 12); 
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# congline=mlines.Line2D([],[],color='black',lw=6,label='Previous trial was same response', alpha = 1.0); incongline=mlines.Line2D([],[],color='gray',lw=6,label='Previous trial was different response');
# ax1.legend(handles=[congline, incongline],loc = 2, ncol=1, fontsize = 18);
# show();
# 
# #top down
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle(' Previous trial congruence of compatibility of responses from current trial\n top-down two target trials, subject %s'%id, size = 22);
# ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,1.3]); ax1.set_xticks([0.7,1.1]);
# ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Current trial potential responses',size=18);
# ax1.set_xticklabels(['Same response','Different response']);
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_response','same_response')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_response','same_response')]],
#     color = 'black', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_response','same_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_response','same_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_response','same_response')]]],color='black',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_response','same_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_response','same_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_response','same_response')]]],color='black',lw=6.0,capsize = 12); 
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_response','different_response')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_response','different_response')]],
#     color = 'gray', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_response','different_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_response','different_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_response','different_response')]]],color='gray',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_response','different_response')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_response','different_response')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_response','different_response')]]],color='gray',lw=6.0,capsize = 12); 
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# congline=mlines.Line2D([],[],color='black',lw=6,label='Previous trial was same response', alpha = 1.0); incongline=mlines.Line2D([],[],color='gray',lw=6,label='Previous trial was different response');
# ax1.legend(handles=[congline, incongline],loc = 2, ncol=1, fontsize = 18);
# show();
#
#
# ############# Congruency of perceptual compatibility ############
# 
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle(' Previous trial congruence of percepts from current trial\n bottom-up two target trials, subject %s'%id, size = 22);
# ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,1.3]); ax1.set_xticks([0.7,1.1]);
# ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Current trial percepts (collapsing across all two target displays)',size=18);
# ax1.set_xticklabels(['Same shapes','Different shapes']);
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_percept','same_percept')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_percept','same_percept')]],
#     color = 'black', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_percept','same_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_percept','same_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_percept','same_percept')]]],color='black',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_percept','same_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_percept','same_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_percept','same_percept')]]],color='black',lw=6.0,capsize = 12); 
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_percept','different_percept')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_percept','different_percept')]],
#     color = 'gray', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','same_percept','different_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_percept','different_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','same_percept','different_percept')]]],color='gray',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'b','different_percept','different_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_percept','different_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'b','different_percept','different_percept')]]],color='gray',lw=6.0,capsize = 12); 
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# congline=mlines.Line2D([],[],color='black',lw=6,label='Previous trial was same shapes', alpha = 1.0); incongline=mlines.Line2D([],[],color='gray',lw=6,label='Previous trial was different shapes');
# ax1.legend(handles=[congline, incongline],loc = 2, ncol=1, fontsize = 18);
# show();
# 
# 
# 
# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle(' Previous trial congruence of percepts from current trial\n top-down two target trials, subject %s'%id, size = 22);
# ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,1.3]); ax1.set_xticks([0.7,1.1]);
# ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Current trial percepts (collapsing across all two target displays)',size=18);
# ax1.set_xticklabels(['Same shapes','Different shapes']);
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_percept','same_percept')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_percept','same_percept')]],
#     color = 'black', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_percept','same_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_percept','same_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_percept','same_percept')]]],color='black',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_percept','same_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_percept','same_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_percept','same_percept')]]],color='black',lw=6.0,capsize = 12); 
# ax1.plot([0.7,1.1],[db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_percept','different_percept')],db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_percept','different_percept')]],
#     color = 'gray', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
# if id=='agg':
#     ax1.errorbar(0.7, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','same_percept','different_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_percept','different_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','same_percept','different_percept')]]],color='gray',lw=6.0,capsize = 12);
#     ax1.errorbar(1.1, db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,'t','different_percept','different_percept')], yerr = [[db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_percept','different_percept')]],
#         [db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,'t','different_percept','different_percept')]]],color='gray',lw=6.0,capsize = 12); 
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# congline=mlines.Line2D([],[],color='black',lw=6,label='Previous trial was same shapes', alpha = 1.0); incongline=mlines.Line2D([],[],color='gray',lw=6,label='Previous trial was different shapes');
# ax1.legend(handles=[congline, incongline],loc = 2, ncol=1, fontsize = 18);
# show();



# ##########################################################################################################################################################
# ## Previous trial type by response type, collapsing across each type of response  ##
# ##########################################################################################################################################################

#bottom-up version
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle(' Response repetition, bottom-up two target trials, subject %s'%id, size = 22);
ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,1.3]); ax1.set_xticks([0.7,1.1]);
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Current trial response',size=18);
ax1.set_xticklabels(['Up response','Down response']);
ax1.plot([0.7,1.1],[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','up','up')],db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','down','up')]],
     color = 'black', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
if id=='agg':
    ax1.errorbar(0.7, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','up','up')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','up','up')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','up','up')]]],color='black',lw=6.0,capsize = 12);
    ax1.errorbar(1.1, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','down','up')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','down','up')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','down','up')]]],color='black',lw=6.0,capsize = 12); 
ax1.plot([0.7,1.1],[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','up','down')],db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','down','down')]],
     color = 'gray', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
if id=='agg':
    ax1.errorbar(0.7, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','up','down')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','up','down')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','up','down')]]],color='gray',lw=6.0,capsize = 12);
    ax1.errorbar(1.1, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'b','down','down')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','down','down')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'b','down','down')]]],color='gray',lw=6.0,capsize = 12); 
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
congline=mlines.Line2D([],[],color='black',lw=6,label='Up response', alpha = 1.0); incongline=mlines.Line2D([],[],color='gray',lw=6,label='Down response');
ax1.legend(handles=[congline, incongline],loc = 2, ncol=1, fontsize = 18);
show();


## top down version
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle(' Response repetition, top-down two target trials, subject %s'%id, size = 22);
ax1.set_ylim(550,875); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,1.3]); ax1.set_xticks([0.7,1.1]);
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Current trial response',size=18);
ax1.set_xticklabels(['Up response','Down response']);
ax1.plot([0.7,1.1],[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','up','up')],db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','down','up')]],
     color = 'black', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
if id=='agg':
    ax1.errorbar(0.7, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','up','up')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','up','up')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','up','up')]]],color='black',lw=6.0,capsize = 12);
    ax1.errorbar(1.1, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','down','up')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','down','up')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','down','up')]]],color='black',lw=6.0,capsize = 12); 
ax1.plot([0.7,1.1],[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','up','down')],db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','down','down')]],
     color = 'gray', ls = 'solid', lw = 5.0, markersize = 12.0, marker = 'o');
if id=='agg':
    ax1.errorbar(0.7, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','up','down')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','up','down')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','up','down')]]],color='gray',lw=6.0,capsize = 12);
    ax1.errorbar(1.1, db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,'t','down','down')], yerr = [[db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','down','down')]],
        [db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,'t','down','down')]]],color='gray',lw=6.0,capsize = 12); 
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
congline=mlines.Line2D([],[],color='black',lw=6,label='Up response', alpha = 1.0); incongline=mlines.Line2D([],[],color='gray',lw=6,label='Down response');
ax1.legend(handles=[congline, incongline],loc = 2, ncol=1, fontsize = 18);
show();


1/0;




##########################################################################################################################################################

#plot the Nback
#bottom up first
fig , (ax) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Bottom-up previous trial type analysis, UP-DOWN task, subject %s'%id, size = 22);
ax1 = ax[0][0]; ax2 = ax[0][1]; ax3 = ax[1][0]; ax4 = ax[1][1];
colors = ['dodgerblue',(75/255.0,0/255.0,130/255.0),(105/255.0,84/255.0,184/255.0),(186/255.0,85/255.0,212/255.0)];
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6, 2.2, 2.8]);
ax1.set_title('Current trial: ST', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Trial Type ',size=18);
ax1.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax1.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','single_target',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax1.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','single_target',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','single_target',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','single_target',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');

ax2.set_ylim(600,900); ax2.set_yticks(arange(650,901,50)); ax2.set_xlim([0.7,3.1]); ax2.set_xticks([1,1.6, 2.2, 2.8]);
ax2.set_title('Current trial: CP/CR', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Trial Type ',size=18);
ax2.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax2.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','cong_per_cong_resp',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax2.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','cong_per_cong_resp',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');

ax3.set_ylim(600,900); ax3.set_yticks(arange(650,901,50)); ax3.set_xlim([0.7,3.1]); ax3.set_xticks([1,1.6, 2.2, 2.8]);
ax3.set_title('Current trial: IP/CR', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Trial Type ',size=18);
ax3.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax3.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','incong_per_cong_resp',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax3.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','incong_per_cong_resp',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');

ax4.set_ylim(600,900); ax4.set_yticks(arange(650,901,50)); ax4.set_xlim([0.7,3.1]); ax4.set_xticks([1,1.6, 2.2, 2.8]);
ax4.set_title('Current trial: IP/IR', size = 18, position = (.5, 0.9));
ax4.set_ylabel('Response time',size=18); ax3.set_xlabel('Trial Type ',size=18);
ax4.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax4.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','incong_per_incong_resp',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax4.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'b','incong_per_incong_resp',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
show();


#top down version second
fig , (ax) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Top-down previous trial type analysis, UP-DOWN task, subject %s'%id, size = 22);
ax1 = ax[0][0]; ax2 = ax[0][1]; ax3 = ax[1][0]; ax4 = ax[1][1];
colors = ['dodgerblue',(75/255.0,0/255.0,130/255.0),(105/255.0,84/255.0,184/255.0),(186/255.0,85/255.0,212/255.0)];
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6, 2.2, 2.8]);
ax1.set_title('Current trial: ST', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Trial Type ',size=18);
ax1.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax1.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','single_target',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax1.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','single_target',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','single_target',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','single_target',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');

ax2.set_ylim(600,900); ax2.set_yticks(arange(650,901,50)); ax2.set_xlim([0.7,3.1]); ax2.set_xticks([1,1.6, 2.2, 2.8]);
ax2.set_title('Current trial: CP/CR', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Trial Type ',size=18);
ax2.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax2.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','cong_per_cong_resp',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax2.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','cong_per_cong_resp',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');

ax3.set_ylim(600,900); ax3.set_yticks(arange(650,901,50)); ax3.set_xlim([0.7,3.1]); ax3.set_xticks([1,1.6, 2.2, 2.8]);
ax3.set_title('Current trial: IP/CR', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Trial Type ',size=18);
ax3.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax3.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','incong_per_cong_resp',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax3.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','incong_per_cong_resp',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');


ax4.set_ylim(600,900); ax4.set_yticks(arange(650,901,50)); ax4.set_xlim([0.7,3.1]); ax4.set_xticks([1,1.6, 2.2, 2.8]);
ax4.set_title('Current trial: IP/IR', size = 18, position = (.5, 0.9));
ax4.set_ylabel('Response time',size=18); ax3.set_xlabel('Trial Type ',size=18);
ax4.set_xticklabels(['ST','CP/CR','IP/CR','IP/IR']);
x=1;
for type, c in zip(['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'], colors):    
    ax4.plot([x], [db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','incong_per_incong_resp',type)]], color = c, markersize = 12.0, marker = 'o');
    if id=='agg':
     ax4.errorbar(x,db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,'t','incong_per_incong_resp',type)],yerr=[[db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp',type)]],
         [db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp',type)]]],color=c,lw=6.0,capsize = 12);    
    x+=0.6;
ax4.spines['right'].set_visible(False); ax4.spines['top'].set_visible(False);
ax4.spines['bottom'].set_linewidth(2.0); ax4.spines['left'].set_linewidth(2.0);
ax4.yaxis.set_ticks_position('left'); ax4.xaxis.set_ticks_position('bottom');
show();



##########################################################################################################################################################
#Single Target Distractor Shape Plots
# As a function of DISTRACTOR SHAPE
##########################################################################################################################################################

#single target RT broken down by target shape
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('One Target Trials, For Each Shape, UP-DOWN Task, Subject %s'%id, size = 22);
colors=['dodgerblue','mediumpurple'];
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]);
ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,1)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,2)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,3)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,4)],color=colors[0], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,1)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);    
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,2)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,2)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,2)]]],color='black',lw=6.0);     
    ax1.errorbar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,3)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,3)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,3)]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'b',1,4)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,4)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'b',1,4)]]],color='black',lw=6.0); 
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
ax2.set_ylim(400,950); ax2.set_yticks(arange(450,951,50)); ax2.set_xlim([0.7,3.1]); ax2.set_xticks([1,1.6,2.2,2.8]);
ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax2.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,1)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,2)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,3)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,4)],color=colors[0], alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,1)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);    
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,2)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,2)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,2)]]],color='black',lw=6.0);     
    ax2.errorbar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,3)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,3)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,3)]]],color='black',lw=6.0);
    ax2.errorbar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,'t',1,4)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,4)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,'t',1,4)]]],color='black',lw=6.0); 
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
show();  
 
 
 
#single target PC broken down by target shape
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('One Target Trials, For Each Shape, UP-DOWN Task, Subject %s'%id, size = 22);
colors=['dodgerblue','mediumpurple'];
ax1.set_ylim(0.75,1.0); ax1.set_yticks(arange(0.8,1.01,0.05)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]);
ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,1)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,2)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,3)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,4)],color=colors[0], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,1)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);    
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,2)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,2)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,2)]]],color='black',lw=6.0);     
    ax1.errorbar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,3)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,3)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,3)]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'b',1,4)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,4)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'b',1,4)]]],color='black',lw=6.0); 
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
ax2.set_ylim(0.75,1.0); ax2.set_yticks(arange(0.75, 1.01, 0.05)); ax2.set_xlim([0.7,3.1]); ax2.set_xticks([1,1.6,2.2,2.8]);
ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax2.set_xticklabels(['top\nleft','top\nright','bottom\nleft','bottom\nright']);
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,1)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,2)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,3)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,4)],color=colors[0], alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,1)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);    
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,2)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,2)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,2)]]],color='black',lw=6.0);     
    ax2.errorbar(2.2,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,3)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,3)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,3)]]],color='black',lw=6.0);
    ax2.errorbar(2.8,db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,'t',1,4)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,4)]],
        [db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,'t',1,4)]]],color='black',lw=6.0); 
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
show();



#RT as a function of # distractors with the same shapes (1 or 2), collapsed cross the distractor shapes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Number of Distractors With Matching Shapes,\n Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(500,800); ax1.set_yticks(arange(550,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
colors=['dodgerblue','mediumpurple']; #colors=['blue','red']; colors = ['gray','gray'];
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,0)],color=colors[0],width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,1)],color=colors[0],width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,0)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'b',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top-down task plot
ax2.set_ylim(500,800); ax2.set_yticks(arange(550,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,0)],color=colors[0],width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,1)],color=colors[0],width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,0)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,'t',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='blue',lw=6,label='Bottom Up'); twoline=mlines.Line2D([],[],color='red',lw=6,label='Top Down');
# ax1.legend(handles=[oneline,twoline],loc = 10,ncol=2,fontsize = 22);
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
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Proportion Correct By Number of Distractors With Matching Shapes,\n Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(0.7,1.0); ax1.set_yticks(arange(0.75,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
colors = ['gray','gray']; #colors=['blue','red'];
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,0)],color=colors[0],  width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,1)],color=colors[0], width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,0)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'b',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top-down task plot
ax2.set_ylim(0.7,1.0); ax2.set_yticks(arange(0.75,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,0)],color=colors[1], width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,1)],color=colors[1], width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,0)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,'t',1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1)]],[db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1)]]],color='black',lw=6.0);
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
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up Response Time By Number of Distractors With Matching Shapes For Each Shape,\n Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray']; #colors=['blue','red'];
#ax1 is the top left shape 
ax1.set_ylim(500,800); ax1.set_yticks(arange(550,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,0)],color=colors[0], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(500,800); ax2.set_yticks(arange(550,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,0)],color=colors[0], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,2,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(500,800); ax3.set_yticks(arange(550,801,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,0)],color=colors[0], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,3,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(500,800); ax4.set_yticks(arange(550,801,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,0)],color=colors[0], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'b',1,4,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'b',1,4,1)]]],color='black',lw=6.0);
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
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Top-Down Response Time By Number of Distractors With Matching Shapes \n  For Each Shape, Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray']; #colors=['blue','red'];
#ax1 is the top left shape 
ax1.set_ylim(500,800); ax1.set_yticks(arange(550,801,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,0)],color=colors[1],  width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,1)],color=colors[1], width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(500,800); ax2.set_yticks(arange(550,801,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,0)],color=colors[1],  width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,1)],color=colors[1], width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,2,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(500,800); ax3.set_yticks(arange(550,801,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,0)],color=colors[1],width=0.4);
ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,1)],color=colors[1], width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,3,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(500,800); ax4.set_yticks(arange(550,801,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,0)],color=colors[1],  width=0.4);
ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,1)],color=colors[1], width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,'t',1,4,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,'t',1,4,1)]]],color='black',lw=6.0);
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
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up Proportion Correct By Number of Distractors With Matching Shapes\n For Each Shape, Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray']; #colors=['blue','red'];
#ax1 is the top left shape 
ax1.set_ylim(0.75,1.0); ax1.set_yticks(arange(0.75,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Proportion correct',size=18); #ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,0)],color=colors[0], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(0.75,1.0); ax2.set_yticks(arange(0.75,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,0)],color=colors[0], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,2,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(0.75,1.0); ax3.set_yticks(arange(0.75,1.01,0.05)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
#ax3.set_ylabel('Proportion correct',size=18);
ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,0)],color=colors[0], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,3,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(0.75,1.0); ax4.set_yticks(arange(0.75,1.01,0.05)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,0)],color=colors[0], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,1)],color=colors[0], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'b',1,4,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'b',1,4,1)]]],color='black',lw=6.0);
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
fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Top-Down Response Time By Number of Distractors With Matching Shapes\n For Each Shape, Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
colors = ['gray','gray']; #colors=['blue','red'];
#ax1 is the top left shape 
ax1.set_ylim(0.75,1.0); ax1.set_yticks(arange(0.75,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Target Shape TOP-LEFT', size = 18, position = (.5, 0.9));
#ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax1.set_xticklabels(['2','3']); 
ax1.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,0)],color=colors[1], alpha = 0.6, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,0)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,1,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,1,1)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top right shape 
ax2.set_ylim(0.75,1.0); ax2.set_yticks(arange(0.75,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Target Shape TOP-RIGHT', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax2.set_xticklabels(['2','3']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,0)],color=colors[1], alpha = 0.6, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,0)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,2,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,2,1)]]],color='black',lw=6.0);
ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
#ax3 is the bottom left shape 
ax3.set_ylim(0.75,1.0); ax3.set_yticks(arange(0.75,1.01,0.05)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Target Shape BOTTOM-LEFT', size = 18, position = (.5, 0.9));
ax3.set_ylabel('Proportion Correct',size=18); ax3.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax3.set_xticklabels(['2','3']); 
ax3.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,0)],color=colors[1], alpha = 0.6, width=0.4);
ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,0)]]],color='black',lw=6.0);
    ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,3,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,3,1)]]],color='black',lw=6.0);
ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
#ax4 is the bottom right shape 
ax4.set_ylim(0.75,1.0); ax4.set_yticks(arange(0.75,1.01,0.05)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Target Shape BOTTOM-RIGHT', size = 18, position = (.5, 0.9));
#ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching shape (including target)',size=18); #,labelpad=40
ax4.set_xticklabels(['2','3']); 
ax4.bar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,0)],color=colors[1], alpha = 0.6, width=0.4);
ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,1)],color=colors[1], alpha = 0.6 ,width=0.4);
if id=='agg':
    ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,0)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,0)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,0)]]],color='black',lw=6.0);
    ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,'t',1,4,1)],yerr=[[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,1)]],[db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,'t',1,4,1)]]],color='black',lw=6.0);
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

# 
# ##########################################################################################################################################################
# #Single Target Distractor Shape Plots
# # As a function of DISTRACTOR RESPONSE
# ##########################################################################################################################################################
# 
# #RT as a function of # distractors with the same RESPONSE, separated by response and number of matching distractors
# fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Distractor Matching RESPONSE, Response Time,\n Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
# ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
# colors = ['gray','gray']; #colors=['blue','red'];
# #ax1 is the bottom up left response
# ax1.set_ylim(500,900); ax1.set_yticks(arange(550,901,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task, UP Response', size = 18, position = (.5, 0.9));
# #ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax1.set_xticklabels(['3','4']); 
# ax1.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'up',2)],color=colors[0],width=0.4);
# ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'up',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'up',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'up',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'up',2)]]],color='black',lw=6.0);
#     ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'up',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'up',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'up',3)]]],color='black',lw=6.0);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# #ax2 is bottom up right response
# ax2.set_ylim(500,900); ax2.set_yticks(arange(550,901,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Bottom Up Task, DOWN Response', size = 18, position = (.5, 0.9));
# #ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax2.set_xticklabels(['3','4']); 
# ax2.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'down',2)],color=colors[0],width=0.4);
# ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'down',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'down',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'down',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'down',2)]]],color='black',lw=6.0);
#     ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'b',1,'down',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'down',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'b',1,'down',3)]]],color='black',lw=6.0);
# ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
# ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
# ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# #ax3 is the top down left response
# ax3.set_ylim(500,900); ax3.set_yticks(arange(550,901,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Top Down Task,UP Response', size = 18, position = (.5, 0.9));
# ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax3.set_xticklabels(['3','4']); 
# ax3.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'up',2)],color=colors[1],width=0.4);
# ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'up',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'up',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'up',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'up',2)]]],color='black',lw=6.0);
#     ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'up',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'up',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'up',3)]]],color='black',lw=6.0);
# ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
# ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
# ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
# #ax4 is the top down right response
# ax4.set_ylim(500,900); ax4.set_yticks(arange(550,901,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Top Down Task, DOWN Response', size = 18, position = (.5, 0.9));
# #ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax4.set_xticklabels(['3','4']); 
# ax4.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'down',2)],color=colors[1],width=0.4);
# ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'down',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'down',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'down',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'down',2)]]],color='black',lw=6.0);
#     ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,'t',1,'down',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'down',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,'t',1,'down',3)]]],color='black',lw=6.0);
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
# fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('Distractor Matching RESPONSE, Proportion Correct,\n Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
# ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
# colors = ['gray','gray']; #colors=['blue','red'];
# #ax1 is the bottom up left response
# ax1.set_ylim(0.8,1.0); ax1.set_yticks(arange(0.85,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task, UP Response', size = 18, position = (.5, 0.9));
# #ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax1.set_xticklabels(['3','4']); 
# ax1.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'up',2)],color=colors[0],width=0.4);
# ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'up',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'up',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'up',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'up',2)]]],color='black',lw=6.0);
#     ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'up',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'up',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'up',3)]]],color='black',lw=6.0);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# #ax2 is bottom up right response
# ax2.set_ylim(0.8,1.0); ax2.set_yticks(arange(0.85,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Bottom Up Task, DOWN Response', size = 18, position = (.5, 0.9));
# #ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax2.set_xticklabels(['3','4']); 
# ax2.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'down',2)],color=colors[0],width=0.4);
# ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'down',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'down',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'down',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'down',2)]]],color='black',lw=6.0);
#     ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'b',1,'down',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'down',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'b',1,'down',3)]]],color='black',lw=6.0);
# ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
# ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
# ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# #ax3 is the top down left response
# ax3.set_ylim(0.8,1.0); ax3.set_yticks(arange(0.85,1.01,0.05)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Top Down Task, UP Response', size = 18, position = (.5, 0.9));
# ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax3.set_xticklabels(['3','4']); 
# ax3.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'up',2)],color=colors[1],width=0.4);
# ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'up',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'up',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'up',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'up',2)]]],color='black',lw=6.0);
#     ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'up',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'up',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'up',3)]]],color='black',lw=6.0);
# ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
# ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
# ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
# #ax4 is the top down right response
# ax4.set_ylim(0.8,1.0); ax4.set_yticks(arange(0.85,1.01,0.05)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Top Down Task, DOWN Response', size = 18, position = (.5, 0.9));
# #ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax4.set_xticklabels(['3','4']); 
# ax4.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'down',2)],color=colors[1],width=0.4);
# ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'down',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'down',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'down',2)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'down',2)]]],color='black',lw=6.0);
#     ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,'t',1,'down',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'down',3)]],[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,'t',1,'down',3)]]],color='black',lw=6.0);
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
# ##########################################################################################################################################################
# #Single Target Distractor Shape Plots
# # DISTRACTOR RESPONSE, cutting out the same shape conditions!
# #######################################################################################################################################################
# 
# #RT as a function of # distractors with the same RESPONSE, separated by response and number of matching distractors
# fig , (axuno, axduo) = subplots(2,2,figsize = (12.8,7.64)); fig.suptitle('No 5th Distractor Same Shape, Matching RESPONSE, Response Time,\n Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
# ax1 = axuno[0]; ax2 = axuno[1]; ax3 = axduo[0]; ax4 = axduo[1];
# colors = ['gray','gray']; #colors=['blue','red'];
# #ax1 is the bottom up left response
# ax1.set_ylim(500,900); ax1.set_yticks(arange(550,901,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task, UP Response', size = 18, position = (.5, 0.9));
# #ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax1.set_xticklabels(['3','4']); 
# ax1.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'up',2)],color=colors[0],width=0.4);
# ax1.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'up',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax1.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'up',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'up',2)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'up',2)]]],color='black',lw=6.0);
#     ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'up',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'up',3)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'up',3)]]],color='black',lw=6.0);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# #ax2 is bottom up right response
# ax2.set_ylim(500,900); ax2.set_yticks(arange(550,901,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Bottom Up Task, DOWN Response', size = 18, position = (.5, 0.9));
# #ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax2.set_xticklabels(['3','4']); 
# ax2.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'down',2)],color=colors[0],width=0.4);
# ax2.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'down',3)],color=colors[0],width=0.4);
# if id=='agg':
#     ax2.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'down',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'down',2)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'down',2)]]],color='black',lw=6.0);
#     ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'b',1,'down',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'down',3)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'b',1,'down',3)]]],color='black',lw=6.0);
# ax2.spines['right'].set_visible(False); ax2.spines['top'].set_visible(False);
# ax2.spines['bottom'].set_linewidth(2.0); ax2.spines['left'].set_linewidth(2.0);
# ax2.yaxis.set_ticks_position('left'); ax2.xaxis.set_ticks_position('bottom');
# #ax3 is the top down left response
# ax3.set_ylim(500,900); ax3.set_yticks(arange(550,901,50)); ax3.set_xlim([0.7,1.9]); ax3.set_xticks([1,1.6]); ax3.set_title('Top Down Task, UP Response', size = 18, position = (.5, 0.9));
# ax3.set_ylabel('Response time',size=18); ax3.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax3.set_xticklabels(['3','4']); 
# ax3.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'up',2)],color=colors[1],width=0.4);
# ax3.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'up',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax3.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'up',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'up',2)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'up',2)]]],color='black',lw=6.0);
#     ax3.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'up',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'up',3)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'up',3)]]],color='black',lw=6.0);
# ax3.spines['right'].set_visible(False); ax3.spines['top'].set_visible(False);
# ax3.spines['bottom'].set_linewidth(2.0); ax3.spines['left'].set_linewidth(2.0);
# ax3.yaxis.set_ticks_position('left'); ax3.xaxis.set_ticks_position('bottom');
# #ax4 is the top down right response
# ax4.set_ylim(500,900); ax4.set_yticks(arange(550,901,50)); ax4.set_xlim([0.7,1.9]); ax4.set_xticks([1,1.6]); ax4.set_title('Top Down Task, DOWN Response', size = 18, position = (.5, 0.9));
# #ax4.set_ylabel('Response time',size=18); ax4.set_xlabel('Number of matching RESPONSE (including target)',size=18); #,labelpad=40
# ax4.set_xticklabels(['3','4']); 
# ax4.bar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'down',2)],color=colors[1],width=0.4);
# ax4.bar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'down',3)],color=colors[1],width=0.4);
# if id=='agg':
#     ax4.errorbar(1,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'down',2)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'down',2)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'down',2)]]],color='black',lw=6.0);
#     ax4.errorbar(1.6,db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,'t',1,'down',3)],yerr=[[db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'down',3)]],
#         [db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,'t',1,'down',3)]]],color='black',lw=6.0);
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


#########################################################################################################################################################
## ##Number of Targets comparison, 1 vs. 2
#########################################################################################################################################################

colors=['dodgerblue','mediumpurple'];

#do the bottom up and top down plots on separate subaxes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Number of Targets,\n Up-Down Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(500,1050); ax1.set_yticks(arange(550,1051,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Number of targets',size=18); #,labelpad=40
ax1.set_xticklabels(['1','2']); 
ax1.bar(1,db['%s_UD_%s_%s_targets_mean_rt'%(id,'b',1)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_mean_rt'%(id,'b',2)],color=colors[1], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_mean_rt'%(id,'b',1)],yerr=[[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'b',1)]],[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'b',1)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_mean_rt'%(id,'b',2)],yerr=[[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'b',2)]],[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'b',2)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top down version of the task
ax2.set_ylim(500,1050); ax2.set_yticks(arange(550,1051,50)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Number of targets',size=18); #,labelpad=40
ax2.set_xticklabels(['1','2']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_mean_rt'%(id,'t',1)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_mean_rt'%(id,'t',2)],color=colors[1], alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_mean_rt'%(id,'t',1)],yerr=[[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'t',1)]],[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'t',1)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_mean_rt'%(id,'t',2)],yerr=[[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'t',2)]],[db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,'t',2)]]],color='black',lw=6.0);
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




#do the bottom up and top down plots on separate subaxes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Accuracy By Number of Targets,\n Up-Down Task, Subject %s'%id, size = 22);
#ax1 is the bottom up task plot
ax1.set_ylim(0.75, 1.0); ax1.set_yticks(arange(0.75,1.01,0.05)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of targets',size=18); #,labelpad=40
ax1.set_xticklabels(['1','2']); 
ax1.bar(1,db['%s_UD_%s_%s_targets_pc'%(id,'b',1)],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_%s_targets_pc'%(id,'b',2)],color=colors[1], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_%s_targets_pc'%(id,'b',1)],yerr=[[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'b',1)]],[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'b',1)]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_%s_targets_pc'%(id,'b',2)],yerr=[[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'b',2)]],[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'b',2)]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top down version of the task
ax2.set_ylim(0.75, 1.0); ax2.set_yticks(arange(0.75,1.01,0.05)); ax2.set_xlim([0.7,1.9]); ax2.set_xticks([1,1.6]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
ax2.set_ylabel('Proportion Correct',size=18); ax2.set_xlabel('Number of targets',size=18); #,labelpad=40
ax2.set_xticklabels(['1','2']); 
ax2.bar(1,db['%s_UD_%s_%s_targets_pc'%(id,'t',1)],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_%s_targets_pc'%(id,'t',2)],color=colors[1], alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_%s_targets_pc'%(id,'t',1)],yerr=[[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'t',1)]],[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'t',1)]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_%s_targets_pc'%(id,'t',2)],yerr=[[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'t',2)]],[db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,'t',2)]]],color='black',lw=6.0);
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


#########################################################################################################################################################
## Congruency Comparisons
#########################################################################################################################################################

colors = [(75/255.0,0/255.0,130/255.0),(105/255.0,84/255.0,184/255.0),(186/255.0,85/255.0,212/255.0)];


#do the bottom up and top down plots on separate subaxes
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Response Time By Congruency Conditions,\n Up-Down Task, Subject %s'%id, size = 22);
ax1.set_ylim(500,1050); ax1.set_yticks(arange(550,1051,50)); ax1.set_xlim([0.7,2.5]); ax1.set_xticks([1,1.6,2.2]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['CP/CR','IP/CR','IP/IR']); #['Congruent Percept\nCongruent Response','Incongruent Percept\nCongruent Response','Incongruent Percept\nIncongruent Response']
ax1.bar(1,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'b','cong_per_cong_resp')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_cong_resp')],color=colors[1], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_incong_resp')],color=colors[2], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'b','cong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'b','incong_per_incong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp')]],[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top down version of the task
ax2.set_ylim(500,1050); ax2.set_yticks(arange(550,1051,50)); ax2.set_xlim([0.7,2.5]); ax2.set_xticks([1,1.6,2.2]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Condition',size=18);
ax2.set_xticklabels(['CP/CR','IP/CR','IP/IR']);
ax2.bar(1,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'t','cong_per_cong_resp')],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_cong_resp')],color=colors[1], alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_incong_resp')],color=colors[2], alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'t','cong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp')]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp')]]],color='black',lw=6.0);
    ax2.errorbar(2.2,db['%s_UD_%s_2_targets_%s_mean_rt'%(id,'t','incong_per_incong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp')]],[db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp')]]],color='black',lw=6.0);
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


#Accuracy for this comparison
fig , (ax1, ax2) = subplots(1,2,figsize = (12.8,7.64)); fig.suptitle('Accuracy By Congruency Conditions,\n Up-Down Task, Subject %s'%id, size = 22);
ax1.set_ylim(0.75, 1.0); ax1.set_yticks(arange(0.8, 1.01, 0.05)); ax1.set_xlim([0.7,2.5]); ax1.set_xticks([1,1.6,2.2]); ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['CP/CR','IP/CR','IP/IR']); #['Congruent Percept\nCongruent Response','Incongruent Percept\nCongruent Response','Incongruent Percept\nIncongruent Response']
ax1.bar(1,db['%s_UD_%s_2_targets_%s_pc'%(id,'b','cong_per_cong_resp')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_pc'%(id,'b','incong_per_cong_resp')],color=colors[1], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_2_targets_%s_pc'%(id,'b','incong_per_incong_resp')],color=colors[2], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_pc'%(id,'b','cong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'b','cong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'b','cong_per_cong_resp')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_pc'%(id,'b','incong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'b','incong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'b','incong_per_cong_resp')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_UD_%s_2_targets_%s_pc'%(id,'b','incong_per_incong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'b','incong_per_incong_resp')]],[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'b','incong_per_incong_resp')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
#ax2 is the top down version of the task
ax2.set_ylim(0.75, 1.0); ax2.set_yticks(arange(0.8, 1.01, 0.05)); ax2.set_xlim([0.7,2.5]); ax2.set_xticks([1,1.6,2.2]); ax2.set_title('Top Down Task', size = 18, position = (.5, 0.9));
#ax2.set_ylabel('Response time',size=18); ax2.set_xlabel('Condition',size=18);
ax2.set_xticklabels(['CP/CR','IP/CR','IP/IR']);
ax2.bar(1,db['%s_UD_%s_2_targets_%s_pc'%(id,'t','cong_per_cong_resp')],color=colors[0], alpha = 1.0, width=0.4);
ax2.bar(1.6,db['%s_UD_%s_2_targets_%s_pc'%(id,'t','incong_per_cong_resp')],color=colors[1], alpha = 1.0, width=0.4);
ax2.bar(2.2,db['%s_UD_%s_2_targets_%s_pc'%(id,'t','incong_per_incong_resp')],color=colors[2], alpha = 1.0, width=0.4);
if id=='agg':
    ax2.errorbar(1,db['%s_UD_%s_2_targets_%s_pc'%(id,'t','cong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'t','cong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'t','cong_per_cong_resp')]]],color='black',lw=6.0);
    ax2.errorbar(1.6,db['%s_UD_%s_2_targets_%s_pc'%(id,'t','incong_per_cong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'t','incong_per_cong_resp')]],[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'t','incong_per_cong_resp')]]],color='black',lw=6.0);
    ax2.errorbar(2.2,db['%s_UD_%s_2_targets_%s_pc'%(id,'t','incong_per_incong_resp')],yerr=[[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'t','incong_per_incong_resp')]],[db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,'t','incong_per_incong_resp')]]],color='black',lw=6.0);
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
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up RT for Congruent Percept/Congruent Response Trials\n For Each Shape, Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1.set_ylim(500,1050); ax1.set_yticks(arange(550,1051,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top_left','bottom_left','top_right','bottom_right']); 
ax1.bar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_left')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_left')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_right')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_right')],color=colors[0], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_left')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_top_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','cong_per_cong_resp','both_bottom_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','cong_per_cong_resp','both_bottom_right')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#next separate out the incongruent percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up RT for Congruent Percept/Incongruent Response Trials\n For Each Type, Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1.set_ylim(500,1050); ax1.set_yticks(arange(550,1051,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['both_up_responses','both_down_responses']); 
ax1.bar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_top_responses')],color=colors[1], alpha = 1.0, width=0.2);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_bottom_responses')],color=colors[1], alpha = 1.0, width=0.2);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_top_responses')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_top_responses')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_top_responses')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_cong_resp','both_bottom_responses')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_bottom_responses')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_cong_resp','both_bottom_responses')]]],color='black',lw=6.0);   
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#finally check out the incongruent percept/incongreutn response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Bottom-Up RT for Incongruent Percept/Incongruent Response Trials\n For Each Shape, Single Target Trials, UP-DOWN Task, Subject %s'%id, size = 22);
ax1.set_ylim(500,1050); ax1.set_yticks(arange(550,1051,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['top_left\nbottom_left','top_left\nbottom_right','top_right\nbottom_left','top_right\nbottom_right']);
ax1.bar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_bottom_left')],color=colors[2], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_bottom_right')],color=colors[2], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_right_bottom_left')],color=colors[2], alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_right_bottom_right')],color=colors[2], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_bottom_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_bottom_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_left_bottom_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_bottom_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_left_bottom_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_right_bottom_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_right_bottom_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_right_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'b','incong_per_incong_resp','top_right_bottom_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_right_bottom_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'b','incong_per_incong_resp','top_right_bottom_right')]]],color='black',lw=6.0);    
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();    
    
  
#now the top down congruency data
#run the congruency comparison, searating out the different shapes
#first separate out the bottom up congruenct percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-Down RT for Congruent Percept/Congruent Response Trials\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Target Shape',size=18);
ax1.set_xticklabels(['top_left','bottom_left','top_right','bottom_right']); 
ax1.bar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_left')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_left')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_right')],color=colors[0], alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_right')],color=colors[0], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_left')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_top_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_top_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','cong_per_cong_resp','both_bottom_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','cong_per_cong_resp','both_bottom_right')]]],color='black',lw=6.0);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#next separate out the incongruent percept/congruent response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-Down RT for Congruent Percept/Incongruent Response Trials\n For Each Type, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,1.9]); ax1.set_xticks([1,1.6]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['both_top_responses','both_bottom_responses']); 
ax1.bar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_top_responses')],color=colors[1], alpha = 1.0, width=0.2);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_bottom_responses')],color=colors[1], alpha = 1.0, width=0.2);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_top_responses')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_top_responses')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_top_responses')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_cong_resp','both_bottom_responses')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_bottom_responses')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_cong_resp','both_bottom_responses')]]],color='black',lw=6.0);   
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();



#finally check out the incongruent percept/incongreutn response trials
fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Top-Down RT for Incongruent Percept/Incongruent Response Trials\n For Each Shape, Single Target Trials, Left-Right Task, Subject %s'%id, size = 22);
ax1.set_ylim(400,950); ax1.set_yticks(arange(450,951,50)); ax1.set_xlim([0.7,3.1]); ax1.set_xticks([1,1.6,2.2,2.8]); #ax1.set_title('Bottom Up Task', size = 18, position = (.5, 0.9));
ax1.set_ylabel('Response time',size=18); ax1.set_xlabel('Condition',size=18);
ax1.set_xticklabels(['top_left\nbottom_left','top_left\nbottom_right','top_right\nbottom_left','top_right\nbottom_right']);
ax1.bar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_bottom_left')],color=colors[2], alpha = 1.0, width=0.4);
ax1.bar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_bottom_right')],color=colors[2], alpha = 1.0, width=0.4);
ax1.bar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_right_bottom_left')],color=colors[2], alpha = 1.0, width=0.4);
ax1.bar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_right_bottom_right')],color=colors[2], alpha = 1.0, width=0.4);
if id=='agg':
    ax1.errorbar(1,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_bottom_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_bottom_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(1.6,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_left_bottom_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_bottom_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_left_bottom_right')]]],color='black',lw=6.0);
    ax1.errorbar(2.2,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_right_bottom_left')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_right_bottom_left')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_right_bottom_left')]]],color='black',lw=6.0);
    ax1.errorbar(2.8,db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,'t','incong_per_incong_resp','top_right_bottom_right')],yerr=[[db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_right_bottom_right')]],
        [db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,'t','incong_per_incong_resp','top_right_bottom_right')]]],color='black',lw=6.0);    
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
show();  
    
    