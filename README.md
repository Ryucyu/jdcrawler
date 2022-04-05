# jdcrawler爬取京东手机商品页面
## 一个由scrapy + tkinter组合而成的项目


一键安装Python运行库：


**pip3 install -r requirements.txt**

**注意，本项目使用了mongodb作为主要数据库，建议提前安装mongodb**


## 使用方法
运行jdcrawler里的main.py运行scrapy框架进行京东页面的爬取
![image](https://user-images.githubusercontent.com/33159179/161721359-1b587973-b5cf-464c-95df-707f21677f0f.png)

等待运行完成后，可以在info.csv里，或mongodb的jdcrawler[jdphone]中看到数据
![image](https://user-images.githubusercontent.com/33159179/161722155-e7366851-dcce-4223-9916-aa84187cbfe2.png)
![image](https://user-images.githubusercontent.com/33159179/161722213-cf4e2a82-06ca-4678-87b0-2614e9123ae5.png)


之后，运行tkinterpart下的main_page.py文件，可以看到图形化的商品信息界面如下图所示
![image](https://user-images.githubusercontent.com/33159179/161722535-457d389c-d90f-421e-847d-35d7af34b8c9.png)


 可以对商品做出筛选（逻辑还不够完善），也可以查看商品的图片，并保存在img文件下
 
 
 
 之后会添加其他的商品（比如显卡），并且采用即使请求即使呈现的方式（其实其中显示图片的那个部分就是这个形式，效果也非常不错），不像现在是先获取数据再进行处理，主要是scrapy的框架不太好把tkinter嵌合进去，还是用request方便






