import cv2
import numpy as np
planets = cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\OIP.jpeg")
gray = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
#cimg = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)  *** not work
#cv2.imshow("ccir",cimg)
img = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,
 param1=150,param2=28,minRadius=0,
 maxRadius=0)#circles: A vector that stores sets of 3 values: xc,yc,r for each detected circle
#print(circles)
##HOUGH_GRADIENT: Define the detection method. Currently this is the only one available in OpenCV.
##dp = 1: The inverse ratio of resolution.
##min_dist = gray.rows/16: Minimum distance between detected centers.
##param_1 = 200: Upper threshold for the internal Canny edge detector.
##param_2 = 100*: Threshold for center detection.
##min_radius = 0: Minimum radius to be detected. If unknown, put zero as default.
##max_radius = 0: Maximum radius to be detected. If unknown, put zero as default
if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # draw center
            cv2.circle(planets, center, 1, (0, 255,0), 1)#img,center,radius,colour,thickness
            # circle outline
            radius = i[2]
            cv2.circle(planets, center, radius, (255, 0, 0), 1)
cv2.imshow("cir",planets)
cv2.waitKey()
cv2.destroyAllWindows()
