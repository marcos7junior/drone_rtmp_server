# imports
import cv2

# rtmp://IP:PORTA/
rtmp = "rtmp://0.0.0.0:1935/"

# captura o vídeo transmitido via RTMP
cap = cv2.VideoCapture(rtmp)

while True:
    # recebe um valor lógico(success) e uma matriz com os frames
    success, frame = cap.read()
    
    # converte para escala cinza
    capGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # redimensiona ambas as janelas
    capGray = cv2.resize(capGray, (640, 400))
    frame = cv2.resize(frame, (640, 400))

    if success:
        # se o valor lógico for verdadeiro irá mostrar os 
        # frames até a tecla 'ESC' for presionada
        cv2.imshow("Mavic", frame)
        cv2.imshow("Gray Scale", capGray)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        print("Not found")

cap.release()
cv2.destroyAllWindows()
