# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 17:10
# @Author  : hxq
# @Software: PyCharm
# @File    : __init__.py
from hxq.interface.db_helper import DBHelper
from hxq.interface.httpx import http

# if __name__ == '__main__':
#     CONFIG = {
#         'SQL_CREATOR': 'MySQL',
#         'SQL_HOST': '127.0.0.1',
#         'SQL_USER': 'root',
#         'SQL_PASSWORD': '123456',
#         'SQL_DATABASE': 'blog'
#     }
#     db = DBHelper(config=CONFIG)
#     print(db.all("SHOW DATABASES;"))
#     print(db.first("SELECT * FROM  rule_group"))

if __name__ == '__main__':
    http.download(
        'https://infinitypro-img.infinitynewtab.com/wallpaper/nature/pad_nature_6.jpg?attname=infinity-328409872.jpg',
        file_path='3284098721.jpg'
    )
