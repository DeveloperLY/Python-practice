class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 在喝水" % self.name)


tom = Cat()
tom.name = "Tome"
tom.eat()
tom.drink()
print(tom)

lazy_car = Cat()
lazy_car.name = "大懒猫"
lazy_car.eat()
lazy_car.drink()
print(lazy_car)
