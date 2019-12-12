from DbClass import DB

class Content:
    """
    所有文章/网页的共同基类
    """

    def __init__(self, goodsName = None, goodsPrice = None, minPacking = None, baseInfo = None, saleNum = None, goodsAttr = None, goodsDesc = None, stock = None, url = None):
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.minPacking = minPacking if minPacking != '' else '0'
        self.baseInfo = baseInfo
        self.saleNum = saleNum if saleNum != '' else '0'
        self.goodsAttr = goodsAttr
        self.goodsDesc = goodsDesc
        self.stock = stock if stock != '暂无库存' and stock != '' else '0'
        self.url = url
        self.DBModel = DB()

    def print(self):
        """
        用灵活的打印函数控制结果
        """
        print("goodsName: {}".format(self.goodsName))
        print("goodsPrice: {}".format(self.goodsPrice))
        print("minPacking:\n{}".format(self.minPacking))
        print("baseInfo:\n{}".format(self.baseInfo))
        print("saleNum: {}".format(self.saleNum))
        print("stock:\n{}".format(self.stock))
        print("goodsAttr: {}".format(self.goodsAttr))
        print("goodsDesc:\n{}".format(self.goodsDesc))

    def insert(self):
        if self.checkExist() == True :
            print('记录已存在')
            return False
        sql = "INSERT INTO `lcsc_goods_raw_data` " \
              "(`goods_name`, `min_packing`, `goods_price`, `base_info`, `goods_attr`, `stock`, `sale_num`, `goods_desc`, `source_url`) " \
              "VALUES " \
              "('" + self.goodsName + "', '" + self.minPacking + "', '" + self.goodsPrice + "', '" + self.baseInfo + "', '" + self.goodsAttr + "', '" + self.stock + "', '" + self.saleNum + "', '" + self.goodsDesc + "', '" + self.url + "');"

        result = self.DBModel.execute(sql, None)
        if result == True :
            print(self.goodsName + '采集成功')
        else :
            print(self.goodsName + '采集失败' + sql)

    def checkExist(self):
        selectSql = "SELECT goods_raw_data_id FROM lcsc_goods_raw_data WHERE source_url = '" + self.url + "'"
        result = self.DBModel.fetchone(selectSql)
        if result != None :
            return True
        else :
            return False