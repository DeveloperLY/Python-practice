def test(*args, **kwargs):
    print(args)
    print(kwargs)

gl_nums = (1, 4, 5)
gl_dict = {"name": "Sunny", "age": 18}

# test(gl_nums, gl_dict)
test(*gl_nums, **gl_dict)

test(1, 2, 3, name="Jack", age=22)
