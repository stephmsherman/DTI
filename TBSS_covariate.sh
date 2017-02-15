#!/usr/bin/env bash
## covariate TBSS

covariate=$1

cd /home3/kensinel/fMRI_DATA/SleepLDF/scripts/dti_analyses/

tbss_3_postreg -S
echo tbss_3_postreg done!
tbss_4_prestats 0.2
echo tbss_4_prestats done!

cd stats
randomise -i all_FA_skeletonised -o tbss -m mean_FA_skeleton_mask -d design_$covariate.mat -t design.con -n 500 --T2 -V
