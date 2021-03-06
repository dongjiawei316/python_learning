# 爬虫调度程序
#from bike_spider import url_manager, html_downloader, html_parser, html_outputer
from UrlManger import UrlManager
from htmldownload import HtmlDownloader
from HtmlParser import HtmlParser
from HtmlOutputer import HtmlOutputer

# 爬虫初始化
class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, my_root_url):
        count = 1
        self.urls.add_new_url(my_root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                # 下载网页
                html_cont = self.downloader.download(new_url)
                # 解析网页
                self.parser.parse_test(new_url, html_cont)
                """
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                # 网页输出器收集数据
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count += 1
                """

            except:
               print("craw failed")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://www.sina.com.cn/"
    root_url = "http://www.sohu.com/"
    #root_url = "https://baike.baidu.com/item/c%E8%AF%AD%E8%A8%80/105958?fromtitle=c&fromid=7252092"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
