###PURPOSE: this script takes the all_data_<date>.csv from the brain510 SleepLDF/Combine_all_data folder and grabs the covariate of interest (column name of all_data that you want to see whether it correlates with FA values) to create the design matrix for the TBSS analysis

###things that need to be modified after more data collection
#1. if more subjects do not have DTI data then their subject numbers need to be added in the code under 'remove'
#2. make sure the tbss folder contains was run on all the available subjects

import glob, sys, os, shutil
import pandas as pd
import numpy as np

dti_folder = '/home3/kensinel/fMRI_DATA/SleepLDF/DTI'

##file to format covariate data
file = glob.glob('/home3/kensinel/fMRI_DATA/SleepLDF/combined_data/all_data_????-??-??.csv')

##read in data
##may want to add something that ensures the order is correct ascending
d = pd.read_csv(file[0])

##change SleepLDF to SLEEPLDF in subject names
d['subject'] = d['subject'].str.replace('Sleep','SLEEP') 

###remove 2 participants who do not have DTI data
d = d[(d.subject != 'SLEEPLDF004') & (d.subject != 'SLEEPLDF006')]

###sort (just in case subjects are out of order)
d.sort(['subject'],ascending=[True], inplace=True)

##create column of ones for design matrix
d['one'] = 1

###get name of column that will be used in DTI analysis as covariate
covariate = raw_input('Name of covariate: ')

##subset only columns of interest
m = d[['subject', 'one' , covariate]]

##remove missing data points
m = m[np.isfinite(m[covariate])]

##make a list of the subjects that are included in this analysis
subjects_included = m.subject

###make directories as if ran first steps of TBSS
os.makedirs(dti_folder + '/tbss_' + covariate)
newdir = dti_folder + '/tbss_' + covariate + '/FA'
os.makedirs(newdir)
stats_dir = dti_folder + '/tbss_' + covariate + '/stats'
os.makedirs(stats_dir)

##assumes you are only looking at a single covariate
shutil.copy((dti_folder + '/tbss/stats/design.con'), stats_dir)

##create empty list to fill with paths of files that need to copied
files_to_copy = []
for subjects in subjects_included:	
	s = glob.glob('/home3/kensinel/fMRI_DATA/SleepLDF/DTI/tbss/FA/*%s*' % subjects)
	for f in s:	
		files_to_copy.append(f)

##copies all the files to the newly created tbss_covariate/FA directory
for final_files in files_to_copy:
	shutil.copy(final_files, newdir)

###copy other files important for running TBSS
### the target.nii.gz file is the FMRIB58_FA_1mm.nii.gz standard map
shutil.copy('/home3/kensinel/fMRI_DATA/SleepLDF/DTI/tbss/FA/target.nii.gz',newdir)
shutil.copy('/home3/kensinel/fMRI_DATA/SleepLDF/DTI/tbss/FA/best.msf',newdir)

##########creates the design_covariate.mat file to run randomise
##get number of participants
num = m.shape[0]
#use only the columns that go into the .mat
mat = m[['one', covariate]]

f = open((stats_dir + '/design_%s.mat' % covariate), 'w')
f.write('/NumWaves 2\n')
f.write('/NumPoints %d\n' % num)
f.write('/PPheights 1 1\n')
f.write('/Matrix\n')
mat.to_csv(f, sep = " ",header=False,index=False)
f.close()

###now need to run steps of TBSS that require all the FA maps to be combined for only the subjects
##included in this particular analysis

