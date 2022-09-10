#读写文件
#close()关闭并保存文件
#read()读取文件内容，可以分配给变量
#readline()读取文件的一行
#truncate()清空文件
#write("stuff") 写入"stuff"至文件，它需要一个参数
#seek(0) 将读写位置移至文件开头

from sys import argv
scirpt,filename=argv
# print(f"我们现在将要清除{filename}.")
# print("如果你不想这样做，键入CTRL-C (^C).")
# print("如果你想这样做，键入Return")
#
# input("?")
#
# print("打开文件")
# target=open(filename,"w")
# print("正在清空文件，GOODBYE")
# target.truncate()
#
# print("现在我问你输入文件哪三行文本.")
# line1=input("第一行")
# line2=input("第二行")
# line3=input("第三行")
#
# print("我将要写入这三行文本")
# target.write(line1)
# target.write('\r\n')
# target.write(line2)
# target.write('\r\n')
# target.write(line3)
# target.write('\r\n')
#
# print("现在，我们关闭文件")

print("新建文件{filename}")
target=open(filename,"x")
content=input("写入内容")
target.write(content)
target.close()
