class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("电锯")
tool3 = Tool("大锤子")

tool3.count = 88
print("工具对象总数 %d" % tool3.count)
print("====> %d" % Tool.count)

Tool.count = 99
print("工具对象总数 %d" % tool3.count)
print("工具对象总数 %d" % tool1.count)
print("====> %d" % Tool.count)
