# For loop
for i in range(0, 10):
    print(i)

print()

for i in range(10):
    print(i)

print()

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

print()
# loops with else
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")
