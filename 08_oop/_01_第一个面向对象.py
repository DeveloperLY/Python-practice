class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")
    
tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)
