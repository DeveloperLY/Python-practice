def test(num, num_list):
    print("函数开始")
    num += num
    num_list += num_list
    # num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数结束")

gl_num = 9
gl_num_list = [1, 3, 5]
test(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
