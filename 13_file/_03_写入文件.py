# file = open("13_file/README", "w") # 会清空原来的内容
file = open("13_file/README", "a") # 在原内容尾部追加

file.write("Hello Python")
 
file.close()
