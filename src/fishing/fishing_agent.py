
import cv2 as cv
import numpy as np
import pyautogui
import time
from threading import Thread
import os


class FishingAgent:
    def __init__(self, main_agent):
        self.main_agent = main_agent
        
        # interpolate here_path to get the path to the fishing target image
        here_path = os.path.dirname(os.path.realpath(__file__))
        self.fishing_target = cv.imread(
            os.path.join(
                here_path,
                "assets", "fishing_target.png"
            )
        )
        
        self.fishing_thread = None

    def cast_lure(self):
        print("Casting!...")
        self.fishing = True
        self.cast_time = time.time()
        pyautogui.press('1')
        time.sleep(3)
        self.find_lure()

    def find_lure(self):
        start_time = time.time()
        lure_location = cv.matchTemplate(self.main_agent.cur_img, self.fishing_target, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(lure_location)
        self.lure_location = max_loc
        self.move_to_lure()

    def move_to_lure(self):
        if self.lure_location:
            pyautogui.moveTo(self.lure_location[0] + 25, self.lure_location[1], .45, pyautogui.easeOutQuad)
            self.watch_lure()
        else:
            print("Warning: Attempted to move to lure_location, but lure_location is None (fishing_agent.py line 32)")
            return False

    def watch_lure(self):
        time_start = time.time()
        while True:
            pixel = self.main_agent.cur_imgHSV[self.lure_location[1] + 25][self.lure_location[0]]            
            if self.main_agent.zone == "Dustwallow":
                if pixel[0] >= 20 or pixel[1] < 60 or pixel[2] < 40 or time.time() - time_start >= 30:
                    print("Bite detected!")
                    break
            elif self.main_agent.zone == "Feralas" and self.main_agent.time == "night":
                if pixel[0] >= 70:
                    print("Bite detected!")
                    break
                if time.time() - time_start >= 30:
                    print("Fishing timeout!")
                    break
            elif self.main_agent.zone == "Feralas":
                print("Feralas")
                if pixel[0] >= 60 or time.time() - time_start >= 30:
                    print("Bite detected!")
                    break
            print(pixel)
        self.pull_line()

    def pull_line(self):
        os.system("sh -c 'xdotool keydown Shift_L; sleep 0.1; xdotool mousedown 3; sleep 0.1; xdotool mouseup 3; sleep 0.1; xdotool keyup Shift_L; sleep 0.1'")
        time.sleep(3)
        self.run()

    def run(self):
        if self.main_agent.cur_img is None:
            print("Image capture not found!  Did you start the screen capture thread?")
            return
        print("Starting fishing thread in 10 seconds...")
        time.sleep(10)
        
        print("Switching to fishing hotbar (hotbar 6)")
        pyautogui.keyDown('shift')
        pyautogui.press('6')
        pyautogui.keyUp('shift')
        time.sleep(1)
        
        self.fishing_thread = Thread(
            target=self.cast_lure, 
            args=(),
            name="fishing thread",
            daemon=True)    
        self.fishing_thread.start()
