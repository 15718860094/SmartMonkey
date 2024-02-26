from datetime import datetime


class TimeTool:
    @staticmethod
    def formatted_time():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
