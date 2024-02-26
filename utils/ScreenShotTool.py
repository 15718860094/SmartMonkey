import os
import pyautogui
import TimeTool
import settings
from PIL import ImageGrab

class ScreenShotTool:
    @staticmethod
    def take_screenshot():
        screenshot = pyautogui.screenshot()
        screenshot.save(
            os.path.join(
                settings.cache_path, "%s.png" % TimeTool.TimeTool().formatted_time()
            )
        )
    @staticmethod
    def take_screenshot_PIL():
        screenshot = ImageGrab.grab()  # 获取整个屏幕截图
        screenshot.save(
            os.path.join(
                settings.cache_path, "%s.png" % TimeTool.TimeTool().formatted_time()
            )
        )
# 调用截图函数
ScreenShotTool.take_screenshot()