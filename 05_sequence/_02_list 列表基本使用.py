name_list = ["zhangsan", "lisi", "wangwu"]

print(name_list[0])

print(name_list.index("lisi"))

name_list[1] = "李四"

name_list.append("赵六")

name_list.insert(1, "孙二")

temp_list = ["jack", "tom", "sunny"]
name_list.extend(temp_list)

name_list.remove("wangwu")
name_list.pop()
name_list.pop(1)
name_list.clear()

print(name_list)
