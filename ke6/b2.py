name = 'yoyo'
age = 20

x = "my name is {0}, age is {1}, name is {0}".format(name, age)
print(x)

y = "my name is {name}, age is {age}, name is {name}".format(name=name, age=age)
print(y)