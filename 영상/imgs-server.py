import cv2

import network.common as com
from network.server import *


def handler(client, addr, kwargs):
    data_buffer = b''
    while True:
        if cv2.waitKey(33) < 0:
            frame, data_buffer = com.image_unpack(client, data_buffer)
            cv2.imshow("server", frame)


s = Server(port=9998)

s.run(fun=handler)
