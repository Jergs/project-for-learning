from itertools import count
from itertools import accumulate, takewhile
from itertools import product, permutations

for i in count(3):
    print(i)
    if i >= 11:
        break

print()
nums = list(range(8))
print(nums)
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

# combinatoric
print()
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
