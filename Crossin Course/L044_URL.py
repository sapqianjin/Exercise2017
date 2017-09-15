#-*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 44: Weather URL test

import urllib.request

request = urllib.request.Request('http://www.douban.com')
web = urllib.request.urlopen(request)
content = web.read()
print(content.decode('utf-8'))

