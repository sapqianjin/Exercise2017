# -*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 44: Weather

import urllib.request
import json
from L043_City_Dict import city

# request = urllib.request.Request('http://www.douban.com')
# web = urllib.request.urlopen(request)
# content = web.read()
# print(content.decode('utf-8'))

cityName = input('请输入需要查询的城市：\n')
cityCode = city.get(cityName)
if cityCode:
    try:
        print(cityCode)
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % cityCode)
        content = urllib.request.urlopen(urllib.request.Request(url)).read()  # type = bytes
        # print(content)
        print(content.decode('utf-8'))

        data = json.loads(content)  # type = dict
        print("data: %s" % data)

        result = data['weatherinfo']
        print("result: %s" % result)

        string_temp = ('%s: %s，气温：%s~%s\n' % (
            result['city'],
            result['weather'],
            result['temp1'],
            result['temp2'],
        ))
        print(string_temp)
    except:
        print('查询%s天气失败' % cityName)
else:
    print("未找到城市%s代码" % cityName)
