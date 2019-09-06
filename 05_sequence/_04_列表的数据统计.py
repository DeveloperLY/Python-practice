name_list = ["zhangsan", "lisi", "wangwu", "zhangsan", "zhangsan"]

list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

count = name_list.count("zhangsan")
print("zhangsan 出现了 %d 次" % count)

name_list.remove("zhangsan")
print(name_list)
