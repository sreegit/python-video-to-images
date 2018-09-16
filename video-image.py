import cv2
import os
#provide the video number here
videoNum = 23
#provide the video path here
videoPath = '/media/sks/All-Data/Camera-Hik-All/09122018-Sep/'
####make necessary changes whenver there is a change in the video number (eg. from 9 to 10)
videoFileName = 'hiv000'+str(videoNum) +'.mp4'
inputVideo = videoPath+videoFileName
cap = cv2.VideoCapture(inputVideo)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ("Error: Creating the directory!")

def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, frame = cap.read()
    #if ret:
    name = './data/v'+str(videoNum)+'_image' + str(sec) + '.jpg'
    print ('Creating... ' + name)
    if hasFrames:
        cv2.imwrite(name, frame)
    return hasFrames
sec = 0
frameRate = 1

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
cv2.destroyAllWindows()