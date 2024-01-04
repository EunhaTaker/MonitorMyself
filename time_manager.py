import time

class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

class TimeManager:
    
    @staticmethod
    def getTimeFromStr(timeStr: str):
        """
        将时间字符串转换为时间戳
        """
        return int(time.mktime(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")))

    @staticmethod
    def getStrFromTime(timeStamp: int):
        """
        将时间戳转换为时间字符串
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timeStamp))

    @staticmethod
    def getTimeFromDate(dateStr: str):
        """
        将日期字符串转换为时间戳
        """
        return int(time.mktime(time.strptime(dateStr, "%Y-%m-%d")))

    @staticmethod
    def fillStrWithTime(timeFormat: str, timeStamp: int):
        """
        将时间戳填充到时间字符串中
        """
        return time.strftime(timeFormat, time.localtime(timeStamp))
    
    @staticmethod
    def getTimerFromTime(timeStr: str):
        items = timeStr.split(':')
        if len(items) != 3:
            return None
        return Timer(int(items[0]), int(items[1]), int(items[2]))