# -*- coding: utf-8 -*-
import requests as requests
import selenium


#def selenium_init(browser, url, para):
#    sel = selenium('localhost', 4444, browser, url)
#    sel.start()
#    sel.open(para)
#    sel.set_timeout(60000)
#    sel.window_focus()
#    # sel.window_maximize()
#    return sel


#if __name__ == "__main__":
 #   browser = '*firefox'
 #   html = ''
 #   sel1 = selenium_init(browser, 'http://music.baidu.com', '/top')
  #  try:
  #      html = sel1.get_html_source()
 #   finally:
  #      sel1.stop()
 #       print html
import os

import time
from selenium import webdriver
from bs4 import BeautifulSoup


#res = requests.get("https://item.taobao.com/item.htm?spm=a219r.lm874.14.8.MPtHhm&id=524100048964&ns=1&abbucket=3")
#begin = "http://www.jingdong.com"
#begin = "https://item.taobao.com/item.htm?spm=a219r.lm874.14.8.MPtHhm&id=524100048964&ns=1&abbucket=3"
#driver = webdriver.Chrome()
#driver.get(begin)
#cont = driver.page_source
#driver.close()
#res = requests.get(begin)
#cont = res.text
#soup = BeautifulSoup(cont,"lxml")
#print cont
##link = soup.find_all('a')
#for url in link:
    #print url['href']

import urllib2
res = urllib2.urlopen("https://www.baidu.com")
print res



