import cv2                              # load OpenCV

WEB_CAM_IDX = 0                         # default webcam index
cam = cv2.VideoCapture(WEB_CAM_IDX)     # webcam as variable

while cam.isOpened():                   # loop while webcam is open
    status, frame = cam.read()          # read frame from webcam
    if not status:                      # if frame is not read
        break                           # exit loop
    cv2.imshow('Webcam', frame)         # display current frame
    if cv2.waitKey(1) == ord('q'):      # wait for 'q' key (1ms delay)
        break
cam.release()                           # release webcam
cv2.destroyAllWindows()                  # close all windows