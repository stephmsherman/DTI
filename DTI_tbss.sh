#!/usr/bin/env bash
## TBSS (steps 1-4)
######this script runs TBSS on all the subjects that have DTI and puts them in a base folder called tbss
##the tbss folder is going to be used to pull the processed DTI data into other folders to run stats

###when add more subjects: need to date the previous tbss folder (tbss_??_??_??) and create a new one (tbss)

#http://www.fmrib.ox.ac.uk/fslcourse/lectures/practicals/fdt/index.htm
for sub in SLEEPLDF001 SLEEPLDF002 SLEEPLDF003 SLEEPLDF005 SLEEPLDF007 SLEEPLDF008 SLEEPLDF009 SLEEPLDF010 SLEEPLDF011 SLEEPLDF012 SLEEPLDF013 SLEEPLDF014 SLEEPLDF015 SLEEPLDF016 SLEEPLDF017 SLEEPLDF018 SLEEPLDF019 SLEEPLDF020 SLEEPLDF021 SLEEPLDF022 SLEEPLDF023 SLEEPLDF024 SLEEPLDF025 SLEEPLDF026 SLEEPLDF027 SLEEPLDF028 SLEEPLDF029 SLEEPLDF030 SLEEPLDF031 SLEEPLDF032 SLEEPLDF033 SLEEPLDF034 SLEEPLDF035 SLEEPLDF036 SLEEPLDF037 SLEEPLDF038 SLEEPLDF039 SLEEPLDF040; do
study_path="/home3/kensinel/fMRI_DATA/SleepLDF"
struc_dir=$study_path/$sub"_unpack/struc/DTI"

cp -i $struc_dir"/dti_FA_$sub.nii.gz" "/home3/kensinel/fMRI_DATA/SleepLDF/DTI/tbss/" 
done

cd "/home3/kensinel/fMRI_DATA/SleepLDF/DTI/tbss/"


tbss_1_preproc *
echo tbss_1_preproc done! 
tbss_2_reg -T
echo tbss_2_reg done!
tbss_3_postreg -S
echo tbss_3_postreg done!
tbss_4_prestats 0.2
echo tbss_4_prestats done!

#randomise -i all_FA_skeletonised -o tbss -m mean_FA_skeleton_mask -d design.mat -t design.con -n 500 --T2 -V

echo ALL DONE


