import cv2
import time
red_lower = (0, 150 ,150)
red_upper = (15, 255, 255)
green_lower = (50, 80, 80)
green_upper = (80, 255, 255)


webcam_video = cv2.VideoCapture(0)

while True:

    ret, frame = webcam_video.read()


    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    if cv2.countNonZero(red_mask) > cv2.countNonZero(green_mask):
        print("Traffic light is RED, Giving Signal...")
        time.sleep(0.5)
    if cv2.countNonZero(green_mask) > cv2.countNonZero(red_mask):    
        print("Traffic light is GREEN, Giving Signal...")
        time.sleep(0.5)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)        
    cv2.imshow("Traffic Light Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

webcam_video.release()
cv2.destroyAllWindows()
