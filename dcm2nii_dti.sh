#!/usr/bin/env bash

#usage ./dcm2nii_dti.sh <subject> <dti scan>
sub=$1

#for sub in SLEEPLDF; do
study_path="/home3/kensinel/fMRI_DATA/SleepLDF"
struc_dir=$study_path/$sub"_unpack/struc/DTI"
echo $struc_dir
mkdir $study_path/$sub"_unpack/struc/DTI"

dicom_folder=$study_path/$sub"_unpack/raw/*_"${sub}"_*/INVESTIGATORS_KENSINGER*/DIFF_1P8MM_SMS2_P2_2BX60_00*/"
echo $dicom_folder

#move into encoding folder. this is important for changing the files names
cd $dicom_folder

#variable that defines list of individual dicoms
dti_dcm=$dicom_folder"/*_"${sub}"*.IMA"
echo $dti_dcm
#file is a counter variable that is used to rename files
file=1
file_name=$(basename "$dti_dcm")
#echo $file_name
#dcm2nii has a character limit so this loop shortens the file names to s####.IMA
for var in $file_name
do	
	mv $var `printf "s"%04d.IMA $file`
	file=$((file + 1))
done

dti_short=$dicom_folder"/*.IMA"

#echo $dti_short
dcm2nii -o $struc_dir/ $dti_short

mv $struc_dir/*".bval" $struc_dir"/bvals"

mv $struc_dir/*".bvec" $struc_dir"/bvecs"

mv $struc_dir/*".nii.gz" $struc_dir"/nodif.nii.gz"
#done




