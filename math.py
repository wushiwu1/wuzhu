for i in range(10):
    if i % 2 != 0:   #奇数
        print(i)

a = 1
b = 2
c = a + b
a = a + 1
print(c,a)

print(a==b and c>a)

list = ["新皇","cece"]

if '新皇' in list:
    print("包含")
else:
    print("不包含")
