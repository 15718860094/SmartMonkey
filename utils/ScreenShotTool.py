import os
import pyautogui
import TimeTool
import settings


class ScreenShotTool:
    @staticmethod
    def take_screenshot():
        screenshot = pyautogui.screenshot()
        screenshot.save(
            os.path.join(
                settings.cache_path, "%s.png" % TimeTool.TimeTool().formatted_time()
            )
        )
