from sys import exit


def gold_room():
    print("这间房子满是黄金，你想带走多少？")
    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("嘿，学学数字吧")

    if how_much < 50:
        print("真棒，你并不贪婪，你赢了")
        exit(0)
    else:
        dead("你这贪婪的禽兽")

# 这个游戏太糟糕了
