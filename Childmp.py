from Oopsdemo import Calculator


class Childmp(Calculator):
    num2= 200

    def __init__(self):
        Calculator.__init__(self,2, 1)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()


obj = Childmp()
print(obj.getcompletedata())
print(obj.summation())