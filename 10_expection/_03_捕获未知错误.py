try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("除数不能为0")
except Exception as result:
    print("未知错误 %s" % result)

print("*" * 50)
