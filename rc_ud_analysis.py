#Response Conflict Data Analysis code
#Designed for the Up/Down response mapping version of the experiment
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


datapath = '/Users/jameswilmott/Documents/MATLAB/data/response_conflict/'; # '/Volumes/WORK_HD/data/temp_resp/'; # 
shelvepath =  '/Users/jameswilmott/Documents/Python/response_conflict/data/'; #'/Users/james/Documents/Python/response_conflict/data/';  #
savepath =  '/Users/jameswilmott/Documents/Python/response_conflict/figures/'; #'/Users/james/Documents/Python/response_conflict/data/'; #


#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'rc_ud_data');
individ_subject_data = shelve.open(shelvepath+'individ_rc_ud_data');

ids=['ud1','ud2','ud4','ud5','ud6','ud7','ud8','ud9','ud10','ud11','ud12','ud13','ud14','ud15','ud16','ud17','ud18','ud19']; #'jpw'    'ud3',

## Data Analysis Methods ####################################################################################################

#Top: 1-8 ; 17, 18; 21
#bottom: 9-16 ; 19, 20; 22

def analyzePrevTrialDifferentTrialTypeResponses(block_matrix, id):
	#check whether the previous trial, which is different from the current trial, is different depending on if prev response was same or diff from current
	if id=='agg':
		db=subject_data;
	else:
		db=individ_subject_data;
	for type in ['b','t']: 
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		for trial_types, name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
			for prev_resp_repeat, bool in zip(['repeat','switch'],[1,0]):
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				resp_index_counter=0;			
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;			
						for i in arange(0,len(b.trials)):			
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif (not(b.trials[i-1].trial_type in trial_types))&(b.trials[i].trial_type in trial_types)& \
							((b.trials[i-1].selected_type==b.trials[i].selected_type)==bool):
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);									
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
					1/0								
				db['%s_UD_%s_%s_%s_previstrial_response_mean_rt'%(id,type,name,prev_resp_repeat)]=mean(rts);	db['%s_UD_%s_%s_%s_previstrial_response_median_rt'%(id,type,name,prev_resp_repeat)]=median(rts);
				db['%s_UD_%s_%s_%s_previstrial_response_var_rt'%(id,type,name,prev_resp_repeat)]=var(rts);
				db['%s_UD_%s_%s_%s_previstrial_response_pc'%(id,type,name,prev_resp_repeat)]=pc(res);
				db.sync();
				if id=='agg':
					db['%s_UD_%s_%s_%s_previstrial_response_rt_bs_sems'%(id,type,name,prev_resp_repeat)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_%s_%s_previstrial_response_pc_bs_sems'%(id,type,name,prev_resp_repeat)]=compute_BS_SEM(res_matrix, 'pc');									
	db.sync();								

def analyzePrevTrialPotenialResponseBreakdown(block_matrix, id):
	#analyzes NBack for the different trial types broken down by what the actual potential correct response was (e.g., what trial type previously had as the correct response... the incong/ncong trial type won't have a brewkdon by this)
	if id=='agg':
		db=subject_data;
		prev_response_aggregated_data = pd.DataFrame(columns = ['sub_id','type','trial_type','current_response','prev_response','mean_rt','pc']);
		prev_response_data = pd.DataFrame(columns = ['sub_id','type','trial_type','current_response','prev_trial_type','prev_response','mean_rt','pc']);
	else:
		db=individ_subject_data;
	# break the nback analysis down by trial type	
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']: 
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		#for trial_types, name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
		for trial_types, name, response in zip([arange(1,9),(17,18),[21],arange(9,17),(19,20),[22]],['single_target','cong_per_cong_resp','incong_per_cong_resp','single_target','cong_per_cong_resp','incong_per_cong_resp'],['up','up','up','down','down','down']):
			#do a general response breakdwon irrespective of of the trial types as well
			for aggregated_trial_types, aggregated_response in zip([[1,2,3,4,5,6,7,8,17,18,21],[9,10,11,12,13,14,15,16,19,20,22]],['up','down']):
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				resp_index_counter=0;			
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;
						for i in arange(0,len(b.trials)):			
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif ((b.trials[i-1].trial_type in aggregated_trial_types))&(b.trials[i].trial_type in trial_types):	
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);			
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
					1/0
				db['%s_UD_%s_%s_%s_response_%s_prev_response_mean_rt'%(id,type,name,response,aggregated_response)]=mean(rts);	db['%s_UD_%s_%s_%s_response_%s_prev_response_median_rt'%(id,type,name,response,aggregated_response)]=median(rts);
				db['%s_UD_%s_%s_%s_response_%s_prev_response_var_rt'%(id,type,name,response,aggregated_response)]=var(rts);
				db['%s_UD_%s_%s_%s_response_%s_prev_response_pc'%(id,type,name,response,aggregated_response)]=pc(res);
				if id=='agg':
					db['%s_UD_%s_%s_%s_response_%s_prev_response_rt_bs_sems'%(id,type,name,response,aggregated_response)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_%s_%s_response_%s_prev_response_pc_bs_sems'%(id,type,name,response,aggregated_response)]=compute_BS_SEM(res_matrix, 'pc');			
					for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
						prev_response_aggregated_data.loc[resp_index_counter] = [i,type,name,response,aggregated_response,mean(r_scores),pc(res_scores),];
						resp_index_counter+=1;	

			#this other loop acts to loop through for each trial type and response
			for prev_trial_types, prev_name, prev_response in zip([arange(1,9),(17,18),[21],arange(9,17),(19,20),[22]],['single_target','cong_per_cong_resp','incong_per_cong_resp','single_target','cong_per_cong_resp','incong_per_cong_resp'],['up','up','up','down','down','down']):					
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				index_counter=0;
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;
						for i in arange(0,len(b.trials)):			
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif ((b.trials[i-1].trial_type in prev_trial_types))&(b.trials[i].trial_type in trial_types):	
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);					
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
					1/0
				db['%s_UD_%s_%s_%s_response_%s_prev_trialtype_%s_prev_response_mean_rt'%(id,type,name,response,prev_name,prev_response)]=mean(rts);	db['%s_UD_%s_%s_%s_response_%s_prev_trialtype_%s_prev_response_median_rt'%(id,type,name,response,prev_name,prev_response)]=median(rts);
				db['%s_UD_%s_%s_%s_response_%s_prev_trialtype_%s_prev_response_var_rt'%(id,type,name,response,prev_name,prev_response)]=var(rts);
				db['%s_UD_%s_%s_%s_response_%s_prev_trialtype_%s_prev_response_pc'%(id,type,name,response,prev_name,prev_response)]=pc(res);
				if id=='agg':
					db['%s_UD_%s_%s_%s_response_%s_prev_trialtype_%s_prev_response_rt_bs_sems'%(id,type,name,response,prev_name,prev_response)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_%s_%s_response_%s_prev_trialtype_%s_prev_response_pc_bs_sems'%(id,type,name,response,prev_name,prev_response)]=compute_BS_SEM(res_matrix, 'pc');	
					for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
						prev_response_data.loc[index_counter] = [i,type,name,response,prev_name,prev_response,mean(r_scores),pc(res_scores),];
						index_counter+=1;	
	db.sync();
	if id=='agg':
		prev_response_aggregated_data.to_csv(savepath+'prev_response_aggregated_across_trial_types.csv',index=False);	
		prev_response_data.to_csv(savepath+'prev_response_each_trial_type.csv',index=False);


def computeDiffPerceptDiffRespBreakdown(block_matrix, id):
	#analyze the different shape/different 
	if id=='agg':
		db=subject_data;
	else:
		db=individ_subject_data;
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']: 
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		#target shapes = 1, top left    2, top right     3, bottom left      4, bottom right
		for trial_types, name in zip([(23,24,25,26)],['incong_per_incong_resp']):
			for prev_trial_types, prev_name in zip([(23,24,25,26)],['incong_per_incong_resp']):
				#determine if the previous trial was of the same trial type (diff/diff), and if the response was the same and then whether the target shape was the same
				for shape_bool, same_shape in zip([1,0],['same_shapes','diff_shapes']):
					all_rt_matrix = [[] for su in block_matrix];
					all_res_matrix = [[] for su in block_matrix];					
					index_counter=0;
					for subj_nr,blocks in enumerate(block_matrix):
						for b in blocks:
							if b.block_type!=type:
								continue;
							for i in arange(0,len(b.trials)):			
								# 0 nback is satisfied if the first trials in a block or if the previous trial was different
								#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
								if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
									foo='bar';
								elif ((b.trials[i-1].trial_type in prev_trial_types))&(b.trials[i].trial_type in trial_types): #first to check same trial type
									if (b.trials[i-1].selected_type==b.trials[i].selected_type): #next to check same response
										if (b.trials[i].selected_type == 'up'): #this conditional allows me to determine which shape needs to be matched or not
											if (((any(b.trials[i].target_shapes)==1)&(any(b.trials[i-1].target_shapes)==1))| \
											((any(b.trials[i].target_shapes)==2)&(any(b.trials[i-1].target_shapes)==2))==shape_bool): #check if shapes were both 1 or both 2
												if b.trials[i].result==1:										
													all_rt_matrix[subj_nr].append(b.trials[i].response_time);
												all_res_matrix[subj_nr].append(b.trials[i].result);													
										elif (b.trials[i].selected_type=='down'):
											if (((any(b.trials[i].target_shapes)==3)&(any(b.trials[i-1].target_shapes)==3))| \
											((any(b.trials[i].target_shapes)==4)&(any(b.trials[i-1].target_shapes)==4))==shape_bool): #check if shapes were both 1 or both 2
												if b.trials[i].result==1:										
													all_rt_matrix[subj_nr].append(b.trials[i].response_time);
												all_res_matrix[subj_nr].append(b.trials[i].result);									
					ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
					res_matrix = all_res_matrix;
					rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
					print "%s %s number of trials for each participant: \n"%(type, same_shape);
					for goo in rt_matrix:
						print '%3.0f'%(len(goo));
					print '\n sum of trial numbers: %3.0f\n'%(sum([len(r) for r in rt_matrix]));	
					if len(rts)==0:
						continue;
						1/0
					db['%s_UD_%s_%s_currentandprevtype_same_response_%s_mean_rt'%(id,type,name,same_shape)]=mean(rts);	db['%s_UD_%s_%s_currentandprevtype_same_response_%s_median_rt'%(id,type,name,same_shape)]=median(rts);
					db['%s_UD_%s_%s_currentandprevtype_same_response_%s_var_rt'%(id,type,name,same_shape)]=var(rts);
					db['%s_UD_%s_%s_currentandprevtype_same_response_%s_pc'%(id,type,name,same_shape)]=pc(res);						
					db.sync();
					if id=='agg':								
						db['%s_UD_%s_%s_currentandprevtype_same_response_%s_rt_bs_sems'%(id,type,name,same_shape)]=compute_BS_SEM(rt_matrix, 'time');
						db['%s_UD_%s_%s_currentandprevtype_same_response_%s_pc_bs_sems'%(id,type,name,same_shape)]=compute_BS_SEM(res_matrix, 'pc');
	db.sync();
								
		

def analyzePreviousTrialActualResponse(block_matrix, id):
	#analyzes NBack for the different trial types broken down by what the actual GIVEN response was (e.g., what response was given on the previous trial and what was given the curren trial)
	if id=='agg':
		db=subject_data;
		prev_aggregated_actual_response_data = pd.DataFrame(columns = ['sub_id','type','current_response','prev_response','mean_rt','pc']);
		prev_actual_response_data = pd.DataFrame(columns = ['sub_id','type','trial_type','current_response','prev_trial_type','prev_response','mean_rt','pc']);
	else:
		db=individ_subject_data;
	# break the nback analysis down by trial type	
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']: 
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		for trial_types, name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
			for response in ['up','down']:
				for prev_trial_types, prev_name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
					for prev_response in ['up','down']:
						all_rt_matrix = [[] for su in block_matrix];
						all_res_matrix = [[] for su in block_matrix];					
						index_counter=0;
						for subj_nr,blocks in enumerate(block_matrix):
							for b in blocks:
								if b.block_type!=type:
									continue;
								for i in arange(0,len(b.trials)):
									# 0 nback is satisfied if the first trials in a block or if the previous trial was different
									#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
									if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
										foo='bar';
									elif ((b.trials[i-1].trial_type in prev_trial_types))&(b.trials[i-1].selected_type==prev_response)&(b.trials[i].trial_type in trial_types)&(b.trials[i].selected_type==response):	
										if b.trials[i].result==1:										
											all_rt_matrix[subj_nr].append(b.trials[i].response_time);
										all_res_matrix[subj_nr].append(b.trials[i].result);
						ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
						rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
						res_matrix = all_res_matrix;
						rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
						if len(rts)==0:
							continue;
							1/0										
						db['%s_UD_%s_%s_%s_actualresponse_%s_prev_trialtype_%s_prev_actualresponse_mean_rt'%(id,type,name,response,prev_name,prev_response)]=mean(rts);	db['%s_UD_%s_%s_%s_actualresponse_%s_prev_trialtype_%s_prev_actualresponse_median_rt'%(id,type,name,response,prev_name,prev_response)]=median(rts);
						db['%s_UD_%s_%s_%s_actualresponse_%s_prev_trialtype_%s_prev_actualresponse_var_rt'%(id,type,name,response,prev_name,prev_response)]=var(rts);
						db['%s_UD_%s_%s_%s_actualresponse_%s_prev_trialtype_%s_prev_actualresponse_pc'%(id,type,name,response,prev_name,prev_response)]=pc(res);
						db.sync();
						if id=='agg':
							db['%s_UD_%s_%s_%s_actualresponse_%s_prev_trialtype_%s_prev_actualresponse_rt_bs_sems'%(id,type,name,response,prev_name,prev_response)]=compute_BS_SEM(rt_matrix, 'time');
							db['%s_UD_%s_%s_%s_actualresponse_%s_prev_trialtype_%s_prev_actualresponse_pc_bs_sems'%(id,type,name,response,prev_name,prev_response)]=compute_BS_SEM(res_matrix, 'pc');	
							for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
								prev_actual_response_data.loc[index_counter] = [i,type,name,response,prev_name,prev_response,mean(r_scores),pc(res_scores),];
								index_counter+=1;
							
		#now collapse across all trial types together
		for current_response in ['up','down']:
			for prev_response in ['up','down']:
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				index_counter=0;
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;
						for i in arange(0,len(b.trials)):
							# 0 nback is satisfied if the first trials in a block or if the previous trial was different
							#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif (b.trials[i-1].selected_type==prev_response)&(b.trials[i].selected_type==current_response):	
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
					1/0									
				db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_mean_rt'%(id,type,current_response,prev_response)]=mean(rts);	db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_median_rt'%(id,type,current_response,prev_response)]=median(rts);
				db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_var_rt'%(id,type,current_response,prev_response)]=var(rts);
				db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_pc'%(id,type,current_response,prev_response)]=pc(res);
				db.sync();
				if id=='agg':
					db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_rt_bs_sems'%(id,type,current_response,prev_response)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_aggtrials_%s_actualresponse_aggtrialtype_%s_prev_actualresponse_pc_bs_sems'%(id,type,current_response,prev_response)]=compute_BS_SEM(res_matrix, 'pc');	
					for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
						prev_aggregated_actual_response_data.loc[index_counter] = [i,type,current_response,prev_response,mean(r_scores),pc(res_scores),];
						index_counter+=1;
						
						
						
	#THIS IS THE IMPORTANT CALCULATION					
	# previous trial congruent actual response or not
	for type in ['b','t']: 
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		for trial_types, name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
				for prev_trial_types, prev_name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
					for prev_cong, bool in zip(['congruent','incongruent'],[1,0]):
						all_rt_matrix = [[] for su in block_matrix];
						all_res_matrix = [[] for su in block_matrix];					
						index_counter=0;
						for subj_nr,blocks in enumerate(block_matrix):
							for b in blocks:
								if b.block_type!=type:
									continue;
								for i in arange(0,len(b.trials)):
									# 0 nback is satisfied if the first trials in a block or if the previous trial was different
									#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
									if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
										foo='bar';
									elif ((b.trials[i-1].trial_type in prev_trial_types))&(b.trials[i].trial_type in trial_types)&((b.trials[i-1].selected_type==b.trials[i].selected_type)==bool):	
										if b.trials[i].result==1:										
											all_rt_matrix[subj_nr].append(b.trials[i].response_time);
										all_res_matrix[subj_nr].append(b.trials[i].result);
						ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
						rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
						res_matrix = all_res_matrix;
						rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
						if len(rts)==0:
							continue;
							1/0
							
						db['%s_UD_%s_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,type,name,prev_name,prev_cong)]=mean(rts); db['%s_UD_%s_%s_%s_prev_trialtype_%s_actualresponse_median_rt'%(id,type,name,prev_name,prev_cong)]=median(rts);
						db['%s_UD_%s_%s_%s_prev_trialtype_%s_actualresponse_var_rt'%(id,type,name,prev_name,prev_cong)]=var(rts);
						db['%s_UD_%s_%s_%s_prev_trialtype_%s_actualresponse_pc'%(id,type,name,prev_name,prev_cong)]=pc(res);
						db.sync();
						if id=='agg':
							db['%s_UD_%s_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,type,name,prev_name,prev_cong)]=compute_BS_SEM(rt_matrix, 'time');
							db['%s_UD_%s_%s_%s_prev_trialtype_%s_actualresponse_pc_bs_sems'%(id,type,name,prev_name,prev_cong)]=compute_BS_SEM(res_matrix, 'pc');
							
							
	### Here, run the same analysis as above but isubtract the top-down means from each participant as if it were a 'baseline' condition. Idea is to determine if the response mapping/some weirdness in the data is special to the bottom up case
	#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
	for trial_types, name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
			for prev_trial_types, prev_name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
				for prev_cong, bool in zip(['congruent','incongruent'],[1,0]):	
					bu_all_rt_matrix = [[] for su in block_matrix];
					bu_all_res_matrix = [[] for su in block_matrix];
					td_all_rt_matrix = [[] for su in block_matrix];
					td_all_res_matrix = [[] for su in block_matrix];					
					index_counter=0;	
					for subj_nr,blocks in enumerate(block_matrix):
						for b in blocks:
							for i in arange(0,len(b.trials)):
								# 0 nback is satisfied if the first trials in a block or if the previous trial was different
								#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
								if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
									foo='bar';
								elif ((b.trials[i-1].trial_type in prev_trial_types))&(b.trials[i].trial_type in trial_types)&((b.trials[i-1].selected_type==b.trials[i].selected_type)==bool)&(b.block_type=='b'):	
									if b.trials[i].result==1:										
										bu_all_rt_matrix[subj_nr].append(b.trials[i].response_time);
									bu_all_res_matrix[subj_nr].append(b.trials[i].result);	
								elif ((b.trials[i-1].trial_type in prev_trial_types))&(b.trials[i].trial_type in trial_types)&((b.trials[i-1].selected_type==b.trials[i].selected_type)==bool)&(b.block_type=='t'):	
									if b.trials[i].result==1:										
										td_all_rt_matrix[subj_nr].append(b.trials[i].response_time);
									td_all_res_matrix[subj_nr].append(b.trials[i].result);								
					#bottom up versions
					bu_ind_rt_sds=[std(are) for are in bu_all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					bu_rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(bu_all_rt_matrix,bu_ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
					bu_res_matrix = bu_all_res_matrix;
					#top down versions
					td_ind_rt_sds=[std(are) for are in td_all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					td_rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(td_all_rt_matrix,td_ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
					td_res_matrix = td_all_res_matrix;				
						
					#now compute the difference between top-down and bottom-up
					rts = [mean(bu)-mean(td) for bu,td in zip(bu_rt_matrix, td_rt_matrix)];
					res = [pc(bu)-pc(td) for bu,td in zip(bu_res_matrix, td_res_matrix)];
					
					#in case this condition isn't possible...
					if len([r for r in rts])==0:
						#continue;
						1/0
					
					#save the data
					db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,name,prev_name,prev_cong)]=nanmean(rts);
					db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_pc'%(id,name,prev_name,prev_cong)]=mean(res);
					db.sync();					
					if id=='agg':
						db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,name,prev_name,prev_cong)]=compute_BS_SEM_from_means(rts, 'time');
						db['%s_UD_BUTD_diffference_%s_%s_prev_trialtype_%s_actualresponse_pc_bs_sems'%(id,name,prev_name,prev_cong)]=compute_BS_SEM_from_means(res, 'pc');					
										
	db.sync();		
	if id=='agg':
		prev_actual_response_data.to_csv(savepath+'prev_each_trialtype_actual_responses.csv',index=False);	
		prev_aggregated_actual_response_data.to_csv(savepath+'aggregated_current_and_prev_response.csv',index=False);		
		


def AnalyzeCongruencyPrevTrial(block_matrix, id):
	if id=='agg':
		db=subject_data;
		perceptual_congruence_data = pd.DataFrame(columns = ['sub_id','type','current_percept','prev_percept','mean_rt','pc']);
		response_congruence_data = pd.DataFrame(columns = ['sub_id','type','current_response','prev_response','mean_rt','pc']);
	else:
		db=individ_subject_data;	
	# break the nback analysis down by trial type	
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']:
		#perceptual incongruence first, e.g. was the percept being the same (e.g., two left shapes, or two right shapes) or not on trial N-1 predictive of RT depedning on if trial N was congruent or not
		for trial_types, name in zip([(17,18,19,20),(21,22,23,24,25,26)],['same_percept','different_percept']):
			for prev_trial_types, prev_name in zip([(17,18,19,20),(21,22,23,24,25,26)],['same_percept','different_percept']):
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				index_counter=0;
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;
						for i in arange(0,len(b.trials)):
							# 0 nback is satisfied if the first trials in a block or if the previous trial was different
							#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif (b.trials[i-1].trial_type in prev_trial_types)&(b.trials[i].trial_type in trial_types):	
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);		
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					1/0;
					continue;
					1/0		
				db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,type,name,prev_name)]=mean(rts);	db['%s_UD_%s_%s_%s_prev_trial_median_rt'%(id,type,name,prev_name)]=median(rts);
				db['%s_UD_%s_%s_%s_prev_trial_var_rt'%(id,type,name,prev_name)]=var(rts);
				db['%s_UD_%s_%s_%s_prev_trial_pc'%(id,type,name,prev_name)]=pc(res);		
				if id=='agg':
					db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,type,name,prev_name)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_%s_%s_prev_trial_pc_bs_sems'%(id,type,name,prev_name)]=compute_BS_SEM(res_matrix, 'pc');
					for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
						perceptual_congruence_data.loc[index_counter] = [i,type,name,prev_name,mean(r_scores),pc(res_scores),];
						index_counter+=1;
		#next run the anaylsis according to the congruence across trials of responses						
		for trial_types, name in zip([(17,18,19,20,21,22),(23,24,25,26)],['same_response','different_response']):
			for prev_trial_types, prev_name in zip([(17,18,19,20,21,22),(23,24,25,26)],['same_response','different_response']):
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				index_counter=0;
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;
						for i in arange(0,len(b.trials)):
							# 0 nback is satisfied if the first trials in a block or if the previous trial was different
							#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif (b.trials[i-1].trial_type in prev_trial_types)&(b.trials[i].trial_type in trial_types):	
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
					1/0										
				db['%s_UD_%s_%s_%s_prev_trial_mean_rt'%(id,type,name,prev_name)]=mean(rts);	db['%s_UD_%s_%s_%s_prev_trial_median_rt'%(id,type,name,prev_name)]=median(rts);
				db['%s_UD_%s_%s_%s_prev_trial_var_rt'%(id,type,name,prev_name)]=var(rts);
				db['%s_UD_%s_%s_%s_prev_trial_pc'%(id,type,name,prev_name)]=pc(res);		
				if id=='agg':
					db['%s_UD_%s_%s_%s_prev_trial_rt_bs_sems'%(id,type,name,prev_name)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_%s_%s_prev_trial_pc_bs_sems'%(id,type,name,prev_name)]=compute_BS_SEM(res_matrix, 'pc');								
					for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
						response_congruence_data.loc[index_counter] = [i,type,name,prev_name,mean(r_scores),pc(res_scores),];
						index_counter+=1;								
	db.sync();		
	if id=='agg':
		perceptual_congruence_data.to_csv(savepath+'perceptual_congruence.csv',index=False);	
		response_congruence_data.to_csv(savepath+'response_congruence.csv',index=False);								
								

def analyzePrevTrial(block_matrix, id):
	#analyzes NBack for the different trial types
	if id=='agg':
		db=subject_data;
		data = pd.DataFrame(columns = ['sub_id','type','trial_type','prev_trial_type','mean_rt','pc']);
	else:
		db=individ_subject_data;
	# break the nback analysis down by trial type	
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']: 
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		for trial_types, name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
			#this second loop acts to loop through for each trial type given the trial type in the outer loop above
			for test_trial_types, test_name in zip([arange(1,17),(17,18,19,20),(21,22),(23,24,25,26)],['single_target','cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
				all_rt_matrix = [[] for su in block_matrix];
				all_res_matrix = [[] for su in block_matrix];					
				index_counter=0;
				for subj_nr,blocks in enumerate(block_matrix):
					for b in blocks:
						if b.block_type!=type:
							continue;
						for i in arange(0,len(b.trials)):
							# 0 nback is satisfied if the first trials in a block or if the previous trial was different
							#however, for now exclude the first trial in a block because it can't be broken down by which trial type preceeded it
							if (b.trials[i].trial_nr==0)&(b.trials[i].trial_type in trial_types):						
								foo='bar';
							elif ((b.trials[i-1].trial_type in test_trial_types))&(b.trials[i].trial_type in trial_types):	
								if b.trials[i].result==1:										
									all_rt_matrix[subj_nr].append(b.trials[i].response_time);
								all_res_matrix[subj_nr].append(b.trials[i].result);
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = all_res_matrix;
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
					1/0
				db['%s_UD_%s_%s_prev_trial_%s_mean_rt'%(id,type,name,test_name)]=mean(rts);	db['%s_UD_%s_%s_prev_trial_%s_median_rt'%(id,type,name,test_name)]=median(rts);	db['%s_UD_%s_%s_prev_trial_%s_var_rt'%(id,type,name,test_name)]=var(rts);
				db['%s_UD_%s_%s_prev_trial_%s_pc'%(id,type,name,test_name)]=pc(res);
				if id=='agg':
					db['%s_UD_%s_%s_prev_trial_%s_rt_bs_sems'%(id,type,name,test_name)]=compute_BS_SEM(rt_matrix, 'time');
					db['%s_UD_%s_%s_prev_trial_%s_pc_bs_sems'%(id,type,name,test_name)]=compute_BS_SEM(res_matrix, 'pc');	
					for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
						data.loc[index_counter] = [i,type,name,test_name,mean(r_scores),pc(res_scores),];
						index_counter+=1;				
	db.sync();
	if id=='agg':
		data.to_csv(savepath+'prev_trial_1back.csv',index=False);				


def analyzeDistShapeEffect(trial_matrix,id):
	#trial_matrix should be a list of trials for each subjects
	#get appropriate database to store data
	if id=='agg':
		db=subject_data;
		#data = pd.DataFrame(columns = ['sub_id','type','nr_match','mean_rt','pc']);
	else:
		db=individ_subject_data;
	trials = [tee for person in trial_matrix for tee in person]; #collect all trials together in a single list
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']: 
		#cycle through number of targets. Only do single targets for now
		for nrt in [1]:
			t = [tee for tee in trials if (tee.block_type==type)]; #segment the relevant trials
			t_matrix = [[tee for tee in trs if (tee.block_type==type)] for trs in trial_matrix];
			#now go through and separate trials where the 5th distractor's shape matched the target or not
			for match_5thdist in [0,1]:
				#first do this analysis collapsing across all 4 target shapes
				all_rt_matrix = [[tee.response_time for tee in ts if(tee.result==1)&(tee.fifth_distractor_match==match_5thdist)] for ts in t_matrix];
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
				res_matrix = [[tee.result for tee in ts if(tee.fifth_distractor_match==match_5thdist)] for ts in t_matrix];
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
				#compute and display the data 
				db['%s_UD_%s_%s_targets_%s_5thdmatch_mean_rt'%(id,type,nrt,match_5thdist)]=mean(rts); db['%s_UD_%s_%s_targets_%s_5thdmatch_var_rt'%(id,type,nrt,match_5thdist)]=var(rts); db['%s_UD_%s_%s_targets_%s_5thdmatch_median_rt'%(id,type,nrt,match_5thdist)]=median(rts); 
				db['%s_UD_%s_%s_targets_%s_5thdmatch_pc'%(id,type,nrt,match_5thdist)]=pc(res);
				print '%s %s %s nr of targets 5th dist match = %s rt: %3.2f'%(id,type,nrt,match_5thdist, mean(rts));
				db.sync();
				if id=='agg':
					db['%s_UD_%s_%s_targets_%s_5thdmatch_rt_bs_sems'%(id,type,nrt,match_5thdist)] = compute_BS_SEM(rt_matrix,'time'); db['%s_UD_%s_%s_targets_%s_5thdmatch_pc_bs_sems'%(id,type,nrt,match_5thdist)] = compute_BS_SEM(res_matrix, 'pc');
					#append all the datae for each subject together in the dataframe for use in ANOVA
					
			#then run this separately for each unique target shape
			for shape in [1,2,3,4]:
				for match_5thdist in [0,1]:
					all_rt_matrix = [[tee.response_time for tee in ts if(tee.result==1)&(tee.fifth_distractor_match==match_5thdist)&(tee.target_shapes[0]==shape)] for ts in t_matrix];
					ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
					res_matrix = [[tee.result for tee in ts if(tee.fifth_distractor_match==match_5thdist)&(tee.target_shapes[0]==shape)] for ts in t_matrix];
					rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];						
					if len(rts)==0:
						continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)				
					#compute and display the data 
					db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_mean_rt'%(id,type,nrt,shape,match_5thdist)]=mean(rts); db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_var_rt'%(id,type,nrt,shape,match_5thdist)]=var(rts);
					db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_median_rt'%(id,type,nrt,shape,match_5thdist)]=median(rts); 
					db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc'%(id,type,nrt,shape,match_5thdist)]=pc(res);
					print '%s %s %s nr of targets target shape = %s 5th dist match = %s rt: %3.2f'%(id,type,nrt,shape,match_5thdist, mean(rts));
					db.sync();
					if id=='agg':
						db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_rt_bs_sems'%(id,type,nrt,shape,match_5thdist)] = compute_BS_SEM(rt_matrix,'time'); db['%s_UD_%s_%s_targets_%s_targetshape_%s_5thdmatch_pc_bs_sems'%(id,type,nrt,shape,match_5thdist)] = compute_BS_SEM(res_matrix, 'pc');
						#append all the datae for each subject together in the dataframe for use in ANOVA
			
			#now run this same analysis looking at the number of similar response items in the display(e.g., the aggregation of trials with same shape as fifth distractor and the other same response)
			#first collapse across the target shapes to look at only responses.. 
			for resp in ['up','down']:
				for nr_matchdist in [2,3]:			
					all_rt_matrix = [[tee.response_time for tee in ts if(tee.result==1)&(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_types[0]==resp)] for ts in t_matrix];
					ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean					
					res_matrix = [[tee.result for tee in ts if(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_types[0]==resp)] for ts in t_matrix];
					rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];						
					if len(rts)==0:
						continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)					
					#compute and display the data 					
					db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_mean_rt'%(id,type,nrt,resp,nr_matchdist)]=mean(rts); db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_var_rt'%(id,type,nrt,resp,nr_matchdist)]=var(rts);				
					db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_median_rt'%(id,type,nrt,resp,nr_matchdist)]=median(rts);
					db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc'%(id,type,nrt,resp,nr_matchdist)]=pc(res);					
					print '%s %s %s nr of targets resp = %s nr matching dists %s rt: %3.2f'%(id,type,nrt, resp, nr_matchdist, mean(rts));
					db.sync();					
					if id=='agg':					
						db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,type,nrt,resp,nr_matchdist)] = compute_BS_SEM(rt_matrix,'time');
						db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,type,nrt,resp,nr_matchdist)] = compute_BS_SEM(res_matrix, 'pc');					
					
			
			#now pull it apart depending on the target shape
			for shape,resp in zip([1,2,3,4],['up','up','down','down']):
				for nr_matchdist in [2,3]:
					all_rt_matrix = [[tee.response_time for tee in ts if(tee.result==1)&(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_shapes[0]==shape)] for ts in t_matrix];
					ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
					res_matrix = [[tee.result for tee in ts if(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_shapes[0]==shape)] for ts in t_matrix];
					rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];						
					if len(rts)==0:
						continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)					
					#compute and display the data 
					db['%s_UD_%s_%s_targets_%s_targetshape_%s_resp_%s_nrmatchdist_mean_rt'%(id,type,nrt,shape,resp,nr_matchdist)]=mean(rts); db['%s_UD_%s_%s_targets_%s_targetshape_%s_resp_%s_nrmatchdist_var_rt'%(id,type,nrt,shape,resp,nr_matchdist)]=var(rts);				
					db['%s_UD_%s_%s_targets_%s_targetshape_%s_resp_%s_nrmatchdist_median_rt'%(id,type,nrt,shape,resp,nr_matchdist)]=median(rts);
					db['%s_UD_%s_%s_targets_%s_targetshape_%s_resp_%s_nrmatchdist_pc'%(id,type,nrt,shape,resp,nr_matchdist)]=pc(res);
					print '%s %s %s nr of targets target shape = %s resp = %s nr matching dists %s rt: %3.2f'%(id,type,nrt,shape, resp, nr_matchdist, mean(rts));
					db.sync();
					if id=='agg':					
						db['%s_UD_%s_%s_targets_%s_targetshape_%s_resp_%s_nrmatchdist_rt_bs_sems'%(id,type,nrt,shape,resp,nr_matchdist)] = compute_BS_SEM(rt_matrix,'time');
						db['%s_UD_%s_%s_targets_%s_targetshape_%s_resp_%s_nrmatchdist_pc_bs_sems'%(id,type,nrt,shape,resp,nr_matchdist)] = compute_BS_SEM(res_matrix, 'pc');
						#append all the datae for each subject together in the dataframe for use in ANOVA					
			
			#last, determine whether the response associated with the target shape impacted RTs by taking out the trials where the5th distractor shape was the same as the target
			#this might be the most important analysis
			#first collapse across the target shapes to look at only responses.. 
			for resp in ['up','down']:
				for nr_matchdist in [2,3]:			
					all_rt_matrix = [[tee.response_time for tee in ts if(tee.result==1)&(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_types[0]==resp)&(tee.fifth_distractor_match==0)] for ts in t_matrix];
					ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean					
					res_matrix = [[tee.result for tee in ts if(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_types[0]==resp)&(tee.fifth_distractor_match==0)] for ts in t_matrix];
					rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];						
					if len(rts)==0:
						continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)					
					#compute and display the data 					
					db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,type,nrt,resp,nr_matchdist)]=mean(rts); db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_var_rt'%(id,type,nrt,resp,nr_matchdist)]=var(rts);				
					db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_median_rt'%(id,type,nrt,resp,nr_matchdist)]=median(rts);
					db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_pc'%(id,type,nrt,resp,nr_matchdist)]=pc(res);					
					db.sync();					
					if id=='agg':					
						db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,type,nrt,resp,nr_matchdist)] = compute_BS_SEM(rt_matrix,'time');
						db['%s_UD_%s_%s_targets_%s_resp_%s_nrmatchdist_5thdnotmatch_pc_bs_sems'%(id,type,nrt,resp,nr_matchdist)] = compute_BS_SEM(res_matrix, 'pc');
						
			
			#do the above analysis separating out the different shapes
			for shape,resp in zip([1,2,3,4],['up','up','down','down']):
				for nr_matchdist in [2,3]:			
					all_rt_matrix = [[tee.response_time for tee in ts if(tee.result==1)&(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_shapes[0]==shape)&(tee.fifth_distractor_match==0)] for ts in t_matrix];
					ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
					rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean					
					res_matrix = [[tee.result for tee in ts if(sum([tee.distractor_types==resp])==nr_matchdist)&(tee.target_shapes[0]==shape)&(tee.fifth_distractor_match==0)] for ts in t_matrix];
					rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];						
					if len(rts)==0:
						continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
					#compute and display the data 					
					db['%s_UD_%s_%s_targets_%s_shape_%s_resp_%s_nrmatchdist_5thdnotmatch_mean_rt'%(id,type,nrt,shape,resp,nr_matchdist)]=mean(rts); db['%s_UD_%s_%s_targets_%s_shape_%s_resp_%s_nrmatchdist_5thdnotmatch_var_rt'%(id,type,nrt,shape,resp,nr_matchdist)]=var(rts);				
					db['%s_UD_%s_%s_targets_%s_shape_%s_resp_%s_nrmatchdist_5thdnotmatch_median_rt'%(id,type,nrt,shape,resp,nr_matchdist)]=median(rts);
					db['%s_UD_%s_%s_targets_%s_shape_%s_resp_%s_nrmatchdist_5thdnotmatch_pc'%(id,type,nrt,shape,resp,nr_matchdist)]=pc(res);					
					db.sync();					
					if id=='agg':					
						db['%s_UD_%s_%s_targets_%s_shape_%s_resp_%s_nrmatchdist_5thdnotmatch_rt_bs_sems'%(id,type,nrt,shape,resp,nr_matchdist)] = compute_BS_SEM(rt_matrix,'time');
						db['%s_UD_%s_%s_targets_%s_shape_%s_resp_%s_nrmatchdist_5thdnotmatch_pc_bs_sems'%(id,type,nrt,shape,resp,nr_matchdist)] = compute_BS_SEM(res_matrix, 'pc');									
					
	db.sync();


