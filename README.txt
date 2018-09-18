//////////README//////////////

Files used
1. video-image.py - the python script file
2. config.json


////2. config.json

How to give video numbers? (videoNumber)

	Examples: videoNumber: 008, videoNuber: 031, videoNumber 100 

	startingPoint - the minute from which the video frames should be captured. Eg. 5 (means from the 5th minute onwards the capturing starts)

	dirPath - provide the complete path to the directory where the videos are kept

	videoNamePrefix - provide the prefix of the vidow. Eg. hiv00


Observations:
	It is found that, the computer heats up and takes time when the number of frames increases in a video. Therefore it may be better to process one video at a time.