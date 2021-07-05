import cv2

rtmp = "rtmp://192.168.0.104:1935/"

cap = cv2.VideoCapture(rtmp)

while True:
    success, frame = cap.read()

    capGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    capGray = cv2.resize(capGray, (640, 400))
    frame = cv2.resize(frame, (640, 400))

    if success:
        cv2.imshow("Mavic", frame)
        cv2.imshow("Gray Scale", capGray)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        print("Not found")

cap.release()
cv2.destroyAllWindows()
