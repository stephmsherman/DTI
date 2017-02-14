import glob, sys, os
import pandas as pd
import numpy as np

dti_folder = '/home3/kensinel/fMRI_DATA/SleepLDF/DTI/'
file = glob.glob('/home3/kensinel/fMRI_DATA/SleepLDF/combined_data/all_data_????-??-??.csv')

##read in data
d = pd.read_csv(file[0])

##change SleepLDF to SLEEPLDF in subject names
d['subject'] = d['subject'].str.replace('Sleep','SLEEP') 

###remove 2 participants who do not have DTI data
d = d[(d.subject != 'SLEEPLDF004') & (d.subject != 'SLEEPLDF006')]

##create column of ones for design matrix
d['one'] = 1

###get name of column that will be used in DTI analysis as covariate
covariate = 'meq_score'

##subset only columns of interest
m = d[['subject', 'one' , covariate]]

##remove missing data points
m = m[np.isfinite(m[covariate])]

subjects_included = m.subject

os.mkdir(dti_folder + covariate)

for subjects in subjects_included:
	#

##get number of participants
num = m.shape[0]

mat = m[['one', covariate]]

f = open(('/Volumes/LabShareFolder/SleepLDF/Combine_all_data/design_%s.mat' % covariate), 'w')
f.write('/NumWaves 2\n')
f.write('/NumPoints %d\n' % num)
f.write('/PPheights 1 1\n')
f.write('/Matrix\n')
mat.to_csv(f, sep = " ",header=False,index=False)
f.close()
