import os

def removeFile(filePathName):
	print ("removing file: " + filePathName)
	try:
		os.remove(filePathName)
	except OSError:
		pass

def checkFileSize(startCount):
	filePathName = './data/frame'+ str(startCount) +'.jpg'
	try:
		statinfo = os.stat(filePathName)
		print (filePathName+ ' size :' + str(statinfo.st_size))
		if statinfo.st_size < 5:
			print("remove file")
			removeFile(filePathName)
			return 1
		else:
			print ('valid file')
			return 0
	except OSError:
		print ("Err: file not found")
		return 0
		pass
	

def init():
	print("Calling file size...")
	startCount = 13001
	endCount = 15001

	removeCount = 0
	for x in range(startCount, endCount+1):
		count = checkFileSize(x)	
		removeCount = removeCount + count

	print(removeCount)

##init()




from os import listdir
from os.path import isfile, join
from time import sleep

def listFiles():
	videoPath = '/media/sks/All-Data/Camera-Hik-All/09122018-Sep'
	onlyfiles = [f for f in listdir(videoPath) if isfile(join(videoPath, f))]
	print (len(onlyfiles))

	i = 0
	for x in onlyfiles:
		print (x)
		sleep(0.3)
		i += 1
		print (i)

#listFiles()


#### create directories in loop

import os

def createDirectories():
	for i in range(0, 5):
		try:
		    if not os.path.exists('data'+str(i)):
		        os.makedirs('data'+str(i))
		        print("created dir : "+str(i) )
		except OSError:
		    print ("Error: Creating the directory!")

#createDirectories()

### read file config
import json

def readFile():
	with open('config.json', 'r') as f:
		distros_dict = json.load(f)

	# for distro in distros_dict:
	#     print(distro['dirPath'])

	print(distros_dict["videoNumber"])

#readFile()


import cv2

def allFrames():
	vidcap = cv2.VideoCapture('/media/sks/All-Data/Camera-Hik-All/09122018-Sep/hiv00037.mp4')

	# frameRate = vidcap.get(5)
	# print(frameRate)

	# frameId = vidcap.get(1)

	# print(frameId)
	sec = 1
	print("going to calcuate Sec.. ")
	vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*5000)
	print("calc done..")
	success,image = vidcap.read()
	count = 0
	while success:
	  cv2.imwrite("./data/frame%d.jpg" % count, image)     # save frame as JPEG file   

	  vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*5000)   
	  success,image = vidcap.read()
	  print('Read a new frame: ', success, count)
	  count += 1
	  sec += 1

allFrames()