class Calculator:
    num = 100

    def __init__(self,a,b):
        self.a= a
        self.b= b
        print("I am called automatically when object is created")

    def getData(self):
        print("executing method 1 in class")

    def summation(self):
        return self.a + self.b + Calculator.num



obj = Calculator(2,3)
obj.getData()
print(obj.summation())

obj1 = Calculator(5,6)
obj1.getData()
print(obj1.summation())
