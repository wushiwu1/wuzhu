print("第一个任务")

age = int(input("请猜猜我的年龄："))

while age > 0:
    if age > 71:
        print("请往小了猜")
        age = int(input("请猜猜我的年龄："))
        continue
    elif age < 71:
        print("请往大了猜")
        age = int(input("请猜猜我的年龄："))
        continue
    else:
        print("猜对了！")
        break

print("第二个任务")
while True:
    money = int(input("请输入月工资："))
    if money <= 1000:
        print("老板，你自己玩吧")
    elif money <= 15000:
        print("老板，说的很好，但是我不听")
    elif money <= 20000:
        print("老板，你说的可以，可以一试下")
    elif money <= 30000:
        print("老板说啥都挺好，积极配合")
    elif money <= 50000:
        print("老板你一直对，不对也是对")
    else:
        print("公司就是我家")
        break

# if age>71:
#     print("我没有那么大！")
#     continue
# elif age<71:
#     print("猜小了哈！")
#     continue
# else:
#     print("终于猜对了！")
#     break


# for i in age:
#     while i>71:
#         print("我没有那么大！")
#         break
#     while i<71:
#         print("猜小了哈！")
#         break
#     while i==71:
#         print("猜对了")
#         break
