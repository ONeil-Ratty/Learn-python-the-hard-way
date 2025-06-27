from sys import argv


script, file_name = argv

currentFile = open(file_name)

def print_all(file):
    print(file.read())

def rewind(file):
    file.seek(0)

def print_line(line_count,file):
    print(line_count, file.readline())





print("first lets print the whole file")
print_all(currentFile)

print("now lets rewind, kinf of like a tape")
rewind(currentFile)

print("lets print three lines:")

currentLine = 1
print_line(currentLine,currentFile)

currentLine = currentLine + 1
print_line(currentLine,currentFile)

currentLine = currentLine + 1
print_line(currentLine,currentFile)


