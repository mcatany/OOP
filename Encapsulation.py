# Encapsulation

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

# Example of usage
if __name__ == "__main__":	
	c = Computer()
	c.sell()

	c.__maxprice = 1000

	c.sell()

	c.setMaxPrice(1000)

	c.sell()


