words = ["hello", "world"]
print(words)
print(words[0])

# Different types
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

# Strings as lists
some_str = "Hello world!"
print(some_str[6])

# 'in' Operator (contains)
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# append to the list
words.append("newWord")

# length of the list
print(len(words))

# insert to a position
words.insert(0, "someWord")
print(words)

# other useful methods
# max
# min
# count
# remove
# reverse
# index

# slicing
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

# not limited from one of the sides
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# slice with step
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

# negatives count from the end of the list
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# reverse list
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::-1])

# tricky
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

# comprehensions
cubes = [i ** 3 for i in range(5)]
print(cubes)

# other example
evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)
