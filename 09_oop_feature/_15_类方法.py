class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)
        
tool1 = Tool("斧头")
tool2 = Tool("电锯")

Tool.show_tool_count()
