import cv2
import numpy as np
from tqdm import tqdm

cap = cv2.VideoCapture('Friends.mkv') #INPUT FILE
framecount=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(framecount)
print(cap.isOpened())

jump=20; #Cannot take all frames (too long), so we skip frames

ret, frame = cap.read()
w = frame.shape[0]
h = frame.shape[1]
d = frame.shape[2]

frame1=np.zeros((w,h,d), dtype=frame.dtype)
frame2 = np.zeros((w,int(framecount/jump)+1, d), dtype=frame.dtype)
j=0

for i in tqdm(range (0,framecount,jump)):
	cap.set(1, i)
	ret, frame1=cap.read()
	frame2[:,j,1]=np.mean(frame1[:,:,1])
	frame2[:,j,2]=np.mean(frame1[:,:,2])
	frame2[:,j,0]=np.mean(frame1[:,:,0])
	j+=1
	
cv2.imshow('image', frame2)
cv2.imwrite('Friends.png',frame2) #OUTPUT FILE
cv2.waitKey(0)	