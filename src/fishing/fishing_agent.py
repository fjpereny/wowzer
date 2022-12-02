
import cv2
import numpy as np
import pyautogui
import time
from threading import Thread


class FishingAgent:
    def __init__(self, main_agent):
        self.main_agent = main_agent
        self.fishing_target = cv2.imread("fishing/assets/fishing_target.png")
        self.lure_location = None
        self.lure_pixel_box = None
        self.fishing = False
        self.cast_time = None

    def cast_lure(self):
        print("Casting!...")
        self.fishing = True
        self.cast_time = time.time()
        pyautogui.press('1')
        self.find_lure()

    def find_lure(self):
        start_time = time.time()
        while self.lure_location is None:
            self.lure_location = pyautogui.locateOnScreen(self.fishing_target, confidence=0.8)
            if time.time() - start_time > 15:
                print("Warning: Failed to find lure")
                break
        if self.lure_location:
            lure_pixel_box_x0 = self.lure_location[0] - 50
            lure_pixel_box_x1 = self.lure_location[0] + 50
            lure_pixel_box_y0 = self.lure_location[1] - 50
            lure_pixel_box_y1 = self.lure_location[1] + 50
            self.lure_pixel_box = [lure_pixel_box_x0, lure_pixel_box_y0, lure_pixel_box_x1, lure_pixel_box_y1]
            self.move_to_lure()

    def move_to_lure(self):
        if self.lure_location:
            pyautogui.moveTo(self.lure_location[0] + 20, self.lure_location[1] + 10, .45, pyautogui.easeOutQuad)
            self.watch_lure()
        else:
            print("Warning: Attempted to move to lure_location, but lure_location is None (fishing_agent.py line 32)")
            return False

    def watch_lure(self):
        start_time = time.time()
        tol = 0.05    # Percent tolerance
        avg_col = np.average(self.main_agent.cur_img.crop(self.lure_pixel_box))
        cur_avg_col = avg_col
        while (1 - tol) * avg_col < cur_avg_col < (1 + tol) * avg_col:
            cur_avg_col = np.average(self.main_agent.cur_img.crop(self.lure_pixel_box))
            if time.time() - start_time >= 30:
                break
        # self.pull_line()

    def pull_line(self):
        pyautogui.keyDown('shift')
        pyautogui.click(button='right')
        pyautogui.keyUp('shift')

    def run(self):
        while True:
            if self.cast_time is not None and (time.time() - self.cast_time) >= 35:
                self.lure_location = None
                self.lure_pixel_box = None
                self.fishing = False
                self.cast_time = None

            if self.fishing is False:
                self.cast_lure()
