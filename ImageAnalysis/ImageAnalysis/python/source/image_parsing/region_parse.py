'''
Parses regions

.. todo:: add an image showing what it means to parse a region

'''


from __future__ import print_function

import os
import json
import logging
from collections import OrderedDict

from PIL import Image

# logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

regions_dir = "C:/Users/borbs/OneDrive/04_Job Stuff/03_Work Stuff/PERLER_BEAD_MACHINE_00000/regions"

json_file = "C:/Users/borbs/OneDrive/04_Job Stuff/03_Work Stuff/PERLER_BEAD_MACHINE_00000/test2_data.json"

json_data = OrderedDict()

for im_file in os.listdir(regions_dir):
	#im_file = 'test_0-3.bmp'
	# Open image
	#im_file = "C:/Users/borbs/OneDrive/04_Job Stuff/03_Work Stuff/PERLER_BEAD_MACHINE_00000/regions/test_0-0.bmp"
	im = Image.open(os.path.join(regions_dir,im_file))
	px = im.load()

	region_num = im_file.rpartition(".")[0].rpartition("_")[2]
	logger.info('Region num: {0}'.format(region_num))

	logger.info('Image Format: {0}'.format(im.format))
	logger.info('Image Size: {0}'.format(im.size))
	logger.info('Image Mode: {0}'.format(im.mode))

	x_size, y_size = im.size
	logger.info('Width: {0}'.format(x_size))
	logger.info('Height: {0}'.format(y_size))

	json_data[region_num] = {}

	for y in range(0, int(y_size)):
		for x in range(0, int(x_size)):
			logger.debug('x coord: {0}'.format(x))
			logger.debug('y coord: {0}'.format(y))
			logger.debug('pixel value: {0}'.format(px[x,y]))

			json_data[region_num]['{0}-{1}'.format(y,x)] = px[x,y] 

with open(json_file, "w") as outfile:
	json.dump(json_data, outfile, sort_keys=True, 
	indent=4, separators=(',', ': ')
)

# Region dict example

'''
regions : {
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
}
'''

