import cv2

img = cv2.imread("PRO-104-Project-Image-main/solar-system.jpg")

cv2.putText(img, "Sun", (5, 300), cv2.FONT_HERSHEY_COMPLEX, 2.5, (253,255,158))
cv2.putText(img, "Mercury", (125, 190), cv2.FONT_HERSHEY_COMPLEX, 0.3, (106,166,255))
cv2.putText(img, "Venus", (185, 260), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,111,255))
cv2.putText(img, "Earth!", (280, 260), cv2.FONT_HERSHEY_COMPLEX, 0.6, (114,255,63))
cv2.putText(img, "Our Moon!", (315, 160), cv2.FONT_HERSHEY_COMPLEX, 0.25, (114,255,63))
cv2.putText(img, "Mars", (382, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (35,35,153))
cv2.putText(img, "Jupiter", (510, 390), cv2.FONT_HERSHEY_COMPLEX, 1.5, (22,93,165))
cv2.putText(img, "Saturn", (745, 350), cv2.FONT_HERSHEY_COMPLEX, 1.2, (190,190,160))
cv2.putText(img, "Uranus", (945, 300), cv2.FONT_HERSHEY_COMPLEX, 0.9, (235,188,126))
cv2.putText(img, "Neptune", (1090, 300), cv2.FONT_HERSHEY_COMPLEX, 0.9, (230,83,38))


cv2.imshow("Solar System", img)
cv2.waitKey(7000)

cv2.imwrite("Solar_systemwithname.jpg",img)
