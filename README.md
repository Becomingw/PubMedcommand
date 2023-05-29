# :bulb:基于Python的PubMed爬虫文献推荐

## :artificial_satellite: 功能：

1.输入关键词（支持中英输入），可以为作者，普通关键词或者期刊；

2.输出为excel表格，以列表形式存储文献信息；

3.支持文献标题与摘要翻译（目前采用彩云:cloud:小译API）；

4.随机选取一篇文献发送到指定邮箱（带中英文摘要）；

## :dagger: 使用：

1.首先你得有个彩云翻译API、开启stamp的网易163邮箱、一个接收邮件的其他邮箱；

​	a.先说彩云翻译API，去彩云翻译官网申请，[官方文档](https://docs.caiyunapp.com/blog/2018/09/03/lingocloud-api/) :point_left:，注意存好Token，后面有用；

​	b.注册网易163邮箱，打开启stamp，开启方法自行搜索，开启后会给一个License，这个也要保存好；

​	c.一个其他邮箱，qq邮箱应该每个人都有，其他邮箱理论也可；

​	d. 目前，你要有这几个码①彩云token；②163邮箱地址及其license；③一个其他邮箱地址

​	e.你得安装Python3.6及以上版本

2.下载两py文件，点击[下载](https://cowtransfer.com/s/b0a288c15ec84d) 。

3.解压后，用python先打开init.py文件，也可以用记事本打开复制到相应编译器打开（自动配置运行初始环境)

4.打开PubMedclawer.py文件，找到配置部分，如图：

![token.png](https://s2.loli.net/2022/11/26/ofPH4LTN2iqkcdF.png)

![clawer配置.png](https://s2.loli.net/2022/11/26/NZcI8XAdmwesH4B.png)

**红色马赛克部分都是比填项，token，receiver，sender，pwd（license）**

5.其他部分在代码里面写的很清楚，:bangbang:建议不要将page改的过大，运行时间长，而且没那么必要（还有被封IP的可能）;

6.run起来后请尽量按要求填写内容，不然可能会报错（虽然有一定的处理机制），:heavy_check_mark:关键词支持中英文输入:heavy_check_mark: ；

7.得到的文献存储在py文件同目录的RX.xlsx（这个地址可以更改）中，同时会发送一封邮件到你到你的邮箱:e-mail: ；

## :zap: 接下来做什么？

1.优化邮箱显示形式；加入Flask框架，使用html来显示邮箱文本；

2.加入其他网站爬取选项，加入指定期刊官网爬取最新文献；

3.加入自动运行，定时爬取文献，并发送到自己邮箱；

4.用flask写一个web前端，部署到服务器，达到更方便的使用；

5.定期推送指定期刊（自己研究领域的专业期刊）的最新一些文献摘要到邮箱，养成阅读最新行业顶尖文献的好习惯!!!

### :house: [我的博客](blog.becomingw.cn) 

# 本项目不再更新，定期文献推荐可以使用Pubmed自带的文献推送[Look this tutorial](https://www.xiahepublishing.com/2475-7543/ArticleFullText.aspx?sid=2&id=10.14218%2FMRP.2016.033)





