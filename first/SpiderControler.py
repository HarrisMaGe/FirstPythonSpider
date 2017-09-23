# -*- coding: utf-8 -*-
import Html_Manager,Html_Downloader,Html_Parser,Html_Outputer


class SpiderControler(object):
    def __init__(self):
        self.manager = Html_Manager.Html_Manager()
        self.downloader = Html_Downloader.Html_Downloader()
        self.parser = Html_Parser.Html_Parser()
        self.outputer = Html_Outputer.Html_Outputer()



    def startSPider(self, start_url):
        count =1
        start_html = self.downloader.download(start_url)
        catalog_urls = self.parser.parseCatalog(start_url,start_html)
        for url in catalog_urls:
            self.manager.catalogUrl(url)


        while self.manager.catalogHasurl():
            catalogurl=self.manager.getCatalogurl()
            catalogHtml = self.downloader.download(catalogurl)
            other_urls,item_urls = self.parser.paseItemURL(catalogurl,catalogHtml)
            self.manager.add_urls(other_urls)
            self.manager.add_items_urls(item_urls)


        while self.manager.has_new_url():

            try:
                new_url = self.manager.get_new_url()
                new_html = self.downloader.download(new_url)
                other_urls, item_urls = self.parser.paseItemURL(new_url, new_html)
                self.manager.add_urls(other_urls)
                self.manager.add_items_urls(item_urls)

                count+=1

                if count==100:
                    break
            except:
               continue

        while self.manager.items_has_new_url():
            try:
                new_url = self.manager.get_items_url()
                new_html = self.downloader.download(new_url)
                date = self.parser.parse(new_url,new_html)
                self.outputer.collectItemDte(date)
            except:
                continue


        self.outputer.output()

