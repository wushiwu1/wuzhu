#print ("hello")
name = "cece"
age = 26
hobbie = "giiler"
msg = '''
-------%s info -------
name: %s
age: %d
hobbie: %s
----------end-----------


''' % (name,name,age,hobbie)
print(msg)
# %s
# %d
# %f
msg2 = f'''
-------{name} info -------
name: {name}
age: {age}
hobbie: {hobbie}
----------end-----------


'''
print(msg2)