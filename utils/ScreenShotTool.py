import os
import pyautogui
import TimeTool
import settings
from PIL import ImageGrab
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ScreenShotTool:
    @staticmethod
    def take_screenshot():
        screenshot = pyautogui.screenshot()
        img_path = os.path.join(
            settings.cache_path, "%s.png" % TimeTool.TimeTool().formatted_time()
        )
        screenshot.save(img_path)
        return img_path

    @staticmethod
    def take_screenshot_PIL():
        screenshot = ImageGrab.grab()  # 获取整个屏幕截图
        screenshot.save(
            os.path.join(
                settings.cache_path, "%s.png" % TimeTool.TimeTool().formatted_time()
            )
        )
