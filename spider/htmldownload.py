# 网页下载器
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        # code不为200则请求失败
        if response.getcode() != 200:
            print("down load url failed")
            return None
        return response.read()
