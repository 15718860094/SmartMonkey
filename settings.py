import logging

# Attention
# 关注类别
attention_type = {

} 
# 关注关键字
attention_keyword = {

}
# ScreenShotTool
persistent=True # 是否永久保存截屏
cache_path='data/screen_cache' # 截屏图片缓存路径
shotcut_step=10 # 每次截屏的间隔时间

# ImageHandler
deduplication_threshold = 0.75  # 重复数据删除阈值

 

# Log
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
