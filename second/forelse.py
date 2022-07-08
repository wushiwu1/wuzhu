#for else 当循环正常结束时（没有被break，exit），则执行
# while else 同上

for d in range(2,101):

    for i in range(2,d):
        if d%i == 0:
            break
    else:
        print(f"{d} is 质数")
