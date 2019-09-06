class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 在喝水" % self.name)


tom = Cat()
tom.eat()
tom.drink()
tom.name = "Tome"
print(tom)
