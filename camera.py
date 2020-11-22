import numpy as np
import cv2
import time


def record():
    final = time.time() + 10

    capture = cv2.VideoCapture(0)

    W = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*"mp4v")

    output = cv2.VideoWriter('output.mp4', codec, 20.0, (W, H))


    while True:
        ret, frame= capture.read()

        output.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & (time.time() >= final):
            break


    capture.release()
    output.release()
    cv2.destroyAllWindows()
