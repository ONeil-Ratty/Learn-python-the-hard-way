def add(a,b):
    print(f"we are adding {a} and {b}")
    return a + b

def sub(a,b):
    print(f"we are subtracting {a} and {b}")
    return a - b

def multiply(a,b):
    print(f"we are multiplaying {a} and {b}")
    return a * b

def division(a,b):
    print(f"we are division {a} and {b}")
    return a / b

print("lets do some math with functions")

age = add(10,10)
height = sub(200,25)
weight = multiply(10,2)
iQ = division(300,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iQ}")

print("here is a puzzle")
what = add(age,sub(height,multiply(weight,division(iQ,2))))

print(f"that becomes {what} can you do it by hand?")