def computeSTBias(trial_matrix, id='agg'):
	#determine if there is a bias in responding for the single target trials
	#get appropriate database to store data
	if id=='agg':
		db=subject_data;
	else:
		db=individ_subject_data;
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']: 
		#cycle through number of targets. Only do single targets for now
		for nrt in [1]:
			for target_shape in [1,2,3,4]:
				t_matrix = [[tee for tee in trs if (tee.block_type==type)] for trs in trial_matrix];
				all_rt_matrix = [[tee.response_time for tee in ts if((tee.result==1)&(tee.nr_targets==nrt)&(tee.target_shapes[0]==target_shape))] for ts in t_matrix];
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean			
				res_matrix = [[tee.result for tee in ts if((tee.nr_targets==nrt)&(tee.target_shapes[0]==target_shape))] for ts in t_matrix];
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];						
				if len(rts)==0:
					continue;
				db['%s_UD_%s_%s_targets_%s_targetshape_mean_rt'%(id,type,nrt,target_shape)]=mean(rts);	db['%s_UD_%s_%s_targets_%s_targetshape_median_rt'%(id,type,nrt,target_shape)]=median(rts);	db['%s_UD_%s_%s_targets_%s_targetshape_var_rt'%(id,type,nrt,target_shape)]=var(rts);
				db['%s_UD_%s_%s_targets_%s_targetshape_pc'%(id,type,nrt,target_shape)]=pc(res);
				db.sync();
				if id=='agg':					
					db['%s_UD_%s_%s_targets_%s_targetshape_rt_bs_sems'%(id,type,nrt,target_shape)] = compute_BS_SEM(rt_matrix,'time');
					db['%s_UD_%s_%s_targets_%s_targetshape_pc_bs_sems'%(id,type,nrt,target_shape)] = compute_BS_SEM(res_matrix, 'pc');				
	db.sync();


