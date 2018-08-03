# 网页解析器
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HtmlParser(object):

    def parse_test(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print("url is None,", page_url)
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        links = soup.find_all("a")
        for link in links:
            print(link)
            new_url = link['href']
            print(new_url)
            # 获取到的url不完整，学要拼接
            #new_full_url = urljoin(page_url, new_url)
            #print(new_full_url)

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print("url is None,", page_url)
            return
        #使用python标准库（html.parser）来解析网页
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)
        self._print_new_urls(new_urls)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_data(self, page_url, soup):
        res_data = {"url": page_url}
        # 获取标题
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()
        summary_node = soup.find("div", class_="lemma-summary")
        res_data["summary"] = summary_node.get_text()
        return res_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 查找出所有符合下列条件的url
        #links = soup.find_all("a", href=re.compile(r"/item/"))
        links = soup.find_all("a", href=re.compile(r"/s/"))
        for link in links:
            new_url = link['href']
            # 获取到的url不完整，学要拼接
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _print_new_urls(self, new_urls):
        print("new urls nums : ", str(len(new_urls)))
        for url in new_urls:
            print("url :", url)