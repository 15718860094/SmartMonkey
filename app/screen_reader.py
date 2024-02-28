
from settings import *
from utils.ImageHandler import ImageHandler
from utils.OllamaHandler import OllamaHandler
from utils.ScreenShotTool import ScreenShotTool
from utils.TimeTool import TimeTool
import os
import shutil
import sys
import signal
import time
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'utils'))
sys.path.append(os.path.join(os.getcwd(), '.'))


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class SingletonLoop:
    def __init__(self):
        self.run()

    def run(self):
        self.imgs_directory = os.path.join(cache_path, TimeTool().today_date)
        pid = os.getpid()
        logging.info("进程ID为: %s", pid)
        if not os.path.exists(self.imgs_directory):
            os.makedirs(self.imgs_directory)
        try:
            while True:
                img_path = os.path.join(
                    self.imgs_directory, "%s.png" % TimeTool.formatted_time())
                ScreenShotTool.take_screenshot(img_path)
                ollama_handler = OllamaHandler(
                    model='llava', prompt='请用中文描述一下这个图片的内容')
                ollama_handler.request_with_images(img_path)

                time.sleep(shotcut_step)

        except KeyboardInterrupt:
            self.graceful_exit(signal.SIGINT, None)

    def graceful_exit(self, signum, frame):
        logging.info("接收到信号，优雅地关闭程序。")
        if not persistent:
            shutil.rmtree(self.imgs_directory)
            os.rmdir(self.imgs_directory)
        exit(0)

# 创建单例实例
SingletonLoop()