def computeNT(trial_matrix, id='agg'):
	#trial_matrix should be a list of trials for each subjects
	#get appropriate database to store data
	if id=='agg':
		db=subject_data;
		data = pd.DataFrame(columns = ['sub_id','type','nr_targets','mean_rt','pc']);
	else:
		db=individ_subject_data;
    #here cycle through the total number of stimuli and number of distractors, finding the RT and accuracy for each combo
	#run this analysis separatel for the bottom up and top down blocks
	index_counter = 0;
	for type in ['b','t']: 
		#cycle through number of targets. Only do single targets for now
		for nrt in [1,2]:
			t_matrix = [[tee for tee in trs if (tee.block_type==type)] for trs in trial_matrix];
			all_rt_matrix = [[tee.response_time for tee in ts if((tee.result==1)&(tee.nr_targets==nrt))] for ts in t_matrix];
			ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
			rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean			
			res_matrix = [[tee.result for tee in ts if(tee.nr_targets==nrt)] for ts in t_matrix];
			rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
			
			if (type == 'b')&(nrt==1):
				poss = array([len([tee.response_time for tee in ts if ((tee.nr_targets==nrt)&(tee.block_type==type))]) for ts in trial_matrix]);
				excluded = poss - array([len(gub) for gub in rt_matrix]);				
				1/0;
			
			
			if len(rts)==0:
				continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
			db['%s_UD_%s_%s_targets_mean_rt'%(id,type,nrt)]=mean(rts);	db['%s_UD_%s_%s_targets_median_rt'%(id,type,nrt)]=median(rts);	db['%s_UD_%s_%s_targets_var_rt'%(id,type,nrt)]=var(rts);
			db['%s_UD_%s_%s_targets_pc'%(id,type,nrt)]=pc(res);
			print '%s %s %s nr of targets = rt: %3.2f'%(id,type,nrt,mean(rts));
			db.sync();
			if id=='agg':					
				db['%s_UD_%s_%s_targets_rt_bs_sems'%(id,type,nrt)] = compute_BS_SEM(rt_matrix,'time');
				db['%s_UD_%s_%s_targets_pc_bs_sems'%(id,type,nrt)] = compute_BS_SEM(res_matrix, 'pc');
				#append data to the dataframe object
				for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
					data.loc[index_counter] = [i,type,nrt,mean(r_scores),pc(res_scores),];
					index_counter+=1;
				
	db.sync();	
	if id=='agg':
		data.to_csv(savepath+'nr_targets.csv',index=False);

