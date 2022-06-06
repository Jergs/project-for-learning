file = open("../textfile.txt")

# write mode
# open("textfile.txt", "w")

# read mode
# open("textfile.txt", "r")
# open("textfile.txt")

# binary write mode
# open("textfile.txt", "wb")

file.close()

# read and print
file = open("../textfile.txt", "r")
cont = file.read()
print(cont)
file.close()

print()

# read bytes
file = open("../textfile.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# read lines
file = open("../textfile.txt", "r")
print(file.readlines())
file.close()

file = open("../textfile.txt", "r")
for line in file:
    print(line)
file.close()

# write deletes all content

# append adds to the end of file

# 'with' closes the file at the end
with open("../textfile.txt") as f:
    print(f.read())

# test case
file = open("../textfile.txt", "r")
book_list = file.readlines()
for book in book_list:
    letter = book[0]
    if book == book_list[len(book_list) - 1]:
        letters_num = str(len(book))
        print(letter + letters_num)
    else:
        letters_num = str(len(book) - 1)
        print(letter + letters_num)

file.close()
