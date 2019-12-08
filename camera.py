import cv2
import numpy

capture = cv2.VideoCapture(0)

while 1:
    ret, frame = capture.read()
    cv2.imshow("capture", frame)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break;

capture.release()
cv2.destroyAllWindows()
