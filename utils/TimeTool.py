from datetime import datetime


class TimeTool:
    def __init__(self) -> None:
        self.today_date = datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def formatted_time():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time
