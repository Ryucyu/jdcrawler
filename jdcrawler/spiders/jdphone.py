import scrapy,re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options    # 使用无头浏览器
from scrapy import signals
from jdcrawler.items import JdcrawlerItem

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class JdphoneSpider(scrapy.Spider):
    name = 'jdphone'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=2095e905c7534e00b6ac6232b6f1c910&page=1&s=1&click=0']
    page = 1

    custom_settings = {
        'DOWNLOAD_DELAY':0.5
    }
    Cookie = '__jdu=1627024440534187317840; shshshfpa=a8a08250-e249-f65e-37ed-0aa5fb5f8a85-1627797593; shshshfpb=wQNedzIC9WyDmF7sjAanQZQ%3D%3D; pinId=2d48dZ-sL5asonOA5_t1Hg; pin=jd_vQkZAAwQwXMt; unick=jd_vQkZAAwQwXMt; _tp=Wus08TNYxPn9iHO5MYbnnQ%3D%3D; _pst=jd_vQkZAAwQwXMt; user-key=71a53daf-1873-40a3-b2a9-29686717c3bd; cn=2; ipLocation=%u6d59%u6c5f; PCSYCityID=CN_330000_330600_0; areaId=15; ipLoc-djd=15-1255-15944-51612; unpl=JF8EAMdnNSttDx4EVxwFGkYXH19RW1oNSh9UO2FXV1hQQlwDHVFMGxd7XlVdXhRKFR9tZxRUVFNIVA4fCysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwRFkpeUVtYCU8VBm9uA1ZdXkJRBCsyHCIge15cX14BTScCX2Y1FgkETlMGHgodXxBMXlJfXg1OEgJrZQBUVF5JVAMSBxoiEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_fdac660e6e3446409fe7c2498977bf86|1648722120237; __jdc=122270672; __jda=122270672.1627024440534187317840.1627024440.1648704405.1648709293.19; shshshfp=ffbb8ca43179a4d63773014ae62e1391; token=dfb91c31bd0fba2f8caa04affa2dcf94,3,915956; __tk=Xphyvph1v3X1YpJ5XDhzvsaFZca5YshEZpdnvprnZsr3Y3hyuDbTv2,3,915956; ip_cityCode=1255; wlfstk_smdl=g3iieshd07ar5359qc30mxk1luf43x3k; ceshi3.com=000; TrackID=1zQAlPSWR0tzaWGtOaT-acAm9SK1REMZ8FfemRfWC42oxSz9tdFI4TCPr3m6BbG6LH3lAksjDfPUpGsF1_oT9rDIJzzj0YPHfcBPjdSfuZD1EwnWduIlu5wHx_XpLyP8i; thor=3BDDDEBDDB42CED6A3C3E8962EE71AC7597CDA5BC03EAB963D687A76E30A035FA2EC26158A16F609C7FD2FFF9F5B6BA44D258C88A6D6F94DD64B8CE25173DB7CE4DFBFE0CB1E869260E3026B9B93F09CCD3698CD63D712A248CF98A59929C92D94ADC278D427D5F1A451A65A50FC9D1664951BFD845DC9F9E4268A4B01227066DAFB5C03EFE6F7808C543FD41528206F490EFADE2A6AF6A0467F101C48749BC2; shshshsID=cc9b9a4ab0c35e44955483cebc793cda_78_1648722209838; __jdb=122270672.93.1627024440534187317840|19.1648709293; 3AB9D23F7A4B3C9B=THB23IK6CTP2BTHYKTEO46KWEATO4KX4F542GHGIYW7D5IDHPBHLN3SGEMBGWGLZHEY6ABW4AEIT2GPKCPD2Z653YQ'
    cookies = {i.split('=')[0]: i.split('=')[1] for i in Cookie.split('; ')}

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(JdphoneSpider, cls).from_crawler(crawler, *args, *kwargs)
        spider.chrome = webdriver.Chrome(options=chrome_options)
        crawler.signals.connect(spider.spider_closed, signal=spider.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.browser.quit()

    def parse(self, response):
        for i in range(1,61):
            item = JdcrawlerItem()
            price = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[3]/strong/i/text()').extract_first()
            pic = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[1]/a/img/@data-lazy-img').extract_first()
            inner_href = response.xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[4]/a/@href').extract_first()

            if pic == None:
                pic = "none"
            if inner_href == None:
                inner_href = "none"
            item['price'] = price
            item['pic'] ='https:' + pic
            item['inner_href'] = 'https:' + inner_href

            yield scrapy.Request(
                item['inner_href'],
                callback=self.parse_inner,
                cookies=self.cookies,
                meta={"item": item},
            )

        next_url = f'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=2095e905c7534e00b6ac6232b6f1c910&page={self.page}'
        if self.page <= 160:
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                cookies=self.cookies
            )
            self.page = self.page + 1

    def parse_inner(self,response):
        item = response.meta['item']

        result = re.findall(r'商品名称：(.*?)<', response.text)
        item['name'] = "未知商品名" if result == [] else result[0]

        result = re.findall(r'运行内存：(.*?)<', response.text)
        item['RAM'] = "未知运行内存" if result == [] else result[0]

        result = re.findall(r'机身内存：(.*?)<', response.text)
        item['ROM'] = "未知机身内存" if result == [] else result[0]

        result = re.findall(r'后摄主摄像素：(.*?)<', response.text)
        item['After_taken_pixel'] = "未知后摄像素" if result == [] else result[0]

        result = re.findall(r'分辨率：(.*?)<', response.text)
        item['resolution'] = "未知分辨率" if result == [] else result[0]

        result = re.findall(r'CPU型号：(.*?)<', response.text)
        item['CPU'] = "暂无型号" if result == [] else result[0]

        result = re.findall(r'移动5G', response.text)
        item['S5G'] = "不支持5G" if result == [] else "支持5G"

        yield item




