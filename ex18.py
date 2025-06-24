def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")


def print_one(arg1):
    print(f"arg:{arg1}")

def print_none():
    print("i am empty inside")

print_two("Hello","World")
print_one("Hello")
print_none()