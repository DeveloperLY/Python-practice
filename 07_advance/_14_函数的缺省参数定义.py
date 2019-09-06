def print_info(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))

print_info("Tom")
print_info("Jack", True)
print_info("Rouse", False)
