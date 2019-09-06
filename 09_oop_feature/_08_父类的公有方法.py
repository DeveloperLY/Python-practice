class A:
    def __init__(self):
        self.num1 = 10086
        self.__num2 = 10010

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法 %d" % self.num1)

class B(A):
    def demo(self):
        print("子类访问父类公共属性 %d" % self.num1)
        self.test()
        pass


b = B()
b.demo()
print(b)
