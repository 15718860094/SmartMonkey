import os
import pyautogui
import TimeTool
from PIL import ImageGrab


class ScreenShotTool:
    @staticmethod
    def take_screenshot(img_path):
        screenshot = pyautogui.screenshot()
        screenshot.save(img_path)

    @staticmethod
    def take_screenshot_PIL():
        screenshot = ImageGrab.grab()  # 获取整个屏幕截图
        screenshot.save(
            os.path.join(
                settings.cache_path, "%s.png" % TimeTool.TimeTool().formatted_time()
            )
        )
