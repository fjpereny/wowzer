

from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread
from fishing.fishing_agent import FishingAgent


class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.fishing_thread = None

        self.cur_img = None     # BGR Image
        self.cur_imgHSV = None  # HSV Image

        self.zone = "Feralas"
        self.time = "night"
        
        # print("MainAgent setup complete...")


def update_screen(agent):

    t0 = time.time()
    fps_report_delay = 5
    fps_report_time = time.time()
    while True:
        agent.cur_img = ImageGrab.grab()
        agent.cur_img = np.array(agent.cur_img)
        agent.cur_img = cv.cvtColor(agent.cur_img, cv.COLOR_RGB2BGR)
        agent.cur_imgHSV = cv.cvtColor(agent.cur_img,cv.COLOR_BGR2HSV)

        # cv.imshow("Computer Vision", agent.cur_img)
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        ex_time = time.time() - t0
        if time.time() - fps_report_time >= fps_report_delay:
            print("FPS: " + str(1 / (ex_time)))
            fps_report_time = time.time()
        t0 = time.time()
        time.sleep(0.005)


def print_menu():
    print("Enter a command:")
    print("\tS\tStart the main agent.")
    print("\tZ\tSet zone.")
    print("\tF\tStart the fishing agent.")
    print("\tQ\tQuit wowzer.")


if __name__ == "__main__":
    main_agent = MainAgent()

    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == "s":
            update_screen_thread = Thread(
            target=update_screen, 
            args=(main_agent,),
            name="update screen thread",
            daemon=True)
            update_screen_thread.start()
            print("Thread started")

        elif user_input =='z':
            pass

        elif user_input == 'f':
            fishing_agent = FishingAgent(main_agent)
            fishing_agent.run()

        elif user_input == 'q':
            cv.destroyAllWindows()
            break

        else:
            print("Input error.")
            print_menu()

    print("Done.")


 
