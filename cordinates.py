import pyautogui
import time

print("Press Ctrl-C to quit.")
try:
    while True:
        x1, y1 = pyautogui.position()
        width, height = pyautogui.size()
        x2 = x1 + width
        y2 = y1 + height
        position_str = f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}"
        print(position_str, end="")
        print("\b" * len(position_str), end="", flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone.")