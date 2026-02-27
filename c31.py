class Computer:
    def __init__(self):
        self.__maxprice = 500
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))
    def setmaxprice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setmaxprice(1000)
c.sell()