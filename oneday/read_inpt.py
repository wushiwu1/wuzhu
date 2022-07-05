name = input("your name :").strip()
age = (input("your age :"))
if age.isdigit():
    age = int(age)
else:
    print("错误格式")
    print(type(age))


hobbie = input("your hobbie :").strip()
job = input("your job :").strip()
msg = f'''
----------{name}--------
your name is {name}
your age in {50-age} years,you will 50 age.
your hobbie : {hobbie}
your job is  {job}


--------END--------
'''
print(msg)