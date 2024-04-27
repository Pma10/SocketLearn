import network.common as com
from network.client import *
from threading import Thread
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def send(c):
    while True:
        if cv2.waitKey(33) >= 0:
            break
        ret, frame = capture.read()
        c.send(com.image_pack(frame))


c = Client(host="127.0.0.1", port=9998)
th = Thread(target=send, args=(c,))
th.start()
th.join()
capture.release()
cv2.destroyAllWindows()