def computeCongruency(trial_matrix, id = 'agg'):
	#computes the response and perceptual incongruence data for the two target trials
	#trial_matrix should be a list of trials for each subjects
	#get appropriate database to store data
	if id=='agg':
		db=subject_data;
		data = pd.DataFrame(columns = ['sub_id','type','congruency','mean_rt','pc']);
	else:
		db=individ_subject_data;	
    #here cycle through the total number of stimuli and number of distractors, finding the RT and accuracy for each combo
	#run this analysis separatel for the bottom up and top down blocks
	index_counter = 0;
	for type in ['b','t']:
		t_matrix = [[tee for tee in trs if (tee.block_type==type)] for trs in trial_matrix];
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong
		for trial_types, name in zip([(17,18,19,20),(21,22),(23,24,25,26)],['cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp']):
			all_rt_matrix = [[tee.response_time for tee in ts if((tee.result==1)&(tee.nr_targets==2)&(tee.trial_type in trial_types))] for ts in t_matrix];
			ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
			rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean			
			res_matrix = [[tee.result for tee in ts if((tee.nr_targets==2)&(tee.trial_type in trial_types))] for ts in t_matrix];
			rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
			
			if (type == 'b')&(name == 'incong_per_incong_resp'):
				poss = array([len([tee.response_time for tee in ts if ((tee.trial_type in trial_types)&(tee.block_type==type))]) for ts in trial_matrix]);
				excluded = poss - array([len(gub) for gub in rt_matrix]);				
				1/0;			
			
			
			
			if len(rts)==0:
				continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)			
			db['%s_UD_%s_2_targets_%s_mean_rt'%(id,type,name)]=mean(rts);	db['%s_UD_%s_2_targets_%s_median_rt'%(id,type,name)]=median(rts);	db['%s_UD_%s_2_targets_%s_var_rt'%(id,type,name)]=var(rts);
			db['%s_UD_%s_2_targets_%s_pc'%(id,type,name)]=pc(res);
			print '%s %s %s = rt: %3.2f'%(id,type,name,mean(rts));
			print '%s %s %s = PC: %1.3f'%(id,type,name,pc(res));
			db.sync();
			if id=='agg':
				db['%s_UD_%s_2_targets_%s_rt_bs_sems'%(id,type,name)] = compute_BS_SEM(rt_matrix,'time');
				db['%s_UD_%s_2_targets_%s_pc_bs_sems'%(id,type,name)] = compute_BS_SEM(res_matrix, 'pc');
				for i,r_scores,res_scores in zip(linspace(1,len(rt_matrix),len(rt_matrix)),rt_matrix,res_matrix):
					data.loc[index_counter] = [i,type,name,mean(r_scores),pc(res_scores),];
					index_counter+=1;				
	db.sync();
	if id=='agg':
		data.to_csv(savepath+'congruency.csv',index=False);

