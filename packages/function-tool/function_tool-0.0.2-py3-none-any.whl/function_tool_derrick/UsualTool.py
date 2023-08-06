# -*- coding: utf-8 -*-
# @Time     : 2023/4/17 12:51
# @Author   : Long-Long Qiu
# @FileName : UsualTool.py
# @Product  : PyCharm
# import packages
import time
from enum import Enum

"""
与日期和时间相关的功能
"""

class TimestampType(Enum):
    """
    时间戳类型：枚举
    """
    SECONDS = 0 # 秒
    MILLISECOND = 1 # 毫秒

class DateTimeTool(object):

    @classmethod
    def timestamp2time (cls, ts: int=int(time.time()), formatter: str="%Y-%m-%d %H:%M:%S", tsType: TimestampType=TimestampType.SECONDS, transfer: bool=False) -> str:
        """
        时间戳转换为指定格式的时间字符串
        :param ts:
        :param formatter:
        :param tsType:
        :param transfer:
        :return:
        """

        if tsType == TimestampType.MILLISECOND:
            ts //= 1000

        if transfer:
            timeArray = time.localtime(ts + 8 * 60 * 60)
        else:
            timeArray = time.localtime(ts)
        otherStyleTime = time.strftime(formatter, timeArray)

        return otherStyleTime

    @classmethod
    def time2timestamp (cls, timeStr: str, formatter: str="%Y-%m-%d %H:%M:%S", tsType: TimestampType=TimestampType.SECONDS, transfer: bool=False) -> int:
        """
        时间字符串转换为时间戳
        :param timeStr:
        :param formatter:
        :param tsType:
        :param transfer:
        :return:
        """

        timeArray = time.strptime(timeStr, formatter)
        # 转换为时间戳
        timeStamp = int(time.mktime(timeArray))

        if transfer:
            timeStamp = timeStamp - 8 * 60 * 60

        if tsType == TimestampType.MILLISECOND:
            return timeStamp * 1000
        return timeStamp

