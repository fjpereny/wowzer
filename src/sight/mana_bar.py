
import time


def watch_mana(agent):
    while True:
        if agent.cur_img:
            # Mana 75% Detection
            r, g, b = agent.cur_img.getpixel((255, 76))
            if r > 10 or g > 10 or b < 190 or b > 220:
                print("Mana at 75%!")

        time.sleep(1)
