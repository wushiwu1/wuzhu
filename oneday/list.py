name1 = "money"
name2 = "celina"
name3 = "dina"
print("字符串输出",name1,name2,name3)

names = "Monkey,celina,dina,blackgire"
print(names)
name_list = ["Monkey","celina","dina","blackgire"]
print("输出列表元素")
print(name_list[2])

print("循环输出列表")
for girl in name_list:
    print(f"hello,how are you? {girl}")

print("增删改查")
name_list.append("mali")
name_list.insert(0,"皇帝")
print(name_list)
name_list[0] = "新皇"
print("mali位置：",name_list.index("mali"))
print("修改第一个人",name_list)
name_list.remove("mali")
print("mali 删除:",name_list)

print("切片",name_list[-2:])
print(name_list[0:5:2])
print("嵌套")
name_list.append(["冰冰","22岁","172cm"])
print(name_list[-1][1])
name_list[-1][1] = "23岁"
print(name_list)
