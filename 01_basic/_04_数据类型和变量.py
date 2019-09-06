############# QQ 号码 #############

qq_number = '379509684'

qq_password = "123456"

print(qq_number)
print(qq_password)

############# 超市买苹果 #############

price = 8.5

weight = 7.3

money = weight * weight

money += 10

print(money)

############# 个人信息 #############

name = "DeveloperLY"
age = 18
gender = False
height = 1.81
weight = 80.0
print(name)

############# 买苹果增强版 #############

price_str = input("苹果的单价：")

weight_str = input("苹果的重量：")

# ❌
# money = price_str * weight_str

price = float(price_str)
weight = float(weight_str)

money = price * weight

print(money)

############# 买苹果改进 #############

price = float(input("苹果的单价："))

weight = float(input("苹果的重量："))

money = price * weight

print(money)