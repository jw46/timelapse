import cv2
import time

def get_sequence(i):
    s = str(i)
    if len(s) == 1:
        return '0' + s
    else:
        return s

camera = cv2.VideoCapture("/dev/video2")
i = 0
while i < 60:
    return_value, image = camera.read()
    cv2.imwrite(f'/home/jon/temp/capture/image{get_sequence(i)}.png', image)
    time.sleep(20)
    i += 1
del(camera)