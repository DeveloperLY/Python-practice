def print_info(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s]%s 是 %s" % (title, name, gender_text))

print_info("Tom")
print_info("Jack", "缺省值", True)
print_info("Rouse", False)
print_info("Rouse", gender=False)
