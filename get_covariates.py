import glob, sys, os
import pandas as pd
import numpy as np
 
file = glob.glob('path/all_data_????-??-??.csv')

##read in data
d = pd.read_csv(file[0])

###remove 2 participants who do not have DTI data
d = d[(d.subject != 'SleepLDF004') & (d.subject != 'SleepLDF006')]

##create column of ones for design matrix
d['one'] = 1

###get name of column that will be used in DTI analysis as covariate
covariate = 'meq_score'

##subset only columns of interest
m = d[['subject', 'one' , covariate]]

##remove missing data points
m = m[np.isfinite(m[covariate])]

subjects_included = m.subject
subjects_included.replace('Sleep', 'SLEEP',regex=True)

##get number of participants
num = m.shape[0]

f = open(('path/design_%s.mat' % covariate), 'w')
f.write('/NumWaves 2\n')
f.write('/NumPoints %d\n' % num)
f.write('/PPheights 1 1\n')
f.write('/Matrix\n')
m.to_csv(f, sep = " ",header=False,index=False)
f.close()
