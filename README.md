# 百度快照爬虫 -By 向宇翔[vanxkr@gmail.com | github - https://github.com/vanxkr]
版本：1.0.20170328

环境：
OS: ubuntu14.04 x86
python: 2.7.9

model安装:
    sudo pip install bs4 re urllib pyopenssl ndg-httpsclient pyasn1

运行时示例：
python crawler_main.py ["关键字(可以有空格)"] [爬取条数]

爬取数据存放在 ./html # 若无法自动创建文件夹，请在文件当前目录创建 ./html

规则：
    1. 超时等待时间为5s，连续5次超时 drop
    2. 为方便文件处理，输出文件关键字间空格已用 '_' 代替
    3. 启用网页压缩，加快了网页的抓取
