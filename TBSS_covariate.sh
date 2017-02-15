#!/usr/bin/env bash
## covariate TBSS
##steps 3 and 4 have to be run on only the participants included in the analysis 

covariate=$1

cd /home3/kensinel/fMRI_DATA/SleepLDF/DTI/tbss_$covariate

tbss_3_postreg -S
echo tbss_3_postreg done!
tbss_4_prestats 0.2
echo tbss_4_prestats done!

cd stats
randomise -i all_FA_skeletonised -o tbss -m mean_FA_skeleton_mask -d design_$covariate.mat -t design.con -n 500 --T2 -V

##view results
##change the tbss*.nii.gz file to see other results
#fslview $FSLDIR/data/standard/MNI152_T1_1mm.nii.gz mean_FA_skeleton.nii.gz -l Green -b 0.2,0.7 tbss_tfce_corrp_tstat1.nii.gz -l Red-Yellow -b 0.95,1

