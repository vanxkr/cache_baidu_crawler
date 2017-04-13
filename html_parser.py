#coding:utf-8

__author__ = 'vanxkr@gamil.com'

import re
from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath
from bs4 import BeautifulSoup

class HtmlParser(object):
    def __init__(self):
        pass

    def _vanxkr_join(self,base,url):
        url1 = urljoin(base, url)
        arr = urlparse(url1)
        path = normpath(arr[2])
        return urlunparse((arr.scheme,arr.netloc,path,\
            arr.params,arr.query,arr.fragment))

    def _get_cache_urls(self,soup):
        tags = soup.find_all('a',href=re.compile(r'^http://cache.baiducontent.com/*'))
        cache_urls = []
        for i in tags:
            cache_urls.append(i['href'])
        return cache_urls

    def _get_next_page_url(self,soup):
        print soup.find('a',class_=re.compile(r'^n$'))
        next_page_url = soup.find('a',class_=re.compile(r'^n$'))['href']
        next_page_full_url = self._vanxkr_join('https://www.baidu.com',next_page_url)
        return next_page_full_url

    def parse(self,html_cont):
        if html_cont is None:
            return 'error: html_cont is None'
        soup = BeautifulSoup(html_cont,'html.parser')
        cache_urls = self._get_cache_urls(soup)
        return cache_urls
