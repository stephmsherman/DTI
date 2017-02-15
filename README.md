#Diffusion Tensor Imaging Scripts

Protocol for DTI analyses on SLEEPLDF project
This protocol starts with preprocessing the dicoms and ends with statistical analyses to examine whether a covariate is (postively or negatively) associated with white matter integrity (Fractional Anisotropy, FA)

- Steps 1-3 are single subject steps and steps 4-9 are run on the entire group</b>
- Currently this protocol is only for covariate analyses looking at contrast 0 1 and 0 -1.

1. cd into the folder where all the scripts live

2. Run: ./dcm2nii_dti.sh <subject> (i.e. ./dcm2nii_dti.sh SLEEPLDF001). This script finds the DTI dicom data based on the folder name. The names of the .iMA (dicoms) are shortened because the file names are too long to run dcm2nii. The .nii.gz files are moved to each subjects struc/DTI folder along with the bvec and bval files

3. Run: ./DTI_preprocessing.sh <subject> (i.e. ./DTI_preprocessing.sh SLEEPLDF001). This script does the eddy current correction and runs DTI fit to create the FA map for that subject

**Next steps completed after all subjects have FA maps

4. Run: ./DTI_tbss.sh. Make sure to add the subjects to the loop. The goal of this step is to have TBSS processed FA maps for each subject so the following analyses can be completed on those processed maps

5. QA check, Run: python combined_slicedir.py to create a combined image of the FA maps for all participants to check the quality

6. Secure copy all_data_<date>.csv from the brain510 to get covariate data for analyses. Outside of pleiades on a computer connected to the brain50 run: scp path/all_data_<date>.csv <bcusername>@pleiades.bc.edu:path/combined_data/ 

7. Run: python prep_covariate_design_matrix.py. This script will prompt you to enter the name of the covariate you are interested in analyzing. Type the covariate name exactly how it appears as a column name in the all_data_<date>.csv file (i.e. meq_score). This covariate can only be a numeric column. The script will format the covariate data to the design_<covariate>.mat file and create a new tbss_<covariate> folder with only subject FA files that have a measurement for the covariate in the FA folder. This script also creates a stats folder that include the design matrix and contrast files.

8. Run: ./TBSS_covariate.sh <covariate> (i.e. ./TBSS_covariate.sh meq_score). This script runs the last two steps of TBSS to combine all the FA maps from the participants with complete data and runs randomise.

9. Time to look at the results! Within the stats folder of the tbss_<covariate> folder run fslview $FSLDIR/data/standard/MNI152_T1_1mm.nii.gz mean_FA_skeleton.nii.gz -l Green -b 0.2,0.7 tbss_tfce_corrp_tstat1.nii.gz -l Red-Yellow -b 0.95,1 Change the tbss*.nii.gz to look at the other contrast analyses. tfce files are Threshold-Free Cluster Enhancement.

