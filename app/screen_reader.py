# import settings
# from utils import ScreenShotTool, TimeTool
import os
import logging
import signal

# 定义退出函数
def graceful_exit(signum, frame):
    logging.info("接收到退出信号，正在关闭程序")
    # TODO 添加程序逻辑
    exit(0)

# 注册退出信号处理函数
signal.signal(signal.SIGINT, graceful_exit)
signal.signal(signal.SIGTERM, graceful_exit)

# 记录进程ID
pid = os.getpid()
logging.info("程序启动成功，进程ID为:", pid)

# 单例循环
try:
    while True:
        pass
except KeyboardInterrupt:
    graceful_exit(signal.SIGINT, None)
