from sys import argv

#takes command line arguments and stores it in the variables
script, filename = argv

#uses the information in the commmand line to open a txt file
txt = open(filename)


print("Here's your file %r" %filename)
print(txt.read())

print("Type the filename again:")
file_again = input(">")
txt_again = open(file_again)

print(txt_again.read())