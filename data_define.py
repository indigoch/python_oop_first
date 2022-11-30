class Record:
    def __init__(self,date,order_id,money,province):
        self.money = money
        self.order_id = order_id
        self.date = date
        self.province = province

    def __str__(self):
        return f"{self.date},{self.money},{self.order_id},{self.province}"

        