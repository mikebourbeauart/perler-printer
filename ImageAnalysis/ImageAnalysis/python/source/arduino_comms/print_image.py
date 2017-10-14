'''
color to use and where to put it 
'''

import os
import logging
import json
from collections import OrderedDict

import serial

# logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)



root_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0].rpartition('\\')[0]
json_file_path = os.path.join(root_dir, 'resources', 'json_data', 'region_data.json')

connected = False
ser = serial.Serial('com4',9600) #Create Serial port object called arduinoSerialData
 
while not connected:
	serin = ser.read()
	connected = True
	print 'Arduino connected'


'''Reads and returns data from external JSON file

@param mDataDir:  str, path of the info folder
@param mTaskName: str, task name

@returns: prep_data dictionary
'''
json_file_path = os.path.join(
	root_dir, 'resources', 'json_data', 'region_data.json'
)

logger.info('JSON path : "%s"' % json_file_path)

try:
	with open(json_file_path, 'r') as handle:
		json_data = json.load(handle, object_pairs_hook=OrderedDict) # Opens dict in order

except:
	logger.warning('No region data found. Run image_split then region_parse to create region data')

#for key, val in json_data.iteritems():
#print(key)
#print(val)
region_count = 0
for key in json_data.iteritems():

	region = list(json_data.keys())[region_count]
	print 'region {0}'.format(region)
	pixel_count = 0
	pixel_data = json_data[region]
	for pos, color in pixel_data.iteritems():
		
		# Send pixel pos data to printer
		ser.write('1')

		print 'pixel {0}'.format(pos)
		print 'color {0}'.format(color)

		inChar = ser.read()
		print 'serial {0}'.format(inChar)

		# Wait for response that bead has been dropped
		while ser.read() != '0':
			ser.read()
		
		# Go to home location and pick up new bead
		pixel_count += 1
	region_count += 1



#ser.write(key)
'''
if (arduinoSerialData.inWaiting()>0):
	myData = arduinoSerialData.readline()
	print myData
'''