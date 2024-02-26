import pyautogui
import TimeTool

class ScreenShotTool:
    @staticmethod
    def take_screenshot(file_path):
        screenshot = pyautogui.screenshot()
        screenshot.save("%s.png" % TimeTool.TimeTool().formatted_time())
