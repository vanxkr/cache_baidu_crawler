## 百度快照爬虫 
版本：1.0.20170328  
-By 向宇翔 [ <a href='http://vanxkr.com' target='_blank'>vanxkr.com</a> | vanxkr@gmail.com ] 

环境：
OS: ubuntu14.04 x86
python: 2.7.9

model安装:
```shell
sudo pip install bs4 re urllib pyopenssl ndg-httpsclient pyasn1
```

运行时示例：
```shell
python crawler_main.py ["关键字(可以有空格)"] [爬取条数]
```

爬取数据存放在 `./html` # 若无法自动创建文件夹，请在文件当前目录创建 `./html`

* 规则：
    * 超时等待时间为5s，连续5次超时 drop
    * 为方便文件处理，输出文件关键字间空格已用 '_' 代替
