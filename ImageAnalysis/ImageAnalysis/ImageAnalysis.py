from __future__ import print_function
from PIL import Image

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Open image
im = Image.open("C:/Users/borbs/OneDrive/04_Job Stuff/03_Work Stuff/PERLER_BEAD_MACHINE_00000/test2.jpg")
px = im.load()

# Number of pegs per board
peg_num = 2
logger.info('Image Format: {0}'.format(im.format))
logger.info('Image Size: {0}'.format(im.size))
logger.info('Image Mode: {0}'.format(im.mode))


x_size, y_size = im.size


# Get number of perler boards for each axis
x_boards = x_size / peg_num
logger.info('Peg board rows: {0}'.format(x_boards))
y_boards = y_size / peg_num
logger.info('Peg board columns: {0}'.format(y_boards))

# Get number of spare pegs (non full boards)
x_spare_pegs = x_size % peg_num
logger.info('Spare pegs per row: {0}'.format(x_spare_pegs))

is_x_spare_pegs = x_spare_pegs

if is_x_spare_pegs > 0:
	is_x_spare_pegs = 1

y_spare_pegs = y_size % peg_num
logger.info('Spare pegs per column: {0}'.format(y_spare_pegs))

is_y_spare_pegs = y_spare_pegs

if is_y_spare_pegs > 0:
	is_y_spare_pegs = 1

# Get whole number of boards
x_whole_boards = int(x_boards)
logger.info('Number of x whole boards: {0}'.format(x_whole_boards))
y_whole_boards = int(y_boards)
logger.info('Number of y whole boards: {0}'.format(y_whole_boards))

# Set init box size (top left x, top left y, bottom right x, bottomr right y)
tlx = 0
tly = 0
brx = peg_num 
bry = peg_num 

logger.info('y range: {0}'.format(y_whole_boards + is_y_spare_pegs))
logger.info('x range: {0}'.format(x_whole_boards + is_x_spare_pegs))

# Region dict example
'''
1-1: {
	1-1: (255,255,255),
	1-2: (255,255,255),
	1-2: (255,255,255),
	2-2: (255,255,255)
},
1-2: {
	1-1: (255,0,0),
	1-2: (255,0,0),
	1-2: (255,0,0),
	2-2: (255,0,0)
}
'''
image_val_dict = {
	pegboard_region: {
		pixel: pixel_color
	}
}


count = 0
for rows in range(0, y_whole_boards + is_y_spare_pegs):
	for columns in range(0, x_whole_boards + is_x_spare_pegs):
		box = (tlx, tly, brx, bry)
		logger.info('Box: {0}'.format(box))
		region = im.crop(box)
		region.show()
		tlx += peg_num
		brx +=peg_num 
		count += 1
		logger.info('Count: {0}'.format(count))
		# Reset iteration to left side of image
		if count > x_whole_boards:
			tlx = 0
			tly += peg_num
			brx = 2 
			bry += peg_num
			count = 0

		print(region.getdata())
		#reg_x_size, reg_y_size = region.size
		#logger.info('Region x size: {0}'.format(reg_x_size))
		#logger.info('Region y size: {0}'.format(reg_y_size))

region = im.crop(box)


#region = region.transpose(Image.ROTATE_180)
#im.paste(region, box)

#im.show()