import re
import time

import requests
from pyquery import PyQuery as pq

from config import Source

class StockSpider:
    def __init__(self, stockId, scale=1, source='SINA'):
        self._scale = scale
        if source == 'SINA':
            self._source = Source.SINA
        if type(stockId) is not str:
            return 'StockId must be str'
        if re.match('^(sz|sh)[0-9]+$', stockId) is None:
            return 'StockId is unavailable'
        self._stockId = stockId

    def work(self):
        resp = requests.get(str.format(self._source.SINA_RS, self._stockId))
        dataList = resp.content.split(b'"')[1].decode('gbk').split(',')
        print('{name} price: {price}'.format(name=dataList[0], price=dataList[3]))

a = StockSpider('sz300605')
while True:
    time.sleep(1)
    a.work()


