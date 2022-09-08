from sys import argv
#argv 至少要分配给一个变量 script
script , filename = argv
#将某一文件打开,open并不会返回文件的内容，仅仅创建file object
txt = open(filename)
print(f"你的文件叫 {filename}")
#可以读取md吗？
#这里的xx.read中的xx不是文件类型，而是文件名称
#read 读不了有GBK编码的文件，意味着不能有中文
#调用文件的read方法
print(txt.read())
txt.close()

print("请再次输入文件名：")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()

#文件打开两次也并没有err
