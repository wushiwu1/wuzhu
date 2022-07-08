#2、99乘法表

for high in range(1,10):
    for i in range(1,10):
        if high > i:
            print(f"{high}*{i}={high*i} ",end=" ")
        if high == i:
            print(f"{high}*{i}={high*i}")

#纠正代码
for high in range(1,10):
    for i in range(1,high+1):
        print(f"{high}*{i}={high*i}",end=" ")
    print()
