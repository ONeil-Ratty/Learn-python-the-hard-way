from sys import argv

script, filename = argv

print("We're going to erase %r" %filename)
print("If you dont want that, hit CTRL-C (^C)")
print("if you want to do this, Hit RETURN")

input("?")
print("opening the file...")

target = open(filename,"w")

print("Truncating the file, so long cruel world!!!")
target.truncate()

print("now write 3 new lines pls")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("im going to write them to the file now")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and now we closed it")
target.close()

print("do you want to read its contents")
file = open(filename)
print(file.read())