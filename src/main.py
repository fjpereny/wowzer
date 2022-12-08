
from PIL import Image, ImageGrab
import time
from threading import Thread
import wowzer
from Xlib import display, X
import numpy as np
import cv2 as cv    

import sight.mana_bar as mana_bar
import fishing.fishing_agent as fishing_agent


FPS_REPORT_DELAY = 3


class MainAgent:
    def __init__(self):
        self.agents = []
        self.fishing_thread = None

        self.cur_img = None
        self.cur_imgHSV = None

        self.zone = "Feralas"
        self.time = "day"


def update_screen(agent):
    print("Starting computer vision screen update...")
    dsp = display.Display()
    screen = dsp.screen()
    width = screen.width_in_pixels
    height = screen.height_in_pixels
    print("Detected display resolution: " + str(width) + " x " + str(height))


    loop_time = time.time()
    fps_print_time = time.time()
    while True:
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        screenshotHSV = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        agent.cur_img = screenshot
        agent.cur_imgHSV = screenshotHSV

        cur_time = time.time()
        if cur_time - fps_print_time >= FPS_REPORT_DELAY:
            print('FPS: {}'.format(1 / (cur_time - loop_time)))
            fps_print_time = cur_time
        loop_time = cur_time
        cv.waitKey(1)

def print_menu():
    print('Enter a command:')
    print('\tS\tStart main AI agent screen capture.')
    print('\tZ\tSet zone')
    print('\tF\tStart fishing.')
    print('\tQ\tQuit wowzer.')

def run():
    main_agent = MainAgent()

    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == 's':
            update_screen_thread = Thread(
                target=update_screen, 
                args=(main_agent,), 
                name="update screen thread",
                daemon=True)
            update_screen_thread.start()

        elif user_input == 'f':        
            agent = fishing_agent.FishingAgent(main_agent)
            agent.run()

        elif user_input == 'z':
            print('Enter zone name:')
            print('\tOptions:')
            print('\t\tDustwallow')
            print('\t\tFeralas')
            main_agent.zone = input().title().strip()

        elif user_input == 'q':
            print("Shutting down wowzer.")
            break       
        
        else:
            print("Invalid entry.")
            print_menu()

    print("Done.")
    
if __name__ == '__main__':
    wowzer.run()
