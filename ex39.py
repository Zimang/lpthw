#不能用i number访问除非存在引索为1,2,...i,...n
#.get来通过引索获取值
province = {
    "湖北省": "鄂",
    "湖南省": "湘",
    "浙江省": "浙"
}

cities = {
    "鄂": "武汉",
    "浙": "杭州",
    "湘": "长沙"
}


cities["鄂"] = "宜昌"
cities["浙"] = "宁波"

print(10 * "-")
print("湖北省", cities["鄂"])
print("浙江省", cities["浙"])

print(10 * "-")
print("湖北省", province["湖北省"])
print("浙江省", province["浙江省"])

print(10 * "-")
print("湖北省", cities[province["湖北省"]])
print("浙江省", cities[province["浙江省"]])

print(10 * "-")
for abbrev, city in list(cities.items()):
    print(f"{abbrev}有{city}")

print(10 * "-")
for provi, abbrev in list(province.items()):
    print(f"{provi}缩写是{abbrev}")
    print(f"并且有{cities[abbrev]}")

print(10 * "-")
provi = province.get("台湾省")

if not provi:
    print("暂时没有")
city = cities.get('TW', "不存在")
print(f"台湾省的城市有{city}")
print("-"*10)
province[1]=["wow","jesus"]
list_test=["wow","jesus"]
print(province[1])
print(list_test)
