import cv2
import numpy as np

def sketch(image):
  

# convert the captured image into gray scale image

   grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  
# blurring the image
   blurimg=cv2.GaussianBlur(grayimg,(3,3),0)
  
# extracting edges
   edges=cv2.Canny(blurimg,10,80)
  
#applying threshold
   ret,mimg=cv2.threshold(edges,50,255,cv2.THRESH_BINARY_INV)
   return mimg
# Capturing video from webcam
vid_capt=cv2.VideoCapture(0)
# Capturing the video frame by frame
while True:
   ret,pic_capt=vid_capt.read()
   cv2.imshow('Your Sketch',getmysketch(pic_capt))
   # Key13 is ENTER_KEY
   if cv2.waitKey(1)==13:
   break
# releasing_webcam
vid_capt.release()
# destroying_window
cv2.destroyAllWindows()
