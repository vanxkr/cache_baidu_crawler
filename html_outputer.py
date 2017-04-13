#coding:utf-8

__author__ = 'vanxkr@gamil.com'

import time
import urllib
import sys

import html_downloader

reload(sys)
sys.setdefaultencoding('utf-8')

class HtmlOutput(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownLoader()

    def output_html(self,keywords,i,url):
        if url is None:
            return
        html_cont = self.downloader.download(url)
        if html_cont != 'drop':
            fout = open('./html/'+keywords.replace(' ','_')+'_'+str(i)+'.html','w+')
            fout.write(html_cont)
            fout.close()
            return 'ok'
        else:
            return 'drop'
