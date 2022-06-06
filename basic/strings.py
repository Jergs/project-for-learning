# format
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

# other one
a = "{x}, {y}".format(x=5, y=12)
print(a)

# join
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

# replace
print("Hello ME".replace("ME", "world"))
#prints "Hello world"

# startswith
print("This is a sentence.".startswith("This"))
# prints "True"

# endswith
print("This is a sentence.".endswith("sentence."))
# prints "True"

# upper
print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

# lower
print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

# split
print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"