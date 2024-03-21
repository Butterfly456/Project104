import cv2
cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Mercury", (50,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Venus", (80,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Earth", (110,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Mars", (140,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Jupiter", (160,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Saturn", (180,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Uranus", (200,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.putText(img, "Neptune", (220,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),)

cv2.imshow("output", img)


cv2.waitKey(0)

cv2.imwrite(“Solar_systemwithname.jpg”,img)