def computeCongruencyForEachTrialType(trial_matrix, id = 'agg'):	
	#computes the response and perceptual incongruence data for the two target trial, separated out individually for the trial types
	#trial_matrix should be a list of trials for each subjects
	#get appropriate database to store data
	if id=='agg':
		db=subject_data;
	else:
		db=individ_subject_data;
	#run this analysis separatel for the bottom up and top down blocks
	for type in ['b','t']:
		t_matrix = [[tee for tee in trs if (tee.block_type==type)] for trs in trial_matrix];
		#cycle through the different types: resp cong, perc cong; resp cong, perc incong; respon incong, percept incong		
		for trial_types, name, specific_names in zip([(17,18,19,20),(21,22),(23,24,25,26)],['cong_per_cong_resp','incong_per_cong_resp','incong_per_incong_resp'],
			[('both_top_left','both_top_right','both_bottom_left','both_bottom_right'),('both_top_responses','both_bottom_responses'),('top_left_bottom_left','top_left_bottom_right','top_right_bottom_left','top_right_bottom_right')]):
			for tt, spec_trial in zip(trial_types,specific_names):
				all_rt_matrix = [[tee.response_time for tee in ts if((tee.result==1)&(tee.nr_targets==2)&(tee.trial_type==tt))] for ts in t_matrix];				
				ind_rt_sds=[std(are) for are in all_rt_matrix];  #get individual rt sds and il sds to 'shave' the rts of extreme outliers
				rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)];		
				res_matrix = [[tee.result for tee in ts if((tee.nr_targets==2)&(tee.trial_type==tt))] for ts in t_matrix];
				rts = [r for y in rt_matrix for r in y]; res = [s for y in res_matrix for s in y];
				if len(rts)==0:
					continue;
				db['%s_UD_%s_2_targets_%s_%s_mean_rt'%(id,type,name,spec_trial)]=mean(rts);	db['%s_UD_%s_2_targets_%s_%s_median_rt'%(id,type,name,spec_trial)]=median(rts);	db['%s_UD_%s_2_targets_%s_%s_var_rt'%(id,type,name,spec_trial)]=var(rts);
				db['%s_UD_%s_2_targets_%s_%s_pc'%(id,type,name,spec_trial)]=pc(res);
				print '%s %s %s %s = rt: %3.2f'%(id,type,name,spec_trial,mean(rts));					
				db.sync();
				if id=='agg':
					db['%s_UD_%s_2_targets_%s_%s_rt_bs_sems'%(id,type,name,spec_trial)] = compute_BS_SEM(rt_matrix,'time');
					db['%s_UD_%s_2_targets_%s_%s_pc_bs_sems'%(id,type,name,spec_trial)] = compute_BS_SEM(res_matrix, 'pc');				
	db.sync();


