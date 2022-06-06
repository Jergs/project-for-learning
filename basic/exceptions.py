# try/except
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

# many excepts
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

# no error in except
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

# finally
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

# raise an exception
# raise NameError("Some error")

# raise in except
try:
    num = 5 / 0
except:
    print("An error occurred")
    raise

# assert
assert "1" != "w"

# else with try
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1 / 0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
   