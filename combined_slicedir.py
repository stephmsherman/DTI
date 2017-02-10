##purpose of the script is to look at a combined png files of all the FA maps
#for each subject
import sys
import os
from PIL import Image
import glob

##change directories to where images live
os.chdir('/home3/kensinel/fMRI_DATA/SleepLDF/DTI/all_tbss/FA/slicesdir')
pngs = sorted(glob.glob('dti_FA_SLEEPLDF0*_FA.png'))

##list of images an attributes

images = map(Image.open, pngs)

##get vectors of all the widths and heights
widths, heights = zip(*(i.size for i in images))

##want each new image to be a new row so taking the sum of the heights to create the
#dimensions of the new image
total_height = sum(heights)
max_width = max(widths)

##actually create the new image with the dimensions 
new_im = Image.new('RGB', (max_width, total_height))

y_offset = 0
for im in images:
	new_im.paste(im, (0,y_offset))
	y_offset += im.size[1] ##allows me to change one axis

new_im.save('all.png')
