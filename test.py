import cv2
import numpy as np
import pyautogui
import time
from PIL import Image

# координаты зеркала экрана iPhone
x, y, width, height = 0, 228, 450, 962
region = (x, y, width, height)


# 🔧 Вспомогательная функция: вырезка первой кнопки — по желанию
def crop_start_button_from_screen():
    screenshot = pyautogui.screenshot(region=region)
    left, top = 125, 830
    right, bottom = 415, 900
    button = screenshot.crop((left, top, right, bottom))
    button.save("templates/start_button.png")
    print("📦 Saved start_button.png")
# 🔧 Вспомогательная функция: вырезка кнопки из окна выбора слаймов
def crop_second_start_button():
    try:
        screenshot = pyautogui.screenshot(region=region)
        left, top = 167, 605
        right, bottom = 285, 645
        button = screenshot.crop((left, top, right, bottom))

        # Убедимся, что папка есть
        import os
        os.makedirs("templates", exist_ok=True)

        button_path = "templates/start_button_2.png"
        button.save(button_path)
        print(f"📦 Saved: {button_path}")
    except Exception as e:
        print(f"❌ Error saving template: {e}")
def crop_end_reward_button():
    try:
        screenshot = pyautogui.screenshot(region=region)
        left, top = 162, 740
        right, bottom = 290, 795
        button = screenshot.crop((left, top, right, bottom))

        import os
        os.makedirs("templates", exist_ok=True)

        button_path = "templates/end_reward_button.png"
        button.save(button_path)
        print(f"📦 Saved: {button_path}")
    except Exception as e:
        print(f"❌ Error saving template: {e}")
def crop_treasure_question_tile():
    try:
        screenshot = pyautogui.screenshot(region=region)
        left, top = 35, 515
        right, bottom = 125, 605
        button = screenshot.crop((left, top, right, bottom))

        import os
        os.makedirs("templates", exist_ok=True)

        path = "templates/treasure_tile.png"
        button.save(path)
        print(f"📦 Saved: {path}")
    except Exception as e:
        print(f"❌ Error saving treasure tile: {e}")
def crop_bonus_button():
    try:
        screenshot = pyautogui.screenshot(region=region)
        left, top = 240, 615
        right, bottom = 285, 665
        button = screenshot.crop((left, top, right, bottom))

        # Убедимся, что папка есть
        import os
        os.makedirs("templates", exist_ok=True)

        button_path = "templates/bonus_button.png"
        button.save(button_path)
        print(f"📦 Saved: {button_path}")
    except Exception as e:
        print(f"❌ Error saving template: {e}")
def crop_get_bonus_button():
    try:
        screenshot = pyautogui.screenshot(region=region)
        left, top = 145, 730
        right, bottom = 305, 795
        button = screenshot.crop((left, top, right, bottom))

        # Убедимся, что папка есть
        import os
        os.makedirs("templates", exist_ok=True)

        button_path = "templates/get_bonus_button.png"
        button.save(button_path)
        print(f"📦 Saved: {button_path}")
    except Exception as e:
        print(f"❌ Error saving template: {e}")
def crop_get_treasure_button():
    try:
        screenshot = pyautogui.screenshot(region=region)
        left, top = 155, 685
        right, bottom = 300, 730
        button = screenshot.crop((left, top, right, bottom))

        # Убедимся, что папка есть
        import os
        os.makedirs("templates", exist_ok=True)

        button_path = "templates/get_treasure_button.png"
        button.save(button_path)
        print(f"📦 Saved: {button_path}")
    except Exception as e:
        print(f"❌ Error saving template: {e}")



# ❗ Обрезку вызвать вручную при необходимости:
# crop_start_button_from_screen()
#crop_second_start_button()
#crop_end_reward_button()
# crop_treasure_question_tile()
#crop_get_bonus_button()
#crop_get_treasure_button()


# загрузка шаблонов
# bonus_img = cv2.imread("templates/new_bonus.jpg", cv2.IMREAD_COLOR)
# get_bonus_img = cv2.imread("templates/get_bonus.jpg", cv2.IMREAD_COLOR)
start_img = cv2.imread("templates/start_button.png", cv2.IMREAD_COLOR)
start_img_2 = cv2.imread("templates/start_button_2.png", cv2.IMREAD_COLOR)
end_reward_img = cv2.imread("templates/end_reward_button.png", cv2.IMREAD_COLOR)
treasure_tile_img = cv2.imread("templates/treasure_tile.png",cv2.IMREAD_COLOR)


# def find_and_click(template, screenshot, threshold=0.85):
#     if template is None:
#         print("❌ Template not loaded.")
#         return False
#     if screenshot.shape[0] < template.shape[0] or screenshot.shape[1] < template.shape[1]:
#         print("❌ Template is larger than screenshot.")
#         return False

