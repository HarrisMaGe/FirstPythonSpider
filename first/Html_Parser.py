# -*- coding: utf-8 -*-
import Html_Manager,Html_Downloader
from bs4 import BeautifulSoup
import re


class Html_Parser(object):
    def __init__(self):
        self.judge = Html_Manager.Html_Manager()
        self.download = Html_Downloader.Html_Downloader()

        #self.new_urls = set()

    def parse(self, new_url, new_html):
        if new_url is None or new_html is None:
            return None

        soup = BeautifulSoup(new_html,'lxml')
        new_dates = self.get_new_date(new_url, soup)
        return new_dates

    def parseCatalog(self,start_url,start_html):
        catalogs_urls = set()
        soup = BeautifulSoup(start_html,'lxml')
        catalogs = soup.find_all('a',class_='cate_menu_lk')
        for url in catalogs:
            try:
                url = url['href']
                if url[0] =="/" and url[1] == "/":
                    real_url = 'http:'+url
                    catalogs_urls.add(real_url)
                    #print real_url
                else:
                    catalogs_urls.add(url)
                    #print url
            except:
                continue
        return catalogs_urls

    def paseItemURL(self,url,html):
        other_url = set()
        item_url = set()
        soup = BeautifulSoup(html,'lxml')
        allLinks = soup.find_all('a')
        itemMatch = re.compile(r'.*item.*')
        for link in allLinks:
            try:
                new_url = link['href']
                if new_url[0] == "/" and new_url[1] == "/":
                    real_url = 'http:' + new_url
                if re.match(itemMatch,real_url):
                    item_url.add(real_url)
                else:
                    other_url.add(new_url)
            except:
                continue


        return other_url,item_url

    def beginParser(self, new_url, new_html):

        if new_url is None or new_html is None:
            return None

        soup = BeautifulSoup(new_html, 'lxml')
        main_url = self.getMainUrl(soup)
        main_html = self.download.download(main_url)
        soup_catalog = BeautifulSoup(main_html, 'lxml')
        new_urls = self.get_new_urls(main_url, soup_catalog)
        new_dates = self.get_new_date(main_url, soup_catalog)
        return new_urls, new_dates

    def get_new_urls(self, new_url,soup):
        new_urls = set()
        #cata_urls = self.getCtalogUrl(soup)
        #item_urls = self.getItemsurl(soup)
        #for url in cata_urls:
            #new_urls.add(url)
        #for url in item_urls:
            #new_urls.add(url)

        urls = soup.find_all('a')
        for url in urls:
            try:
                url = url['href']
                if url[0] =="/" and url[1] == "/":
                    real_url = 'http:'+url
                    new_urls.add(real_url)
                    #print real_url
                else:
                    new_urls.add(url)
                    #print url
            except:
                continue
        return new_urls

    def get_new_date(self, new_url,soup):
        #titles = {}
        #titles['url'] = new_url
        #title = soup.find('title').get_text()
        #titles['title'] = title
        #return titles
        items = {}
        try:
            if len(new_url)<64:
                name = soup.find('div',class_='sku-name').get_text()
                shop = soup.find('div',class_='popbox-inner').find('h3').get_text()
                #catalog = soup.fond('div',class_=re.compile(r'item first')).get_text()
                items['name'] = name
                items['shop']  = shop
                #items['catalog'] = catalog
                items['url']   = new_url
                print name+"    "+shop
                return items
            else:
                return
        except:
            return



    def getMainUrl(self,soup):
        mainurl = soup.find('div',class_='main').find('a')['href']
        trueMainUrl = 'http://'+mainurl[2:]
        return trueMainUrl

    def getCtalogUrl(self,soup):
        cata_uels = set()
        cata_uels_1 = soup.find_all('a',class_="keyword")
        for cataurl in cata_uels_1:
            try:
                url = cataurl['href']
                if url[0] =="/" and url[1] == "/":
                    real_url = 'http:'+url
                    cata_uels.add(real_url)
                    #print real_url
                else:
                    cata_uels.add(url)
                    #print url
            except:
                continue
        return cata_uels

    def getItemsurl(self,soup):
        items_urls = set()
        items_urls_1 = soup.find_all("a",class_='category-name')
        for itemurl in items_urls_1:
            try:
                url = itemurl['href']
                if url[0] =="/" and url[1] == "/":
                    real_url = 'http:'+url
                    items_urls.add(real_url)
                    #print real_url
                else:
                    items_urls.add(url)
                    #print url
            except:
                continue
        return items_urls

    def getItemInUrl(self,url,html):
        items_urls_set = set()
        soup = BeautifulSoup(html,'lxml')
        items_urls = soup.fond_all('a',class_='J_ClickStat')
        print 1
        for url in items_urls:
            try:
                item_url = url['href']
                if item_url[0] == "/" and item_url[1] == "/":
                    real_url = 'http:' + item_url
                    items_urls_set.add(real_url)
                    print real_url
                else:
                    items_urls_set.add(item_url)
                    print item_url
            except:
                continue
        return items_urls_set

    def getItemsInformation(self,html):
        try:
            itemInfo = {}
            info = BeautifulSoup(html,'lxml')
            title = info.find('div',class_='tb-title').find('h3')['data_title']
            itemInfo['title'] = title
            price = info.find('div',class_='tb-title')
            real_price = price.find('em',class_='tb-rmb-num').get_text()+price.find('em',class_='tb-rmb').get_text()
            itemInfo['price']=real_price
            return itemInfo
        except:
            return

    #def parserJIngdong(self):
