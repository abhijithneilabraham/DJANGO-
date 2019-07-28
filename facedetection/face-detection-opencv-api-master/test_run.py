import cv2, requests
url = "http://localhost:8000/face_detection/detect/"
##### image 1 #####
image_to_read = cv2.imread("image5.jpg")
tracker = {"url": "https://image.ibb.co/cPrdgS/image5.jpg"}
req = requests.post(url, data=tracker).json()

for (w,x,y,z) in req["faces"]:
    cv2.rectangle(image_to_read,(w,x), (y,z), (0, 255, 0), 2)

cv2.imshow("image1.jpg", image_to_read)
cv2.waitKey(0)
