import cv2

videoCapture = cv2.VideoCapture('C:\Users\Desktop02\Documents\OpenCV_pythonFiles\chapter2\MyCamOutputVid.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
print fps
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
print size
videoWriter = cv2.VideoWriter( 'C:\Users\Desktop02\Documents\OpenCV_pythonFiles\chapter2\MyOutputVid.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), fps, size)

success, frame = videoCapture.read()
while success: # Loop until there are no more frames.
	videoWriter.write(frame)
	success, frame = videoCapture.read()