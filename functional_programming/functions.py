# max
# min
# abs
# sum
# round

# all, any, enumerate
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)


# map, aka collection -> map in java
def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# filter, aka collection -> filter in java
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
