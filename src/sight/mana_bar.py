
import time


def watch_mana(agent):
    while True:
        if agent.cur_img:
            # Mana 75% Detection
            r, g, b = agent.cur_img.getpixel((255, 76))
            if r != 0 or g != 0 or b != 200:
                print("Mana at 75%!")

        time.sleep(1)
