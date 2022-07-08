#存款多少年才能翻倍？
#1万本金，利息0.0325/年，问连本带息多少年翻倍？
from typing import List

a=10000
b=0
# while True:
#     a=(a+a*0.0325)
#     b+=1
#     if a>=20000:
#         print(f"需要{b}年可以翻倍！")
#         break
##纠正
while a<20000:
    a += a*0.0325
    b+=1
else:
    print(f"需要{b}年可以翻倍！")


#2、小球坠落长度计算
# high=int(input("请输入高度（米）："))
# #print(type(high))
# speed=int(input("请输入初速度（米/秒）："))
# time=high / 9.8
# print(f"坠落长度为：{speed*time}米")
#1、有一个小球，从100米高空坠落，每次反弹之前一半高度，问10次反弹结束，小球经过多少米？



#猴子吃桃
#有一堆桃子，猴子每天吃总数的一半并多吃一个，吃了十天，
# 到第十一天只剩下一个桃子，问猴子吃之前，一共多少桃子？







#计算从1-100所有整数的和
a=0
for i in range(1,101):
    a+=i
else:
    print(f"100内整数之和为：{a}")

#寻找列表中最大值 最小值
list=[10,11,12,13,14]
#最小值
for i in list:
    for d in list:
        if i>d:
            break
    else:
        print(f"最小值：{i}")
#最大值
# for i in list:
#     for d in list:
#         if i<d:
#             break
#     else:
#         print(f"最大值：{i}")
##纠正：
max_n = list[0]  #假设最大值
for i in list:
    if i >max_n:  #交换
        max_n = i
print(f"最大值：{max_n}")

#寻找组合
#1、从两个列表里各取一个数，如果这两个数之和等于10，则以元组的方式输出这两个值
a=[1,2,3,4,5]
b=[6,7,8,9]
for i in a:
    for d in b:
        if i+d == 10:
            print(f"元组形式输出：({i},{d})")