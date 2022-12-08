

import cv2 as cv
import numpy as np
import pyautogui
import time


class FishingAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.fishing_target = cv.imread("/home/frank/Git/wowzer/tutorials/04/fishing/assets/fishing_target.png")
        self.fishing_thread = None

    
    def cast_lure(self):
        print("Casting...")
        pyautogui.press('1')
        time.sleep(2)
        self.find_lure()

    def find_lure(self):
        lure_location = cv.matchTemplate(
            self.main_agent.cur_img, 
            self.fishing_target,
            cv.TM_CCOEFF_NORMED)
        lure_loc_arr = np.array(lure_location)

        cv.imshow("Match Template", lure_loc_arr)
        cv.waitKey(0)

    def move_to_lure(self):
        pass

    def watch_lure(self):
        pass

    def pull_line(self):
        pass


    def run(self):
        while True:
            self.cast_lure()
            time.sleep(5)


if __name__ == "__main__":
    main_agent = None
    fishing_agent = FishingAgent(main_agent=main_agent)
    fishing_agent.run()