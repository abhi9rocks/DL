
import cv2
 
vc = cv2.VideoCapture(r'test.mp4') #read into the video file
c = 1
 
if vc.isOpened():
   rval, frame = vc.read()
else:
   rval = False
 
timeF =1.5 #time frame interval 
 
while rval:
   rval, frame = vc.read()
   if (c % timeF == 0):
      cv2.imencode('.jpg', frame)[1].tofile(r'image/' + str(c) + '.jpg')  #save image
   c = c + 1
   cv2.waitKey(1)
 
 
vc.release()