'''
Splits an image up into pegboard sized regions.

.. image:: /images/parse_image.bmp
.. image:: /images/down_arrow.bmp
	:align: center


.. image:: /images/parse_image_demo.bmp

.. todo:: add an image showing what it means to split up a region

.. note:: Any region that is too small for a pegboard will be accounted for, so any size image can be parsed.
'''

from __future__ import print_function

import os
import json
import logging

from PIL import Image

# logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Open image
root_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0].rpartition('\\')[0]
print(root_dir)
image_path = os.path.join(root_dir, 'resources', 'image_dir', 'parse_image.bmp')
print(image_path)

try: 
	im = Image.open(image_path)
	px = im.load()
	peg_num = 6 # Size of pegboard. 2 = 2x2 board, 29 = 29x29, etc...

	logger.info('Image Format: {0}'.format(im.format))
	logger.info('Image Size: {0}'.format(im.size))
	logger.info('Image Mode: {0}'.format(im.mode))

	x_size, y_size = im.size
	logger.info('Width: {0}'.format(x_size))
	logger.info('Height: {0}'.format(y_size))

	# Get number of perler boards for each axis
	x_boards = x_size / peg_num
	y_boards = y_size / peg_num
	logger.info('Peg board rows: {0}'.format(x_boards))
	logger.info('Peg board columns: {0}'.format(y_boards))
	logger.info('Number of x whole boards: {0}'.format(int(x_boards)))
	logger.info('Number of y whole boards: {0}'.format(int(y_boards)))

	# Get number of spare pegs (non full boards)
	x_spare_pegs = x_size % peg_num
	logger.info('Spare pegs per row: {0}'.format(x_spare_pegs))
	is_x_spare_pegs = 0

	if x_spare_pegs > 0:
		is_x_spare_pegs = 1
	y_spare_pegs = y_size % peg_num
	logger.info('Spare pegs per column: {0}'.format(y_spare_pegs))

	is_y_spare_pegs = 0

	if y_spare_pegs > 0:
		is_y_spare_pegs = 1

	# Set init box size (top left x, top left y, bottom right x, bottomr right y)
	tlx = 0
	tly = 0
	brx = peg_num 
	bry = peg_num 


	col_count = 0
	row_count = 0
	do_once = False

	for rows in range(0, int(y_boards) + is_y_spare_pegs):
		for columns in range(0, int(x_boards) + is_x_spare_pegs):

			# Change size of region if iterating on spare peg region
			if col_count == int(x_boards):
				brx = brx - peg_num + x_spare_pegs
				logger.debug('Changed x size')	
			if row_count == int(y_boards) and do_once == False:
				bry = bry - peg_num + y_spare_pegs
				do_once = True # Only change x value once, otherise it will try to save a None image
				logger.debug('Changed y size')	
				logger.debug('Did once')	

			region_id = '{0}-{1}'.format(row_count,col_count)
			logger.info('Region ID: {0}'.format(region_id))	

			box = (tlx, tly, brx, bry)
			logger.info('Box: {0}'.format(box))	
			region = im.crop(box)

			# Save region
			region.save(os.path.join(root_dir, 'resources', 'regions', 'test_{0}.bmp'.format(region_id)))

			# Iterate on x values
			tlx += peg_num
			brx += peg_num 
			col_count += 1
			logger.debug('Column count: {0}'.format(col_count))
			logger.debug('Row count: {0}'.format(row_count))

			# Reset iteration to left side of image
			if col_count > int(x_boards) + is_x_spare_pegs - 1:
				print('resetting')
				tlx = 0
				tly += peg_num
				brx = peg_num
				bry += peg_num
				col_count = 0
				row_count += 1


except:
	logger.warning('No image found. Put a .bmp image in the image_dir')
