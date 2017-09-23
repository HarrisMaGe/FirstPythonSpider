# -*- coding: utf-8 -*-
import requests
from selenium import webdriver

class Html_Downloader(object):
    def download(self, new_url):
        res = requests.get(new_url)
        cont = res.text
        return cont

    def itemDownload(self,url):
        driver = webdriver.Chrome()
        driver.get(url)

        cont = driver.page_source
        driver.close()
        # print cont
        return cont