result=[("a",111),("b",222),("c",333)]
newOrder=[]
result.sort(key=lambda x:x[1],reverse=True)
print(result)
##列表的sort用法
##key排序项，reverse降序与否
##元组无法排序但是可以生成新的元组--sorted
