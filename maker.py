import cv2
import time
count = 1

# Peafowlcas = cv2.CascadeClassifier("classifier/PeafowlV3.1.0.xml")

def num(i):
	i+=1
	return i
cam = cv2.VideoCapture('videos/c7.mp4')
# cam = cv2.VideoCapture(0) #Webcam
name = "Peafowl Auto Capture"

hc = cv2.CascadeClassifier("classifier/PeafowlV3.2.1.xml")
cv2.namedWindow(name, cv2.WINDOW_AUTOSIZE)

while True:
	
	i = 0
	s, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	Peafowl = hc.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in Peafowl:
		# img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		save = img[y:y+h,x:x+w]
		saveGray = cv2.cvtColor(save, cv2.COLOR_BGR2GRAY)
		# filename = 'output/img'+str(x+y)+'.jpg'
		filename = 'output/inrectangle/img'+str(count)+'.jpg'
		cv2.imwrite(filename,saveGray)
		
		# img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		
		
	count=count + 1  
	print("count = "+str(count))
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(name, 1920, 1080)
	cv2.imshow(name, img)


	
	k = cv2.waitKey(10)
	if k == 27:
		cv2.destroyWindow("Detect")
		break


		