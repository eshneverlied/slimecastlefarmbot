import cv2
import numpy as np
import pyautogui
import time
from PIL import Image
import os
from config import x,y,width,height
region = (x, y, width, height)

# загрузка шаблонов
def load_templates():
    return {
        "bonus": cv2.imread("templates/bonus_button.png", cv2.IMREAD_COLOR),
        "get_bonus": cv2.imread("templates/get_bonus_button.png", cv2.IMREAD_COLOR),
        "start1": cv2.imread("templates/start_button.png", cv2.IMREAD_COLOR),
        "start2": cv2.imread("templates/start_button_2.png", cv2.IMREAD_COLOR),
        "end_reward": cv2.imread("templates/end_reward_button.png", cv2.IMREAD_COLOR),
        "treasure_tile": cv2.imread("templates/treasure_tile.png", cv2.IMREAD_COLOR),
        "get_treasure_button": cv2.imread("templates/get_treasure_button.png", cv2.IMREAD_COLOR),

    }


def take_screenshot():
    s = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(s), cv2.COLOR_RGB2BGR)

def find_and_click(template, screenshot, threshold=0.85):
    if template is None:
        return False
    if template.shape[2] == 4:
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
    if screenshot.shape[2] == 4:
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    if screenshot.shape[0] < template.shape[0] or screenshot.shape[1] < template.shape[1]:
        return False

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        h, w = template.shape[:2]
        pyautogui.click(x + max_loc[0] + w // 2, y + max_loc[1] + h // 2)
        time.sleep(1)
        return True
    return False

def find_and_click_best(template, screenshot, threshold=0.85):
    if template is None:
        return False
    if template.shape[2] == 4:
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
    if screenshot.shape[2] == 4:
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    if screenshot.shape[0] < template.shape[0] or screenshot.shape[1] < template.shape[1]:
        return False

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):
        h, w = template.shape[:2]
        b, g, r = screenshot[pt[1] + 2, pt[0] + 2]
        if 170 < r < 200 and 170 < g < 200 and 170 < b < 200:
            continue  # серый
        pyautogui.click(x + pt[0] + w // 2, y + pt[1] + h // 2)
        time.sleep(1)
        return True

    return False

# 🔁 Основной цикл
templates = load_templates()

while True:
    screen = take_screenshot()
    clicked = False

    if find_and_click(templates["bonus"], screen):
        time.sleep(1.5)
        screen = take_screenshot()
        find_and_click(templates["get_bonus"], screen)
        clicked = True

    if not clicked:
        if find_and_click(templates["start2"], screen):
            clicked = True
        elif find_and_click(templates["start1"], screen):
            clicked = True
        elif find_and_click(templates["end_reward"], screen):
            clicked = True
        elif find_and_click(templates["get_treasure_button"], screen):
            clicked = True
        elif find_and_click_best(templates["treasure_tile"], screen):
            clicked = True

    time.sleep(0.8)
