from sys import argv
#练习input和argv
script,user_name = argv
prompt = '>'
print(f"嗨 {user_name},我是脚本{script}.")
print(f"我想要问你几个问题。")
print(f"{user_name},你想要我干什么？")
likes = input(prompt)
print("{},你住在哪里呢？".format(user_name))
lives = input(prompt)
print(f"""
好的，那么你想要我{likes},你住在{lives}.
""")