#     result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
#     _, max_val, _, max_loc = cv2.minMaxLoc(result)
#     print(f"Match: {max_val:.3f}")

#     if max_val >= threshold:
#         h, w = template.shape[:2]
#         pyautogui.click(x + max_loc[0] + w // 2, y + max_loc[1] + h // 2)
#         print("✅ Clicked")
#         return True
#     return False
# def find_and_click_all(template, screenshot, threshold=0.85):
#     if template is None:
#         print("❌ Template not loaded.")
#         return False
#     # Приводим оба изображения к одинаковому формату BGR
#     if template.shape[2] == 4:
#         template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
#     if screenshot.shape[2] == 4:
#         screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

#     result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
#     locations = np.where(result >= threshold)
#     points = list(zip(*locations[::-1]))

#     if not points:
#         print("❌ No matches found.")
#         return False

#     h, w = template.shape[:2]
#     clicked_positions = set()

#     for pt in points:
#         center_x = x + pt[0] + w // 2
#         center_y = y + pt[1] + h // 2
#         if (center_x, center_y) not in clicked_positions:
#             pyautogui.click(center_x, center_y)
#             clicked_positions.add((center_x, center_y))
#             time.sleep(0.3)

#     print(f"✅ Clicked {len(clicked_positions)} tiles.")
#     return True
# def find_and_click_best(template, screenshot, threshold=0.85):
#     if template is None:
#         print("❌ Template not loaded.")
#         return False
#     if screenshot.shape[0] < template.shape[0] or screenshot.shape[1] < template.shape[1]:
#         print("❌ Template is larger than screenshot.")
#         return False

#     if template.shape[2] == 4:
#         template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
#     if screenshot.shape[2] == 4:
#         screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

#     result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
#     locations = np.where(result >= threshold)
#     gray_count = 0
#     yellow_count = 0

#     for pt in zip(*locations[::-1]):
#         h, w = template.shape[:2]
#         border_x = pt[0] + 2  # ближе к рамке слева
#         border_y = pt[1] + 2  # ближе к рамке сверху
#         b, g, r = screenshot[border_y, border_x]

#         if 170 < r < 200 and 170 < g < 200 and 170 < b < 200:
#             gray_count += 1
#             continue

#         yellow_count += 1
#         pyautogui.click(x + pt[0] + w // 2, y + pt[1] + h // 2)
#         print(f"✅ Clicked on yellow tile at ({pt[0] + w // 2}, {pt[1] + h // 2})")
#         break

#     print(f"🟡 Yellow tiles: {yellow_count} | ⚪ Gray tiles: {gray_count}")
#     return yellow_count > 0
# def find_and_click_best(template, screenshot, threshold=0.85):
#     if template is None:
#         return False
#     if screenshot.shape[0] < template.shape[0] or screenshot.shape[1] < template.shape[1]:
#         return False

#     if template.shape[2] == 4:
#         template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)
#     if screenshot.shape[2] == 4:
#         screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

#     result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
#     locations = np.where(result >= threshold)

#     for pt in zip(*locations[::-1]):
#         h, w = template.shape[:2]
#         b, g, r = screenshot[pt[1] + 2, pt[0] + 2]
#         if 170 < r < 200 and 170 < g < 200 and 170 < b < 200:
#             continue  # серый
#         pyautogui.click(x + pt[0] + w // 2, y + pt[1] + h // 2)
#         return True

#     return False

# ✅ Основной проход
screenshot = pyautogui.screenshot(region=region)
screenshot.save("debug_get_treasure_screen.png")
screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

time.sleep(2)
# clicked = False

# # 1. Попытка взять бонус
# if find_and_click(bonus_img, screen):
#     time.sleep(1.5)
#     screen = cv2.cvtColor(np.array(pyautogui.screenshot(region=region)), cv2.COLOR_RGB2BGR)
#     find_and_click(get_bonus_img, screen)
#     clicked = True

# # 2. Если бонус не найден — проверяем кнопки начала боя или награды
# if not clicked:
#     if find_and_click(start_img_2, screen):
#         clicked = True
#     elif find_and_click(start_img, screen):
#         clicked = True
#     elif find_and_click(end_reward_img, screen):
#         clicked = True

# # 3. Если все ещё ничего не найдено — проверяем мини-игру
# if not clicked:
#     treasure_tile_img = cv2.imread("templates/treasure_tile.png", cv2.IMREAD_UNCHANGED)
#     matches = find_and_click_best(treasure_tile_img, screen)
#     if matches:
#         clicked = True