def compute_BS_SEM(data_matrix, type):
    #calculate the between-subjects standard error of the mean. data_matrix should be matrix of trials including each subject
    #should only pass data matrix into this function after segmenting into relevant conditions
	agg_data = [datum for person in data_matrix for datum in person]; #get all the data together
	n = len(data_matrix);
	if type=='time':
		grand_mean = mean(agg_data);
		matrix = [[dee for dee in datas] for datas in data_matrix];
		err = [mean(d) for d in matrix if (len(d)>0)]-grand_mean;
		squared_err = err**2;
		MSE = sum(squared_err)/(n-1);
	elif type=='pc':
		grand_pc = pc(agg_data);
		matrix = [[dee for dee in datas] for datas in data_matrix];
		err = [pc(d) for d in matrix if (len(d)>0)]-grand_pc;
		squared_err = err**2;
		MSE = sum(squared_err)/(n-1);
	denom = sqrt(n);
	standard_error_estimate=sqrt(MSE)/float(denom);
	return standard_error_estimate;


#compute the Bs SEMS using a matrix of means, as well
#designed to deal with NaNs by cutting them out of the analysis
def compute_BS_SEM_from_means(mean_matrix, type):
    #calculate the between-subjects standard error of the mean. data_matrix should be matrix of subjet means
    #should only pass data matrix into this function after segmenting into relevant conditions
	if type=='time':
		grand_mean = nanmean(mean_matrix);
		err = mean_matrix-grand_mean;
		squared_err = err**2;
		non_nans = [r for r in squared_err if ~(isnan(r))]	
		MSE = sum(non_nans)/(len(non_nans)-1);
		n = len(non_nans);
	elif type=='pc':
		grand_pc = nanmean(mean_matrix);
		err = mean_matrix-grand_pc;
		squared_err = err**2;
		non_nans = [r for r in squared_err if ~(isnan(r))]	
		MSE = sum(non_nans)/(len(non_nans)-1);
		n = len(non_nans);
	denom = sqrt(n);
	standard_error_estimate=sqrt(MSE)/float(denom);
	return standard_error_estimate;

