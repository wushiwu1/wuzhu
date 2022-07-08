# for i in range(10):
#     print(i)
# for name in ["hi","hello","reio"]
#     print(name)
# for h in "sjrc jack"
#     print(h)

# for i in range(100,50,-1): #倒叙
#    # if i >=50:
#     if i % 2 == 0 : #偶数
#         print(i)

##循环嵌套
for floor in range(9):
    print(f"第{floor}层")
    for room in range(1,10):
        print(f"房间是{floor}层{room}号")

###break & continue
#1、楼层打印跳过某层
for floor in range(9):
    print(f"第{floor}层")
    if floor == 3:
        print("不走三层")
        continue
    for room in range(1,10):
        if floor == 4 and room == 4:
            print("见鬼了！挂掉了")
            #exit() #退出程序
            break #结束循环，不再继续本楼层
        print(f"房间是{floor}层{room}号")
###标注位

