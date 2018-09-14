import os

startCount= 13000
statinfo = os.stat('./data/frame'+ str(startCount) +'.jpg')
fileName = 'frame' + str(startCount)
print (fileName + '.jpg size :' + str(statinfo.st_size))