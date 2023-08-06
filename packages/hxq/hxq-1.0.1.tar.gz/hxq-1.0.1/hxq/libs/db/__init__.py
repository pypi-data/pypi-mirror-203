# -*- coding: utf-8 -*-
# @Time    : 2022/12/6 23:18
# @Author  : hxq
# @Software: PyCharm
# @File    : __init__.py
import datetime
from json import JSONEncoder


class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat(sep=" ")
        return super().default(obj)
