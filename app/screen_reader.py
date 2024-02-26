from utils.TimeTool import TimeTool
from utils.ScreenShotTool import ScreenShotTool
from settings import *
import os
import sys
import logging
import signal
import time

sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'utils'))


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


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
        pid = os.getpid()
        logging.info("进程ID为: %s", pid)

        try:
            while True:
                ScreenShotTool().take_screenshot()
                time.sleep(shotcut_step)
        except KeyboardInterrupt:
            self.graceful_exit(signal.SIGINT, None)

    def graceful_exit(self, signum, frame):
        logging.info("接收到信号，优雅地关闭程序。")
        # 在这里添加一些清理操作，如果有的话
        exit(0)


# 创建单例实例
SingletonLoop()
