class A:
    def __init__(self):
        self.num1 = 10086
        self.__num2 = 10010

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

class B(A):
    def demo(self):
        # print("访问父类的私有属性 %d" % self.__num2)
        # self.__test()
        pass


b = B()
b.demo()
print(b)
