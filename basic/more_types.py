# None like null in java
var = print()
if var is None:
    print("None = var")

# Dictionary aka map
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

empty = {}

# 'in' with dictionary
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

# get
pairs = {1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

# tuples (aka immutable lists). Faster than lists
words = ("spam", "eggs", "sausages",)
print(words[0])


