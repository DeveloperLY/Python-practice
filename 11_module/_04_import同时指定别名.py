import _01_测试模块1 as DogModule
import _02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
