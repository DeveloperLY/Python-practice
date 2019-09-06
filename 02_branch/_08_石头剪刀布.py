import random

player = int(input("请输入您要出的拳 剪刀(1) / 石头(2) / 布(3)："))

computer = random.randint(1, 3)

print("玩家出的拳头是：%d \n电脑出的拳头是：%d" % (player, computer))

if ((player == 1 and computer == 3) 
    or (player == 2 and computer == 1) 
    or (player == 3 and computer == 2)):
    print("赢了，电脑真是太弱了！")
elif player == computer:
    print("平局，再来一局")
else:
    print("输了，决战到天亮！")2