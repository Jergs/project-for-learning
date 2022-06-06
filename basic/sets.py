# Set is basically set from java (no duplicates)
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

# Another example
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
print()

# Operations on sets
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)   # OR
print(first & second)   # AND
print(first - second)   # 1st but not second
print(second - first)   # same
print(first ^ second)   # NOR (in either, but not both)
