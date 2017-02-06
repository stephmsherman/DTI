#!/usr/bin/env bash

for sub in SLEEPLDF001 SLEEPLDF002 SLEEPLDF003 SLEEPLDF004; do
study_path="/home3/kensinel/fMRI_DATA/SleepLDF"
struc_dir=$study_path/$sub"_unpack/struc/DTI"

fslroi $struc_dir"/nodif.nii.gz" $struc_dir"/b0.nii.gz" 0 1
bet $struc_dir"/b0.nii.gz" $struc_dir"/b0_brain.nii.gz" -m -f .2

eddy_correct $struc_dir"/nodif.nii.gz" $struc_dir"/ecc.nii.gz" 0

dtifit -k $struc_dir"/ecc.nii.gz" -o $struc_dir"/dti" -m $struc_dir"/b0_brain_mask.nii.gz" -r $struc_dir"/bvecs" -b $struc_dir"/bvals"

mv $struc_dir"/dti_FA.nii.gz" $struc_dir"/dti_FA_$sub.nii.gz"
echo DONE with $sub
done


