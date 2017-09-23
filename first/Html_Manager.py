# -*- coding: utf-8 -*-
class Html_Manager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.items_new_urls = set()
        self.items_old_utls = set()
        self.catalog_url = set()
        self.old_catalog_url=set()

    def catalogUrl(self,url):
        if url is None:
            return
        self.catalog_url.add(url)

    def catalogHasurl(self):
        return len(self.catalog_url)!=0

    def getCatalogurl(self):
        url = self.catalog_url.pop()
        self.old_catalog_url.add(url)
        return url

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def has_new_url(self):
        return len(self.new_urls)!=0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def add_urls(self, new_urls):
        if new_urls is None:
            return
        for url in new_urls:
            if url is None:
                continue
            self.new_urls.add(url)

    def items_has_new_url(self):
        return len(self.items_new_urls)!=0


    def add_items_urls(self, new_urls):
        if new_urls is None:
            return
        for url in new_urls:
            if url is None:
                continue
            self.items_new_urls.add(url)

    def get_items_url(self):
        url = self.items_new_urls.pop()
        self.items_old_utls.add(url)
        return url

    def printItemURL(self):
         while self.items_has_new_url():
             url = self.items_new_urls.pop()
             print url
