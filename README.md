# GetLinksFromSoBooks

项目初衷：因为想获取免费的电子书籍，但是每次寻找书籍都会浪费大量时间，尤其在大型的免费电子书籍网站上，所以尽自己可能提取所需的信息(书籍名称，作者名，书籍在网站的详情页，书籍免费百度网盘地址，书籍百度网盘提取码)。

> 从SoBooks爬取所有Kindle书的百度网盘链接以及提取码，用户可以直接浏览本项目，直接下载

![Apache 2](https://img.shields.io/badge/license-Apache%202-brightgreen.svg) ![build](https://img.shields.io/badge/build-passed-green.svg) ![version](https://img.shields.io/badge/Python-3.7.2-green.svg)





## 安装模块
```python
pip install requests
pip install beautifulsoup4
pip install selenium
pip install openpyxl
```

## v0.2
<details>
<summary>展开查看</summary>
<pre><code>.
├── GetLinksFromSoBooks
├── v0.1 第一版本(废弃)
│   ├── Owner: maojian,haoguanwei,linmiao
│   ├── admin
├── v0.2 第二版本(可以使用)
│   ├── crawl_tool.py  爬虫模块
│   ├── model.py 将爬取到的每个书籍看做一个model中的book对象，方便于以后扩展Flask
</code></pre>
</details>

### TODO
1. 在每个书籍的详细信息页面中，由于水平有限，没有找到post请求提交的地址，所以需要使用selenium模拟控制浏览器来获得百度网盘提取码。期待后面可以使用BeautifulSoup来获取每个书籍的百度网盘提取码
2. 未来将集成flask用于将爬取到的信息展示到本地网页服务器
3. ~~openpyxl~~ 将不会在未来使用

### 问题
如果有什么问题，可以issue，谢谢！

另外一个免费的电子书籍网站，请参考爬取源代码[ITbooks](https://github.com/sivanWu0222/CrawlITBooks/tree/master/Python%E7%88%AC%E5%8F%96ItBooks)



## v0.1
### Questions

由于项目使用Python的Selenium模块来自动模拟控制浏览器，本项目自动模拟使用Chrome，因此**需要提前安装相应的Chrome以及对应的插件**

[下载地址](https://pan.baidu.com/s/1Xerfeqzk2ScLvaE6qz5uYQ)

提取码：07na 



注意：插件版本需要与Chrome相匹配



1. 编译运行项目，出现 ==windows chromedriver' executable needs to be in PATH== 

   [解决方案](http://www.sivan.tech/2019/02/04/windows-chromedriver-executable-needs-to-be-in-PATH/)


### 以下模块尚未用到
```
• pip install send2trash
• pip install PyPDF2
• pip install python-docx（安装 python-docx，而不是 docx）
• pip install imapclient
• pip install pyzmail
• pip install twilio
• pip install pillow
• pip install pyobjc-core（仅在 OS X 上）
• pip install pyobjc（仅在 OS X 上）
• pip install python3-xlib（仅在 Linux 上）
• pip install pyautogui
```