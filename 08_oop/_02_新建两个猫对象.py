class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

tom = Cat()
tom.eat()
tom.drink()
print(tom)

lazy_car = Cat()
lazy_car.eat()
lazy_car.drink()
print(lazy_car)

lazy_car2 = lazy_car
print(lazy_car2)
