from sys import argv
script, input_file = argv

#打印所有内容
def print_all(f):
    print(f.read())

#拨开指针
def rewind(f):
    f.seek(0)

#打印一行
def print_a_line(line_count,f):
    print(line_count,f.readline())
#current_line没有任何意义

current_file = open(input_file)
print("现在，让我们打印整个文件：\n")
print_all(current_file)
print("现在让我们回归开头，如同拨动胶片触针")
rewind(current_file)

current_line=1
print_a_line(current_line,current_file)
current_line+=1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line,current_file)
