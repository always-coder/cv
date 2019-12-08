import cv2

image = cv2.imread("./image.png")
cv2.namedWindow("input_image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input_image", image)
cv2.waitKey(0)
cv2.destoryAllWindows()
