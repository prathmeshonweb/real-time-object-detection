import cv2
# Open the device at the ID 0

cap = cv2.VideoCapture(0)

#Check whether user selected camera is opened successfully.


#To set the resolution

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while(True):

# Capture frame-by-frame

ret, frame = cap.read()

# Display the resulting frame

cv2.imshow(‘preview’,frame)

#Waits for a user input to quit the application

if cv2.waitKey(1) & 0xFF == ord(‘q’):

break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()