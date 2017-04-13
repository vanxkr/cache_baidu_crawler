#coding:utf-8

__author__ = 'vanxkr@gamil.com'

import urllib

class UrlManager(object):
    def __init__(self):
        pass

    def search_in_baidu(self,i,keyword):
        p= {'wd': keyword}
        url = "http://www.baidu.com/s?" + urllib.urlencode(p)+'&pn='+str(i)+'&rn=50'
        return url
