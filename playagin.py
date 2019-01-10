import os
import urllib
import urllib.request
import urllib.parse
from lxml import etree


class Spider:
    def __init__(self):
        # self.tiebaName = input('输入贴吧名字:')
        # self.beginPage = int(input('开始页数:'))
        # self.endPage = int(input('结束页数:'))
        self.tiebaName = '图片'
        self.beginPage = int(1)
        self.endPage = int(20)

        self.url = 'http://tieba.baidu.com/f'
        self.ua_headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;'}
        self.userName = 1

    def tiebaSpider(self):
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50
            word = {'kw': self.tiebaName, 'pn': pn}
            word = urllib.parse.urlencode(word)

            myUrl = self.url + '?' + word

            links = self.loadPage(myUrl)

    def loadPage(self, url):
        req = urllib.request.Request(url, headers=self.ua_headers)
        html = urllib.request.urlopen(url).read()

        selector = etree.HTML(html)
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in links:
            link = 'http://tieba.baidu.com' + link
            self.loadImmage(link)

    def loadImmage(self, link):
        req = urllib.request.Request(link, headers=self.ua_headers)
        html = urllib.request.urlopen(req).read()
        selector = etree.HTML(html)

        imageLinks = selector.xpath('//img[@class="BDE_Image"]/@src')

        for imageLink in imageLinks:
            self.writeImages(imageLink)

    def writeImages(self, imageLink):
        print(imageLink)
        print("正在存储文件 %d ..." % self.userName)

        file = open('./images/' + str(self.userName) + '.png', 'wb')

        images = urllib.request.urlopen(imageLink).read()

        file.write(images)
        file.close()
        self.userName += 1


if __name__ == '__main__':
    mySpide = Spider()
    mySpide.tiebaSpider()
