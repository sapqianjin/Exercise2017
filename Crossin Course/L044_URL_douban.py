# -*- coding: utf-8 -*
# Dorian Wang 2017.08.31
# lesson 44: Weather URL test

import urllib.request

request = urllib.request.Request(
    'http://my.qidian.com/level')
web = urllib.request.urlopen(request)
content = web.read()
print(content.decode('utf-8'))

# already read:
# https://book.douban.com/people/154536982/collect?start=0&sort=time&rating=all&filter=all&mode=grid
# https://book.douban.com/people/154536982/collect?start=15&sort=time&rating=all&filter=all&mode=grid
# https://book.douban.com/people/154536982/collect?start=30&sort=time&rating=all&filter=all&mode=grid
# https://book.douban.com/people/154536982/collect?start=45&sort=time&rating=all&filter=all&mode=grid
# ......
# https://book.douban.com/people/154536982/collect?start=195&sort=time&rating=all&filter=all&mode=grid

# reading:
# https://book.douban.com/people/154536982/do

# want to read:
# https://book.douban.com/people/154536982/wish

# here we can find the people number, in my homepage:
# https://www.douban.com/people/154536982/

# Douban Help:
# https://developers.douban.com/wiki/?title=book_v2
# https://developers.douban.com/wiki/?title=guide
# https://api.douban.com/v2/book/user/dorianwang/collections
# https://api.douban.com/v2/book/user/dorianwang/collections?start=20
# https://api.douban.com/v2/book/user/dorianwang/collections?start=40

# here we can format Json, then the structure is more clear.
# http://www.bejson.com/
