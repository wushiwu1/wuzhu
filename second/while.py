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