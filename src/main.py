1
from PIL import Image
import time
from threading import Thread
import wowzer
from Xlib import display, X

import sight.mana_bar as mana_bar
import fishing.fishing_agent as fishing_agent


class MainAgent:
    def __init__(self):
        self.cur_img = None


def update_screen(agent):
    print("Starting computer vision screen update...")
    dsp = display.Display()
    screen = dsp.screen()
    root = screen.root
    width = screen.width_in_pixels
    height = screen.height_in_pixels
    print("Detected display resolution: " + str(width) + " x " + str(height))
    while True:
        raw = root.get_image(0, 0, width, height, X.ZPixmap, 0xffffff)
        agent.cur_img = Image.frombytes("RGB", (width, height), raw.data, "raw", "BGRX")
        print("update")
        time.sleep(0.01)


def run():
    main_agent = MainAgent()
    update_screen_thread = Thread(target=update_screen, args=(main_agent,), name="update screen thread")
    update_screen_thread.start()

    mana_bar_thread = Thread(target=mana_bar.watch_mana, args=(main_agent,), name="mana bar")
    mana_bar_thread.start()

    fishing_agent_thread = fishing_agent.FishingAgent(main_agent)
    time.sleep(5)
    fishing_agent_thread.run()


if __name__ == '__main__':
    wowzer.run()
