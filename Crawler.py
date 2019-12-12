import requests
from bs4 import BeautifulSoup
from Content import Content

class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        用于从一个BeautifulSoup对象和一个选择器获取内容的辅助函数。
        如果选择器没有找到对象，就返回空字符串
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        """
        从指定URL提取内容
        """
        bs = self.getPage(url)

        if bs is not None:
            if bs.find('title').get_text() != '您要访问的页面没有找到' :
                goodsName = self.safeGet(bs, site.goodsName)
                goodsPrice = self.safeGet(bs, site.goodsPrice)
                minPacking = self.safeGet(bs, site.minPacking)
                baseInfo = self.safeGet(bs, site.baseInfo)
                saleNum = self.safeGet(bs, site.saleNum)
                goodsAttr = self.safeGet(bs, site.goodsAttr)
                goodsDesc = self.safeGet(bs, site.goodsDesc)
                stock = self.safeGet(bs, site.stock)
                content = Content(goodsName, goodsPrice, minPacking, baseInfo, saleNum, goodsAttr, goodsDesc, stock, url)
                content.insert()
            else :
                print( url + '页面没有找到' )
        else :
            print( url + '访问失败' )
