class Website:
    """
    描述网站结构的信息
    """

    def __init__(self):
        matchingRule = [
            'h1.product-name',
            'table.price-list-table',
            'div.items>label.stock-number-color',
            'div.product-brand-con',
            'div.items span.pr25 span.color444',
            'div.param-wrap table.param-body',
            'div.pro-intr-txt',
            'div.items span.pr25 label.stock-number-color'
        ]
        self.goodsName = matchingRule[0]
        self.goodsPrice = matchingRule[1]
        self.minPacking = matchingRule[2]
        self.baseInfo = matchingRule[3]
        self.saleNum = matchingRule[4]
        self.goodsAttr = matchingRule[5]
        self.goodsDesc = matchingRule[6]
        self.stock = matchingRule[7]


