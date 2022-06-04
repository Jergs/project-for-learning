def my_func(f, arg):
    return f(arg)


my_func(lambda x: 2 * x * x, 5)


# Another example

# named function
def polynomial(x):
    return x ** 2 + 5 * x + 4


print(polynomial(-4))

# lambda
print((lambda x: x ** 2 + 5 * x + 4)(-4))

# assign lambda to a variable, not recommended
multiply = lambda x, y: x * y
print(multiply(3, 2))
