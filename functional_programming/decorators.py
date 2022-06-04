def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()


@decor
def print_another_text():
    print("Hello world!")


print_another_text()
