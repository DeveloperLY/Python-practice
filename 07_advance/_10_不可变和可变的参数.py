def test(num, num_list):
    print("函数开始执行")
    global gl_num
    gl_num = 100
    num_list = [1, 3, 5]
    print(num)
    print(num_list)
    print("函数执行完成")

gl_num = 88
gl_num_list = [2, 4, 6]
test(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
