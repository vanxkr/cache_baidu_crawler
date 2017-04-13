#coding:utf-8

__author__ = 'vanxkr@gamil.com'
__version__ = '1.0.20170328'

import sys
import datetime

import url_manager
import html_downloader
import html_outputer
import html_parser

class SpiderMain(object):

    def __init__(self):
    
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.outputer = html_outputer.HtmlOutput()
        self.parser = html_parser.HtmlParser()
        
        self.keywords = None
        self.num = 0

    def craw(self):
    
        i = 0
        k = 0
        page_drop = 0
        
        f_1 = 0
        
        while i < int(self.num):
        
            next_page_url = self.urls.search_in_baidu(k,self.keywords)
            search_page = self.downloader.download(next_page_url)
            
            k = k + 50
            
            cache_urls = self.parser.parse(search_page)
            
            for j in cache_urls:
            
                # search all
                endi = j.find('&p1=')
                if j[endi+4:] == '1':
                    f_1 = f_1 + 1
                    if f_1 > 1:
                        print '## search all done'
                        return i,page_drop

                fi = j.find('&query=')
                print '# ['+str(i)+'/'+str(self.num)+']: http://cache.baiducontent.com/...'+j[fi:]
                
                flg = self.outputer.output_html(self.keywords,i,j)
                
                if flg == 'drop':
                    page_drop = page_drop + 1
                    
                i = i+1
                
                if i >= int(self.num):
                    return i,page_drop
        
        return i,page_redirect

if __name__=='__main__':

    obj_spider = SpiderMain()
    obj_spider.keywords = sys.argv[1] # 关键字
    obj_spider.num = sys.argv[2] # 抓取快照数量
    
    starttime = datetime.datetime.now()

    i,page_drop = obj_spider.craw()
    
    endtime = datetime.datetime.now()
    print '\n###############################'
    print '# '+str(i)+' pages used '+str((endtime - starttime).seconds)+' seconds.'
    print '# get page successful: '+str(i-page_drop)
    print '# page drop: '+str(page_drop)
    print '###############################'
    print 'Done!\n'
