#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dorian Wang 2017.09.06
# lesson: download all comic from XKCD

import requests, os, bs4

# request = urllib.request.Request(
#     'http://xkcd.com/')
# web = urllib.request.urlopen(request)
# content = web.read()
# print(content.decode('utf-8'))

# cannot download: 1525
# delay in 1885, 1855, 1843, 1793, 1630, 1552, 1451, 1413, 1397, 1362, 1333
# 1297, 1291
url = 'http://xkcd.com/1291/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # download the page.
    print('Downloading page %s...' % url)
    resPage = requests.get(url)
    resPage.raise_for_status()

    soup = bs4.BeautifulSoup(resPage.text)
    # print(soup)

    # find the URL of the comic image.
    # <div id="comic">
    # <img src="//imgs.xkcd.com/comics/typing_notifications.png"
    # title="Over the years I've decided I'd rather have them on than
    # not, but I'm glad there aren't &quot;has opened a blank note to
    # compose a reply to you&quot; notifications."
    # alt="Typing Notifications"
    # srcset="//imgs.xkcd.com/comics/typing_notifications_2x.png 2x">
    # </div>
    # 为什么这种情况下使用#comic img?
    comicElem = soup.select('#comic img')
    # print(comicElem)
    if comicElem == []:
        print("could find the comic image.")
    else:
        # print(comicElem[0].get('src'))
        comicURL = "http:" + comicElem[0].get('src')
        # print(comicURL)
        # download the image.
        print("Downloading image %s..." % comicURL)
        resComic = requests.get(comicURL)

        # save the image to ./xkcd
        # TODO: only save the address into a file, and then output it to some other tools.
        # TODO: add title into the file, many of them are interesting.
        imageFile = open(os.path.join("xkcd", os.path.basename(comicURL)), 'wb')
        for chunk in resComic.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the prev button's url
    # <a rel = "prev" href = "/1885/" accesskey = "p" >
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    print(url)
print('Done.')
