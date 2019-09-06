def create_num(all_num):
    print("-----1-----")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("-----2-----")
        # print(a)
        yield a
        print("-----3-----")
        a, b = b, a + b
        current_num += 1
        print("-----4-----")

obj = create_num(20)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)
obj2 = create_num(2)
ret = next(obj2)

# for num in obj:
#     print(num)
