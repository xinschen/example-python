#### Scrpay用法
```
创建项目
scrapy startproject tutorial
目录结构说明
scrapy.cfg: 项目的配置文件
tutorial/: 该项目的python模块。之后您将在此加入代码。
tutorial/items.py: 项目中的item文件.
tutorial/pipelines.py: 项目中的pipelines文件.
tutorial/settings.py: 项目的设置文件.
tutorial/spiders/: 放置spider代码的目录.

```

#### 本项目使用
##### 一、美食类爬虫
 ```
 爬取的网站：美食节
 进入tutorial目录，执行 
 scrapy crawl meishi  #结果输出到终端
 scrapy crawl meishi  -o items.json #输出到文件
 

```