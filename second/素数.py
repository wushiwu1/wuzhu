for d in range(2,101):
    num = True
    for i in range(2,d):
        if d%i == 0:
            num = False
    if num == True:
        print(f"{d} is 质数")
