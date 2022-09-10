from sys import argv
from os.path import exists
#一个文件要么读(a,r)要么写(x,w)
#  len(string)显示字节长度
#  exists()判断文件是否存在
#  from os.path import exists
#  if():
#       ...
#  elif():
#       ...
#  else:
#
scirpt, file_one , file_two = argv

print(f"复制文件1到文件2")
if(exists(file_one)):
    target_1=open(file_one,"r")
    target_2=open(file_two,"w")
    content_one=target_1.read()
    le=len(content_one)
    target_2.truncate()
    target_2.write(content_one)
    print(f"现在去看看吧！该文件有{le}字节长")
else:
    print("该文件不存在呀")
