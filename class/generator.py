import random
# 大写97-122
# 小写65-90
list = []
randType = random.randint(1, 3)
# 1小写，2大写，3suzhi5
for i in range(0, 5):
    if (randType == 1):
        list.append(chr(random.randint(65, 90)))
    elif (randType == 2):
        list.append(chr(random.randint(97, 112)))
    else:
        list.append(str(random.randint(0, 9)))
    randType = random.randint(1, 3)
result = "".join(list)
print(result)
