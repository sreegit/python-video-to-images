import cv2
import os
import json
#read file config.json
with open('config.json', 'r') as f:
    configData = json.load(f)

videoNum = configData["videoNumber"]
#provide the video path here
videoPath = configData["dirPath"]

#from which frame/ time the capturing should start
startFrame = configData["startingPoint"]

dirName = 'data'
dirVidNum = dirName+str(videoNum)

####config video prefix is given here
videoFileName = configData["videoNamePrefix"]+str(videoNum) +'.mp4'

inputVideo = videoPath+videoFileName
print("video path set... ", inputVideo)
cap = cv2.VideoCapture(inputVideo)
print('video capturing... ')
try:
    if not os.path.exists( dirVidNum ):
        os.makedirs( dirVidNum )
except OSError:
    print ("Error: Creating the directory!")

def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    print("setting the Seconds...")
    hasFrames, frame = cap.read()
    print("reading video hasFrames... ")
    #if ret:
    name = './'+ dirVidNum +'/v'+str(videoNum)+'_' + str(sec) + '.jpg'
    print ('Creating... ' + name)
    if hasFrames:
        print('going to Write..')
        cv2.imwrite(name, frame)
        print('writing Done JPG...')
    return hasFrames
sec = 0
frameRate = 1

sec = sec+ startFrame
success = getFrame(sec)
while success:
    sec = sec + frameRate
    #stopping the execution if the seconds exceeds 600 (max 600 images only)
    if sec > 600 :
        break
    sec = round(sec, 2)
    success = getFrame(sec)

# When everything done, release the capture
cap.release()
# cv2.destroyAllWindows()