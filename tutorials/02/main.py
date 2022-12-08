

from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread


class MainAgent:
    def __init__(self) -> None:
        self.screenshot = None
        
        print("MainAgent setup complete...")


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
        # print("FPS: " + str(1 / (ex_time)))
        t0 = time.time()


if __name__ == "__main__":
    main_agent = MainAgent()

    update_screen_thread = Thread(
        target=update_screen, 
        args=(),
        name="update screen thread",
        daemon=False)
    update_screen_thread.start()
    print("Thread started")
    