## Data Importation Functions ################################################################################################

#define a function to import individual .mat data files
def loadBlock(subid,block_nr):
	#returns a single Block object corresponding to the block number and subject id
	#block type should be a string corresponding to the task type(e.g. 'Discrim')
	filename = glob(datapath+'%s'%subid+'/'+'*_UD_*_%s_%d.mat'%(subid,block_nr)); #block_type,
	matdata = loadmat(filename[0],struct_as_record=False,squeeze_me=True)['block']; #use scipy loadmat() to load in the files
	block=Block(matdata); #here, create Block object with dictionary of trial data in matdata
	return block;

#define a function to import all .mat data files for a given subject
def loadAllBlocks(subid):
    filenames = glob(datapath+'%s'%subid+'/'+'*_UD_*_%s_[1-9].mat'%subid); #got to check that this regex works here
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
		self.trials = [Trial(trialData,i) for i,trialData in  enumerate(matStructure.trial_data)];
        
#define a Trial object that will hold the individual trial data for discrimination tasks
class Trial(object):
	#object being passed into this Trial instance should be a dictionary corresponding to the trial data for this given trial
	def __init__(self, trialData, i):
		self.sub_id = str(trialData.sub_id);
		self.trial_nr = i;
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
		#here, determine if the last distractor shape (5th distractor) matched the target if it's a single target trials
		if self.nr_targets==2:
			self.fifth_distractor_match = -1;
		elif self.nr_targets==1:
			self.fifth_distractor_match = self.target_shapes[0]==self.distractor_shapes[-1];
		self.trial_times = trialData.trial_times
		self.response_time = self.trial_times.response_time*1000; #ms
		self.response = trialData.response;
		self.result = trialData.result;
		self.selected_type = str(trialData.selected_type);
		self.drift_shift = trialData.drift_shift;
		
		
# datapath = '/Users/james/Documents/MATLAB/data/response_conflict/'; #'/Users/jameswilmott/Documents/MATLAB/data/response_conflict/'; #
# shelvepath =  '/Users/james/Documents/Python/response_conflict/data/';  #'/Users/jameswilmott/Documents/Python/response_conflict/data/'; #
# savepath = '/Users/james/Documents/Python/response_conflict/figures/'; #'/Users/jameswilmott/Documents/Python/response_conflict/figures/'; #		
		