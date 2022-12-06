

from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time


def update_screen():

    t0 = time.time()
    while True:
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        cv.imshow("Computer Vision", screenshot)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        ex_time = time.time() - t0
        print("FPS: " + str(1 / (ex_time)))
        t0 = time.time()


if __name__ == "__main__":
    update_screen()
