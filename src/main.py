
from PIL import Image, ImageGrab
import time
from threading import Thread
import wowzer
from Xlib import display, X
import numpy as np
import cv2 as cv

import sight.mana_bar as mana_bar
import fishing.fishing_agent as fishing_agent


class MainAgent:
    def __init__(self):
        self.cur_img = None
        self.cur_imgHSV = None


def update_screen(agent):
    print("Starting computer vision screen update...")
    dsp = display.Display()
    screen = dsp.screen()
    root = screen.root
    width = screen.width_in_pixels
    height = screen.height_in_pixels
    print("Detected display resolution: " + str(width) + " x " + str(height))

    loop_time = time.time()
    show_fps = False

    while True:
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        screenshotHSV = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        agent.cur_img = screenshot
        agent.cur_imgHSV = screenshotHSV

        # cv_scale = 0.35
        # comp_vision = cv.resize(screenshot, (0, 0), fx=cv_scale, fy=cv_scale)
        # cv.imshow("Computer Vision", comp_vision)
        # print('FPS: {}'.format(1 / (time.time() - loop_time)))
        loop_time = time.time()
        cv.waitKey(1)


def run():
    main_agent = MainAgent()
    update_screen_thread = Thread(target=update_screen, args=(main_agent,), name="update screen thread")
    update_screen_thread.start()

    # mana_bar_thread = Thread(target=mana_bar.watch_mana, args=(main_agent,), name="mana bar")
    # mana_bar_thread.start()

    fishing_agent_thread = fishing_agent.FishingAgent(main_agent)
    time.sleep(5)
    fishing_agent_thread.run()


if __name__ == '__main__':
    wowzer.run()
