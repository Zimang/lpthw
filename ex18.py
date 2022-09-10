#def 创建函数
#两种形参

def print_two(*args):
    arg1,arg2=args
    print(f"arg1:{arg1}  arg2:{arg2}")


def print_ex(arg1,arg2):
    print(f"arg1:{arg1}  arg2:{arg2}")

print_two("黄子明","Zimang")
print_ex("黄子明","Zimang")
