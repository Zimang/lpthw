ten_thing="苹果 橘子 灯泡"
stuff=ten_thing.split(' ')
more_stuff=["白天","夜晚","歌曲"]

while len(stuff)!=5:
    #想不到pop的竟然是最后面的
    next_one=more_stuff.pop()
    print("添加: ",next_one)
    stuff.append(next_one)
    print(f"现在有{len(stuff)}个词语")

print("我们开始",stuff)

print("让我们对stuff做些什么吧")
print(stuff[1])
print(stuff[-1])
#0是第一个，-1是最后一个
print(" ".join(stuff))
#[3:5]从3和4截出一段
print("#".join(stuff[3:5]))

#list的特点
#有序，随机访问，线性遍历
