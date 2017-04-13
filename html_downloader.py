#coding:utf-8

__author__ = 'vanxkr@gamil.com'

import urllib
import requests

class HtmlDownLoader(object):
    def download(self,url):
        if url is None:
            return None

        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'Host': 'pan.baidu.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
            
        for i in range(5):
            try:
                html = requests.get(url, headers=headers, allow_redirects=False, timeout=5)
                
                if html.status_code == 200:
                    return html.content
                else:
                    return 'drop'
                
            except requests.exceptions.ReadTimeout:
                print '## ['+str(i)+'] get page timeout'
                continue
            
            except requests.exceptions.ConnectionError:
                return 'drop'
                
        return 'drop'
