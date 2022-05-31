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